#!/usr/bin/env python3
"""Build a Starter Audit delivery bundle in Markdown, HTML, CSV, and JSON."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ISSUE_SCOUT_PATH = ROOT / "scripts" / "issue_scout.py"


def load_issue_scout():
    spec = importlib.util.spec_from_file_location("issue_scout", ISSUE_SCOUT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {ISSUE_SCOUT_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["issue_scout"] = module
    spec.loader.exec_module(module)
    return module


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_summary(results, source: str, output_dir: Path, include_rejected: bool) -> str:
    accepted_count = len(results.accepted)
    rejected_count = len(results.rejected) if include_rejected else 0
    top = sorted(results.accepted, key=lambda item: item.score, reverse=True)[:3]
    lines = [
        "# Starter Audit Bundle Summary",
        "",
        f"- Source: `{source}`",
        f"- Output directory: `{output_dir}`",
        f"- Accepted opportunities: {accepted_count}",
        f"- Rejected or hidden matches: {rejected_count}",
        "",
        "## Top Actions",
        "",
    ]
    if not top:
        lines.append("No accepted opportunities met the current filters.")
    for index, item in enumerate(top, start=1):
        lines.extend(
            [
                f"{index}. [{item.repository}: {item.title}]({item.url})",
                f"   - Score: {item.score}",
                f"   - Task: {item.task_type}",
                f"   - Time: {item.estimated_time}",
                f"   - Repository health: {item.repo_health}",
                f"   - Decision: {item.worth_doing}",
            ]
        )
    lines.extend(
        [
            "",
            "## Delivery Files",
            "",
            "- `audit_report.md`: client-readable report",
            "- `audit_report.html`: browser-ready and print-friendly report",
            "- `opportunities.csv`: spreadsheet-friendly export",
            "- `opportunities.json`: automation-friendly export",
            "",
            "This bundle does not guarantee income, merged PRs, sponsorship, or bounty awards.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Starter Audit delivery bundle.")
    parser.add_argument("--config", type=Path, help="JSON config with GitHub search queries.")
    parser.add_argument("--offline", type=Path, help="Offline GitHub API issue JSON for testing.")
    parser.add_argument("--output-dir", type=Path, default=Path("reports/starter_audit_bundle"))
    parser.add_argument("--min-score", type=int, default=60)
    parser.add_argument("--include-rejected", action="store_true", default=True)
    parser.add_argument("--exclude-rejected", action="store_true", help="Do not include rejected matches in outputs.")
    parser.add_argument("--enrich-repos", action="store_true", help="Fetch repository health signals for live config runs.")
    parser.add_argument("--dry-run", action="store_true", help="Print the bundle summary without writing files.")
    args = parser.parse_args()

    if bool(args.config) == bool(args.offline):
        parser.error("Pass exactly one of --config or --offline.")

    include_rejected = args.include_rejected and not args.exclude_rejected
    issue_scout = load_issue_scout()

    try:
        opportunities = (
            issue_scout.collect_offline(args.offline)
            if args.offline
            else issue_scout.collect_from_config(args.config, args.enrich_repos)
        )
        results = issue_scout.split_results(opportunities, args.min_score)
        source = "offline sample" if args.offline else str(args.config)
        output_dir = args.output_dir

        summary = build_summary(results, source, output_dir, include_rejected)
        if args.dry_run:
            print(summary)
            return 0
        write_text(output_dir / "audit_report.md", issue_scout.render_report(results, source, "markdown", include_rejected))
        write_text(output_dir / "audit_report.html", issue_scout.render_report(results, source, "html", include_rejected))
        write_text(output_dir / "opportunities.csv", issue_scout.render_report(results, source, "csv", include_rejected))
        write_text(output_dir / "opportunities.json", issue_scout.render_report(results, source, "json", include_rejected))
        write_text(output_dir / "summary.md", summary)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"Built Starter Audit bundle in {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
