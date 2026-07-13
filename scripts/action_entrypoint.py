#!/usr/bin/env python3
"""Validate GitHub Action inputs and invoke the opportunity scout."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Mapping


VALID_FORMATS = {"markdown", "json", "csv", "html"}
VALID_BOOLEANS = {"true": True, "false": False}


def parse_boolean(name: str, value: str) -> bool:
    normalized = value.strip().lower()
    if normalized not in VALID_BOOLEANS:
        raise ValueError(f"{name} must be 'true' or 'false', got {value!r}")
    return VALID_BOOLEANS[normalized]


def build_command(env: Mapping[str, str], python: str = sys.executable) -> tuple[list[str], str, str]:
    action_path = Path(env.get("GITHUB_ACTION_PATH", "")).resolve()
    scout = action_path / "scripts" / "issue_scout.py"
    if not scout.is_file():
        raise ValueError(f"issue_scout.py not found under GITHUB_ACTION_PATH: {action_path}")

    output = env.get("INPUT_OUTPUT", "github-income-scout-report.md").strip()
    if not output or output == "-":
        raise ValueError("output must be a file path; stdout output is not supported by this Action")
    if "\n" in output or "\r" in output:
        raise ValueError("output must be a single-line file path")

    report_format = env.get("INPUT_FORMAT", "markdown").strip().lower()
    if report_format not in VALID_FORMATS:
        raise ValueError(f"format must be one of {sorted(VALID_FORMATS)}, got {report_format!r}")

    min_score_text = env.get("INPUT_MIN_SCORE", "60").strip()
    try:
        min_score = int(min_score_text)
    except ValueError as exc:
        raise ValueError(f"min-score must be an integer, got {min_score_text!r}") from exc
    if not 0 <= min_score <= 100:
        raise ValueError("min-score must be between 0 and 100")

    include_rejected = parse_boolean("include-rejected", env.get("INPUT_INCLUDE_REJECTED", "true"))
    enrich_repos = parse_boolean("enrich-repos", env.get("INPUT_ENRICH_REPOS", "false"))

    offline = env.get("INPUT_OFFLINE", "").strip()
    config = env.get("INPUT_CONFIG", "").strip()
    command = [python, str(scout)]
    if offline:
        command.extend(["--offline", offline])
    else:
        command.extend(["--config", config or str(action_path / "examples" / "queries.json")])

    command.extend(["--min-score", str(min_score), "--format", report_format, "--output", output])
    if include_rejected:
        command.append("--include-rejected")
    if enrich_repos and not offline:
        command.append("--enrich-repos")
    return command, output, report_format


def write_action_outputs(path: str, report_path: str, report_format: str) -> None:
    if not path:
        return
    with Path(path).open("a", encoding="utf-8") as output_file:
        output_file.write(f"report-path={report_path}\n")
        output_file.write(f"report-format={report_format}\n")


def main() -> int:
    try:
        command, report_path, report_format = build_command(os.environ)
        result = subprocess.run(command, check=False)
        if result.returncode != 0:
            return result.returncode
        write_action_outputs(os.getenv("GITHUB_OUTPUT", ""), report_path, report_format)
        return 0
    except (OSError, ValueError) as exc:
        print(f"action input error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
