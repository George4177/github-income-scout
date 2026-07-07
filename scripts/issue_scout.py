#!/usr/bin/env python3
"""Find and score low-risk GitHub issue opportunities."""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


GITHUB_SEARCH_URL = "https://api.github.com/search/issues"


LOW_RISK_KEYWORDS = {
    "docs": 10,
    "documentation": 10,
    "readme": 10,
    "github actions": 8,
    "ci": 8,
    "test": 6,
    "bug": 6,
    "python": 5,
    "automation": 5,
    "good first issue": 5,
    "help wanted": 5,
}

HIGH_RISK_KEYWORDS = {
    "exploit": -30,
    "bypass": -30,
    "credential": -25,
    "token": -20,
    "scrape": -15,
    "spam": -30,
    "trading": -12,
    "casino": -20,
    "adult": -20,
    "impersonation": -25,
    "privilege escalation": -30,
    "request smuggling": -30,
    "xs-search": -25,
    "star +": -20,
    "star and": -20,
    "review an open pr": -20,
}

REJECT_KEYWORDS = {
    "exploit": "security exploit work",
    "bypass": "bypass or circumvention work",
    "credential": "credential-sensitive work",
    "impersonation": "impersonation risk",
    "privilege escalation": "security exploitation work",
    "request smuggling": "security exploitation work",
    "xs-search": "security exploitation work",
    "spam": "spam or platform-abuse risk",
    "star +": "fake-engagement risk",
    "star and": "fake-engagement risk",
    "review an open pr": "fake-engagement risk",
    "casino": "restricted/high-risk vertical",
    "adult": "restricted/high-risk vertical",
}


@dataclass
class Opportunity:
    title: str
    url: str
    repository: str
    labels: list[str]
    body: str
    comments: int
    assignees: list[str]
    created_at: str
    updated_at: str
    score: int
    task_type: str
    difficulty: str
    estimated_value: str
    estimated_time: str
    acceptance: str
    risk: str
    worth_doing: str
    rejected: bool
    rejection_reason: str
    repo_stars: int | None
    repo_forks: int | None
    repo_pushed_at: str
    repo_health: str


@dataclass
class ScoutResult:
    accepted: list[Opportunity]
    rejected: list[Opportunity]


def rejection_reason(text: str) -> str:
    reasons = []
    for keyword, reason in REJECT_KEYWORDS.items():
        if keyword in text and reason not in reasons:
            reasons.append(reason)
    return "; ".join(reasons)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Missing file: {path}") from None
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from None


def github_get(url: str) -> dict[str, Any]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-income-scout",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API error {exc.code}: {detail[:300]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc


def search_issues(query: str, per_page: int) -> list[dict[str, Any]]:
    params = {
        "q": query,
        "sort": "updated",
        "order": "desc",
        "per_page": str(per_page),
    }
    url = f"{GITHUB_SEARCH_URL}?{urllib.parse.urlencode(params)}"
    data = github_get(url)
    return list(data.get("items", []))


def repo_name(item: dict[str, Any]) -> str:
    repo_url = item.get("repository_url", "")
    return repo_url.rsplit("/", 2)[-2] + "/" + repo_url.rsplit("/", 1)[-1] if repo_url else "unknown"


def repo_health(repo: dict[str, Any] | None) -> str:
    if not repo:
        return "not checked"
    pushed_at = repo.get("pushed_at") or ""
    archived = bool(repo.get("archived"))
    disabled = bool(repo.get("disabled"))
    stars = int(repo.get("stargazers_count") or 0)
    if archived or disabled:
        return "avoid: archived or disabled"
    if not pushed_at:
        return "unknown"
    year = int(pushed_at[:4]) if re.match(r"^\d{4}", pushed_at) else 0
    current_year = int(time.strftime("%Y"))
    if year and current_year - year >= 2:
        return "risky: no recent push"
    if stars >= 50:
        return "active-looking"
    return "small/needs manual check"


def classify(text: str, labels: list[str]) -> str:
    haystack = f"{text} {' '.join(labels)}".lower()
    if "github actions" in haystack or re.search(r"\bci\b|\bci/cd\b", haystack):
        return "CI/CD fix"
    if "docs" in haystack or "documentation" in haystack or "readme" in haystack:
        return "Documentation/README"
    if "tool" in haystack or "automation" in haystack:
        return "Small tool"
    if "bug" in haystack:
        return "Bug fix"
    return "Open-source contribution"


def score_issue(item: dict[str, Any], repo: dict[str, Any] | None = None) -> Opportunity:
    labels = [label.get("name", "") for label in item.get("labels", [])]
    assignees = [assignee.get("login", "") for assignee in item.get("assignees", []) if assignee.get("login")]
    title = item.get("title", "")
    body = item.get("body") or ""
    haystack = f"{title} {body} {' '.join(labels)}".lower()
    reject_reason = rejection_reason(haystack)
    comments = int(item.get("comments", 0))

    score = 50
    for word, delta in LOW_RISK_KEYWORDS.items():
        if word in haystack:
            score += delta
    for word, delta in HIGH_RISK_KEYWORDS.items():
        if word in haystack:
            score += delta
    if assignees:
        score -= 20
    if comments > 20:
        score -= 28
    elif comments >= 4:
        score -= 20
    health = repo_health(repo)
    if health == "active-looking":
        score += 4
    elif health.startswith("risky"):
        score -= 8
    elif health.startswith("avoid"):
        score -= 15
    if "bounty" in haystack:
        score += 8
    if "good first issue" in haystack and "new-contributors-only" not in haystack:
        score += 3

    score = max(0, min(score, 100))
    task_type = classify(haystack, labels)

    if reject_reason:
        score = min(score, 35)

    if reject_reason:
        worth = "No, rejected by safety filter"
    elif score >= 75:
        worth = "Yes, inspect README and contribution guide"
    elif score >= 62:
        worth = "Maybe, verify maintainer activity first"
    else:
        worth = "No, keep as backup"

    if task_type in {"Documentation/README", "Small tool"}:
        difficulty = "Low-Medium"
        estimated_time = "1-4 hours"
    elif task_type == "CI/CD fix":
        difficulty = "Medium"
        estimated_time = "2-6 hours"
    else:
        difficulty = "Medium"
        estimated_time = "3-8 hours"

    estimated_value = "Direct bounty only if the issue explicitly links a bounty; otherwise portfolio/lead value"
    acceptance = "Issue scope is clear, tests/docs can prove the change, maintainer accepts PR"
    risk_notes = []
    if assignees:
        risk_notes.append(f"already assigned to {', '.join(assignees)}")
    if comments >= 4:
        risk_notes.append("multiple comments; may already be claimed or noisy")
    if reject_reason:
        risk_notes.append(reject_reason)
    if not risk_notes:
        risk_notes.append("Maintainer inactivity, hidden complexity, duplicate PRs, unclear bounty terms")
    risk = "; ".join(risk_notes)

    return Opportunity(
        title=title,
        url=item.get("html_url", ""),
        repository=repo_name(item),
        labels=labels,
        body=body,
        comments=comments,
        assignees=assignees,
        created_at=item.get("created_at", ""),
        updated_at=item.get("updated_at", ""),
        score=score,
        task_type=task_type,
        difficulty=difficulty,
        estimated_value=estimated_value,
        estimated_time=estimated_time,
        acceptance=acceptance,
        risk=risk,
        worth_doing=worth,
        rejected=bool(reject_reason),
        rejection_reason=reject_reason,
        repo_stars=None if repo is None else int(repo.get("stargazers_count") or 0),
        repo_forks=None if repo is None else int(repo.get("forks_count") or 0),
        repo_pushed_at="" if repo is None else str(repo.get("pushed_at") or ""),
        repo_health=health,
    )


def render_markdown(opportunities: list[Opportunity], source: str, rejected: list[Opportunity] | None = None) -> str:
    rejected = rejected or []
    lines = [
        "# GitHub Opportunity Report",
        "",
        f"Source: {source}",
        f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "| Score | Project | Task | Difficulty | Time | Worth Doing | Link |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for item in sorted(opportunities, key=lambda x: x.score, reverse=True):
        lines.append(
            f"| {item.score} | {item.repository} | {item.task_type} | {item.difficulty} | "
            f"{item.estimated_time} | {item.worth_doing} | [issue]({item.url}) |"
        )

    if rejected:
        lines.extend(
            [
                "",
                "## Rejected By Safety Filter",
                "",
                "| Project | Reason | Link |",
                "| --- | --- | --- |",
            ]
        )
        for item in sorted(rejected, key=lambda x: x.repository):
            lines.append(f"| {item.repository} | {item.rejection_reason} | [issue]({item.url}) |")

    lines.extend(["", "## Details", ""])
    for item in sorted(opportunities, key=lambda x: x.score, reverse=True):
        lines.extend(
            [
                f"### {item.repository}: {item.title}",
                "",
                f"- Link: {item.url}",
                f"- Labels: {', '.join(item.labels) if item.labels else 'none'}",
                f"- Task type: {item.task_type}",
                f"- Estimated difficulty: {item.difficulty}",
                f"- Estimated value: {item.estimated_value}",
                f"- Estimated time: {item.estimated_time}",
                f"- Repository health: {item.repo_health}",
                f"- Acceptance standard: {item.acceptance}",
                f"- Failure risk: {item.risk}",
                f"- Decision: {item.worth_doing}",
                "",
            ]
        )
    return "\n".join(lines)


def opportunity_to_row(item: Opportunity) -> dict[str, Any]:
    return {
        "score": item.score,
        "repository": item.repository,
        "title": item.title,
        "url": item.url,
        "labels": ", ".join(item.labels),
        "assignees": ", ".join(item.assignees),
        "task_type": item.task_type,
        "difficulty": item.difficulty,
        "estimated_value": item.estimated_value,
        "estimated_time": item.estimated_time,
        "acceptance": item.acceptance,
        "risk": item.risk,
        "worth_doing": item.worth_doing,
        "rejected": item.rejected,
        "rejection_reason": item.rejection_reason,
        "repo_stars": item.repo_stars,
        "repo_forks": item.repo_forks,
        "repo_pushed_at": item.repo_pushed_at,
        "repo_health": item.repo_health,
        "comments": item.comments,
        "created_at": item.created_at,
        "updated_at": item.updated_at,
    }


def render_json(results: ScoutResult, source: str, include_rejected: bool) -> str:
    data: dict[str, Any] = {
        "source": source,
        "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "accepted": [opportunity_to_row(item) for item in sorted(results.accepted, key=lambda x: x.score, reverse=True)],
    }
    if include_rejected:
        data["rejected"] = [opportunity_to_row(item) for item in sorted(results.rejected, key=lambda x: x.repository)]
    return json.dumps(data, ensure_ascii=False, indent=2)


def render_csv(results: ScoutResult, include_rejected: bool) -> str:
    fields = [
        "score",
        "repository",
        "title",
        "url",
        "task_type",
        "difficulty",
        "estimated_time",
        "worth_doing",
        "rejected",
        "rejection_reason",
        "risk",
        "comments",
        "assignees",
        "repo_health",
        "repo_stars",
        "repo_pushed_at",
        "updated_at",
    ]
    rows = [opportunity_to_row(item) for item in sorted(results.accepted, key=lambda x: x.score, reverse=True)]
    if include_rejected:
        rows.extend(opportunity_to_row(item) for item in sorted(results.rejected, key=lambda x: x.repository))

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def render_report(results: ScoutResult, source: str, output_format: str, include_rejected: bool) -> str:
    if output_format == "markdown":
        return render_markdown(results.accepted, source, results.rejected if include_rejected else None)
    if output_format == "json":
        return render_json(results, source, include_rejected)
    if output_format == "csv":
        return render_csv(results, include_rejected)
    raise ValueError(f"Unsupported format: {output_format}")


def split_results(opportunities: list[Opportunity], min_score: int) -> ScoutResult:
    accepted = [item for item in opportunities if not item.rejected and item.score >= min_score]
    rejected = [item for item in opportunities if item.rejected or item.score < min_score]
    return ScoutResult(accepted=accepted, rejected=rejected)


def fetch_repo_metadata(item: dict[str, Any]) -> dict[str, Any] | None:
    repo_url = item.get("repository_url")
    if not repo_url:
        return None
    return github_get(repo_url)


def collect_from_config(config_path: Path, enrich_repos: bool = False) -> list[Opportunity]:
    config = load_json(config_path)
    queries = config.get("queries", [])
    per_page = int(config.get("per_page", 10))
    if not queries:
        raise SystemExit("Config must include at least one query.")

    seen: set[str] = set()
    opportunities: list[Opportunity] = []
    for query in queries:
        for item in search_issues(query, per_page):
            url = item.get("html_url", "")
            if not url or url in seen:
                continue
            seen.add(url)
            repo = fetch_repo_metadata(item) if enrich_repos else None
            opportunities.append(score_issue(item, repo=repo))
    return opportunities


def collect_offline(path: Path) -> list[Opportunity]:
    data = load_json(path)
    items = data if isinstance(data, list) else data.get("items", [])
    if not isinstance(items, list):
        raise SystemExit("Offline input must be a list or an object with an items list.")
    return [score_issue(item, repo=item.get("repository") if isinstance(item.get("repository"), dict) else None) for item in items]


def main() -> int:
    parser = argparse.ArgumentParser(description="Score low-risk GitHub issue opportunities.")
    parser.add_argument("--config", type=Path, help="JSON config with GitHub search queries.")
    parser.add_argument("--offline", type=Path, help="Offline GitHub API issue JSON for testing.")
    parser.add_argument("--min-score", type=int, default=0, help="Hide non-rejected opportunities below this score.")
    parser.add_argument(
        "--enrich-repos",
        action="store_true",
        help="Fetch repository metadata for health signals. Adds one GitHub API request per unique issue repository.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json", "csv"),
        default="markdown",
        help="Report format.",
    )
    parser.add_argument(
        "--include-rejected",
        action="store_true",
        help="Include a rejected-by-safety-filter table in the report.",
    )
    parser.add_argument(
        "--output",
        default="reports/opportunities.md",
        help="Markdown output path, or '-' to print to stdout.",
    )
    args = parser.parse_args()

    if bool(args.config) == bool(args.offline):
        parser.error("Pass exactly one of --config or --offline.")

    try:
        opportunities = collect_offline(args.offline) if args.offline else collect_from_config(args.config, args.enrich_repos)
        results = split_results(opportunities, args.min_score)
        source = "offline sample" if args.offline else str(args.config)
        report = render_report(results, source, args.format, args.include_rejected)
        if args.output == "-":
            print(report)
        else:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(report, encoding="utf-8")
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.output != "-":
        print(f"Wrote {args.output} with {len(results.accepted)} opportunities.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
