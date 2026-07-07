#!/usr/bin/env python3
"""Lightweight checks for the static landing page."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


def require_file(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    try:
        html = require_file(SITE / "index.html")
        css = require_file(SITE / "styles.css")
        require_file(SITE / "README.md")
        require_file(ROOT / "README.md")
        require_file(ROOT / "SERVICE_MENU.md")
        weekly_workflow = require_file(ROOT / ".github" / "workflows" / "weekly-scout.yml")
        require_file(ROOT / "docs" / "weekly_scout_workflow.md")
        require_file(ROOT / "examples" / "sample_audit.md")
        require_file(ROOT / "examples" / "starter_audit_case_study.md")
        require_file(ROOT / "examples" / "profile_opportunity_pack_example.md")
        require_file(ROOT / "templates" / "profile_opportunity_pack_template.md")
        require_file(ROOT / "templates" / "profile_pack_delivery_checklist.md")

        for text in [
            "GitHub Income Scout",
            "Starter Audit",
            "SERVICE_MENU.md",
            "profile-opportunity-pack.yml",
            "profile_opportunity_pack_example.md",
            "Recent proof",
            "live_triage_2026-07-07.md",
            "No spam PRs",
            "scripts/issue_scout.py",
            "./styles.css",
            "Read case study",
        ]:
            if text not in html:
                raise AssertionError(f"Missing expected HTML text: {text}")

        for text in ["@media", ".hero", ".feature-grid", ".proof-grid", ".button.primary"]:
            if text not in css:
                raise AssertionError(f"Missing expected CSS text: {text}")

        for text in ["actions/upload-artifact@v4", "weekly-scout-reports", "opportunities.csv"]:
            if text not in weekly_workflow:
                raise AssertionError(f"Missing expected weekly workflow text: {text}")
    except AssertionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print("site checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
