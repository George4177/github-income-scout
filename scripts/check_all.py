#!/usr/bin/env python3
"""Run the local validation suite for GitHub Income Scout."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_example_bundle() -> bool:
    print("\n== example starter audit bundle ==")
    bundle = ROOT / "examples" / "starter_audit_bundle"
    required = {
        "summary.md": "Starter Audit Bundle Summary",
        "audit_report.md": "GitHub Opportunity Report",
        "audit_report.html": "GitHub Opportunity Report",
        "opportunities.csv": "repo_health",
        "opportunities.json": "\"accepted\"",
    }
    for filename, marker in required.items():
        path = bundle / filename
        if not path.exists():
            print(f"Missing example bundle file: {path}", file=sys.stderr)
            return False
        if marker not in path.read_text(encoding="utf-8"):
            print(f"Missing marker {marker!r} in {path}", file=sys.stderr)
            return False
    return True


def check_client_brief_example() -> bool:
    print("\n== client brief example ==")
    path = ROOT / "examples" / "sample_client_brief.md"
    required = [
        "Starter Audit Brief",
        "No income, bounty, merge, or sponsorship guarantees.",
        "Optional Follow-Up Service",
    ]
    if not path.exists():
        print(f"Missing client brief example: {path}", file=sys.stderr)
        return False
    content = path.read_text(encoding="utf-8")
    for marker in required:
        if marker not in content:
            print(f"Missing marker {marker!r} in {path}", file=sys.stderr)
            return False
    return True


def check_profile_publish_assets() -> bool:
    print("\n== profile publish assets ==")
    required = {
        ROOT / "profile" / "README.md": "Available for Fixed-Scope Work",
        ROOT / "profile" / "PUBLISH_PROFILE.md": "George4177/George4177/README.md",
        ROOT / "examples" / "starter_audit_case_study.md": "Starter Audit Case Study",
    }
    for path, marker in required.items():
        if not path.exists():
            print(f"Missing profile asset: {path}", file=sys.stderr)
            return False
        if marker not in path.read_text(encoding="utf-8"):
            print(f"Missing marker {marker!r} in {path}", file=sys.stderr)
            return False
    return True


def check_publish_scripts() -> bool:
    print("\n== publish scripts ==")
    required = {
        "publish_repo.ps1": [
            "GITHUB_TOKEN",
            "Ensure-GitHubRepository",
            "gh repo create",
            "Published repository:",
        ],
        "publish_profile_repo.ps1": [
            "profile/README.md",
            "publish_repo.ps1",
            "Update profile service README",
        ],
    }
    script_dir = ROOT / "scripts"
    for filename, markers in required.items():
        path = script_dir / filename
        if not path.exists():
            print(f"Missing publish script: {path}", file=sys.stderr)
            return False
        content = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in content:
                print(f"Missing marker {marker!r} in {path}", file=sys.stderr)
                return False
    return True


def check_outreach_templates() -> bool:
    print("\n== outreach templates ==")
    template_dir = ROOT / "templates" / "outreach"
    required = {
        "pinned_repo_copy.md": "GitHub Income Scout",
        "community_post.md": "does not promise income",
        "direct_message.md": "No pressure",
        "service_reply.md": "not to guarantee income",
        "README.md": "Do not mass-message maintainers",
    }
    for filename, marker in required.items():
        path = template_dir / filename
        if not path.exists():
            print(f"Missing outreach template: {path}", file=sys.stderr)
            return False
        if marker not in path.read_text(encoding="utf-8"):
            print(f"Missing marker {marker!r} in {path}", file=sys.stderr)
            return False
    return True


def run_step(name: str, args: list[str]) -> bool:
    print(f"\n== {name} ==")
    result = subprocess.run(args, cwd=ROOT, text=True)
    if result.returncode != 0:
        print(f"FAILED: {name}", file=sys.stderr)
        return False
    return True


def main() -> int:
    python = sys.executable
    steps = [
        ("unit tests", [python, "-m", "unittest", "discover", "-s", "tests"]),
        ("site checks", [python, "scripts/check_site.py"]),
        (
            "offline markdown report",
            [
                python,
                "scripts/issue_scout.py",
                "--offline",
                "examples/sample_issues.json",
                "--min-score",
                "60",
                "--include-rejected",
                "--output",
                "-",
            ],
        ),
        (
            "offline json report",
            [
                python,
                "scripts/issue_scout.py",
                "--offline",
                "examples/sample_issues.json",
                "--min-score",
                "60",
                "--include-rejected",
                "--format",
                "json",
                "--output",
                "-",
            ],
        ),
        (
            "starter audit bundle dry-run",
            [
                python,
                "scripts/build_audit_bundle.py",
                "--offline",
                "examples/sample_issues.json",
                "--min-score",
                "60",
                "--dry-run",
            ],
        ),
        (
            "client brief dry-run",
            [
                python,
                "scripts/build_client_brief.py",
                "--opportunities",
                "examples/starter_audit_bundle/opportunities.json",
                "--client-profile",
                "examples/client_profile.json",
                "--output",
                "-",
                "--max-items",
                "3",
            ],
        ),
    ]
    failed = [name for name, args in steps if not run_step(name, args)]
    if not check_example_bundle():
        failed.append("example starter audit bundle")
    if not check_client_brief_example():
        failed.append("client brief example")
    if not check_profile_publish_assets():
        failed.append("profile publish assets")
    if not check_publish_scripts():
        failed.append("publish scripts")
    if not check_outreach_templates():
        failed.append("outreach templates")
    if failed:
        print("\nFailed checks:")
        for name in failed:
            print(f"- {name}")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
