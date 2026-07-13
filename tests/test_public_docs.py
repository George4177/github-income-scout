"""Regression checks for machine-specific paths in public documentation."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_TEXT_SUFFIXES = {".html", ".json", ".md", ".txt", ".yaml", ".yml"}
IGNORED_PARTS = {".git", "dist", "__pycache__"}


class PublicDocumentationTests(unittest.TestCase):
    def test_public_text_does_not_expose_local_runtime_paths(self) -> None:
        forbidden = {
            "C:" + "\\Users\\77",
            "C:" + "/Users/77",
            "codex" + "-runtimes",
            "codex" + "-primary-runtime",
        }
        violations: list[str] = []

        for path in ROOT.rglob("*"):
            if (
                not path.is_file()
                or path.suffix.lower() not in PUBLIC_TEXT_SUFFIXES
                or any(part in IGNORED_PARTS for part in path.parts)
            ):
                continue
            content = path.read_text(encoding="utf-8", errors="replace")
            for marker in forbidden:
                if marker in content:
                    violations.append(f"{path.relative_to(ROOT)}: {marker}")

        self.assertEqual([], violations, "Local paths found:\n" + "\n".join(violations))


if __name__ == "__main__":
    unittest.main()
