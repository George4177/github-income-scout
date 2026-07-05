#!/usr/bin/env python3
"""Build a client-ready Starter Audit brief from opportunity JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_BOUNDARIES = [
    "No income, bounty, merge, or sponsorship guarantees.",
    "No exploit work, fake engagement, credential handling, spam, or platform-rule bypasses.",
    "Recommendations are based on public issue data and should be rechecked before posting or opening a PR.",
]


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc


def normalize_opportunities(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, dict) and isinstance(data.get("accepted"), list):
        return [item for item in data["accepted"] if isinstance(item, dict)]
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    raise ValueError("opportunity JSON must be a list or an object with an 'accepted' list")


def pick_text(item: dict[str, Any], key: str, default: str = "") -> str:
    value = item.get(key, default)
    return str(value).strip() if value is not None else default


def default_recommendation(task_type: str) -> str:
    normalized = task_type.lower()
    if "documentation" in normalized or "docs" in normalized:
        return "Yes, low-risk if the surrounding docs confirm the requested behavior"
    if "small tool" in normalized or "tool" in normalized:
        return "Yes, good first implementation candidate after checking for duplicate PRs"
    if "bug" in normalized:
        return "Maybe, worthwhile after reproducing the bug locally"
    return "Maybe, verify maintainer activity and acceptance details first"


def default_acceptance(task_type: str) -> str:
    normalized = task_type.lower()
    if "documentation" in normalized or "docs" in normalized:
        return "Docs clearly cover the requested behavior and match current implementation"
    if "small tool" in normalized or "tool" in normalized:
        return "Tool matches the requested signature, examples work, and project tests pass"
    if "bug" in normalized:
        return "Bug is reproduced, fixed, and covered by a focused test or clear manual verification"
    return "Issue scope is clear, tests or docs prove the change, and the maintainer accepts the PR"


def default_risk(task_type: str) -> str:
    normalized = task_type.lower()
    if "documentation" in normalized or "docs" in normalized:
        return "Docs may require implementation reading and maintainer wording preferences"
    if "small tool" in normalized or "tool" in normalized:
        return "Duplicate PRs, project-specific style, or hidden edge cases"
    if "bug" in normalized:
        return "Local reproduction or domain setup may take longer than expected"
    return "Maintainer inactivity, hidden complexity, duplicate PRs, unclear bounty terms"


def load_client_profile(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {
            "client_name": "Starter Audit client",
            "skills": ["Python", "automation", "GitHub Actions", "documentation"],
            "weekly_hours": "2-4",
            "preferred_tasks": ["small tools", "docs", "CI fixes"],
            "avoid": ["security exploit work", "fake engagement", "unclear bounties"],
            "budget_note": "Starter Audit scope: USD 29-49 depending on customization.",
        }
    data = load_json(path)
    if not isinstance(data, dict):
        raise ValueError("client profile must be a JSON object")
    return data


def render_list(values: Any) -> str:
    if isinstance(values, list):
        cleaned = [str(value).strip() for value in values if str(value).strip()]
        return ", ".join(cleaned) if cleaned else "Not specified"
    value = str(values).strip()
    return value if value else "Not specified"


def render_opportunity(index: int, item: dict[str, Any]) -> list[str]:
    title = pick_text(item, "title", "Untitled opportunity")
    repository = pick_text(item, "repository", "unknown/repository")
    url = pick_text(item, "url") or pick_text(item, "html_url")
    score = pick_text(item, "score", "not scored")
    task_type = pick_text(item, "task_type", "Open-source contribution")
    difficulty = pick_text(item, "difficulty", "Medium")
    estimated_time = pick_text(item, "estimated_time", "3-8 hours")
    worth_doing = pick_text(item, "worth_doing", default_recommendation(task_type))
    risk = pick_text(item, "risk", default_risk(task_type))
    acceptance = pick_text(item, "acceptance", default_acceptance(task_type))

    lines = [
        f"### {index}. {repository}: {title}",
        "",
        f"- Link: {url or 'Not provided'}",
        f"- Score: {score}",
        f"- Task type: {task_type}",
        f"- Estimated difficulty: {difficulty}",
        f"- Estimated time: {estimated_time}",
        f"- Recommendation: {worth_doing}",
        f"- Acceptance standard: {acceptance}",
        f"- Main risk: {risk}",
        "",
    ]
    return lines


def render_brief(profile: dict[str, Any], opportunities: list[dict[str, Any]], max_items: int) -> str:
    accepted = sorted(
        opportunities,
        key=lambda item: int(item.get("score", 0) or 0),
        reverse=True,
    )[:max_items]
    client_name = str(profile.get("client_name", "Starter Audit client")).strip() or "Starter Audit client"

    lines = [
        f"# Starter Audit Brief: {client_name}",
        "",
        "## Client Fit",
        "",
        f"- Skills: {render_list(profile.get('skills'))}",
        f"- Weekly time available: {render_list(profile.get('weekly_hours'))}",
        f"- Preferred tasks: {render_list(profile.get('preferred_tasks'))}",
        f"- Avoid: {render_list(profile.get('avoid'))}",
        f"- Budget note: {render_list(profile.get('budget_note'))}",
        "",
        "## Recommended Opportunities",
        "",
    ]
    if not accepted:
        lines.append("No opportunities met the current filter. Re-run the scan with broader queries or a lower minimum score.")
    for index, item in enumerate(accepted, start=1):
        lines.extend(render_opportunity(index, item))

    lines.extend(
        [
            "## Suggested First Action",
            "",
            "Start with the first opportunity only after rechecking that the issue is still open, unassigned, and not already covered by a newer pull request.",
            "",
            "## Delivery Boundaries",
            "",
        ]
    )
    for boundary in DEFAULT_BOUNDARIES:
        lines.append(f"- {boundary}")
    lines.extend(
        [
            "",
            "## Optional Follow-Up Service",
            "",
            "If the client chooses one opportunity, the next paid step can be a scoped implementation plan, branch preparation, test plan, and pull request description.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a client-ready Starter Audit brief.")
    parser.add_argument("--opportunities", type=Path, required=True, help="JSON output from issue_scout.py or build_audit_bundle.py.")
    parser.add_argument("--client-profile", type=Path, help="Optional JSON client profile.")
    parser.add_argument("--output", type=Path, default=Path("-"), help="Markdown output path, or '-' for stdout.")
    parser.add_argument("--max-items", type=int, default=5)
    args = parser.parse_args()

    if args.max_items < 1:
        parser.error("--max-items must be at least 1")

    try:
        profile = load_client_profile(args.client_profile)
        opportunities = normalize_opportunities(load_json(args.opportunities))
        brief = render_brief(profile, opportunities, args.max_items)
        if str(args.output) == "-":
            print(brief, end="")
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(brief, encoding="utf-8")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
