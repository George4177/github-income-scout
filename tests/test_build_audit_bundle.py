import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build_audit_bundle.py"
SPEC = importlib.util.spec_from_file_location("build_audit_bundle", MODULE_PATH)
build_audit_bundle = importlib.util.module_from_spec(SPEC)
sys.modules["build_audit_bundle"] = build_audit_bundle
SPEC.loader.exec_module(build_audit_bundle)


class BuildAuditBundleTests(unittest.TestCase):
    def test_build_summary_includes_top_actions_and_files(self):
        issue_scout = build_audit_bundle.load_issue_scout()
        opportunity = issue_scout.score_issue(
            {
                "title": "[tool] slugify",
                "html_url": "https://github.com/example/repo/issues/4",
                "repository_url": "https://api.github.com/repos/example/repo",
                "labels": [{"name": "help wanted"}, {"name": "good first issue"}],
                "comments": 0,
                "created_at": "2026-01-01T00:00:00Z",
                "updated_at": "2026-01-01T00:00:00Z",
                "body": "Small Python automation tool.",
            }
        )
        results = issue_scout.ScoutResult(accepted=[opportunity], rejected=[])

        summary = build_audit_bundle.build_summary(results, "test", Path("out"), include_rejected=True)

        self.assertIn("Starter Audit Bundle Summary", summary)
        self.assertIn("opportunities.csv", summary)
        self.assertIn("[tool] slugify", summary)

    def test_write_text_creates_parent_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "nested" / "file.txt"

            build_audit_bundle.write_text(path, "ok")

            self.assertEqual(path.read_text(encoding="utf-8"), "ok")


if __name__ == "__main__":
    unittest.main()

