import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build_client_brief.py"
SPEC = importlib.util.spec_from_file_location("build_client_brief", MODULE_PATH)
build_client_brief = importlib.util.module_from_spec(SPEC)
sys.modules["build_client_brief"] = build_client_brief
SPEC.loader.exec_module(build_client_brief)


class BuildClientBriefTests(unittest.TestCase):
    def test_render_brief_includes_boundaries_and_top_opportunity(self):
        profile = {
            "client_name": "Test client",
            "skills": ["Python", "docs"],
            "weekly_hours": "2",
            "preferred_tasks": ["documentation"],
            "avoid": ["security exploit work"],
            "budget_note": "USD 29 starter audit",
        }
        opportunities = [
            {
                "score": 75,
                "repository": "example/repo",
                "title": "Improve README",
                "url": "https://github.com/example/repo/issues/1",
                "task_type": "Documentation",
                "difficulty": "Low",
                "estimated_time": "1-2 hours",
                "worth_doing": "Yes",
                "acceptance": "Docs explain setup clearly",
                "risk": "Maintainer inactivity",
            }
        ]

        brief = build_client_brief.render_brief(profile, opportunities, 3)

        self.assertIn("Starter Audit Brief: Test client", brief)
        self.assertIn("example/repo: Improve README", brief)
        self.assertIn("No income, bounty, merge, or sponsorship guarantees.", brief)

    def test_normalize_accepts_issue_scout_json_shape(self):
        data = {"accepted": [{"title": "one"}], "rejected": [{"title": "two"}]}

        opportunities = build_client_brief.normalize_opportunities(data)

        self.assertEqual(opportunities, [{"title": "one"}])

    def test_render_opportunity_uses_task_specific_defaults(self):
        lines = build_client_brief.render_opportunity(
            1,
            {
                "repository": "example/docs",
                "title": "Document setup",
                "task_type": "Documentation",
            },
        )
        content = "\n".join(lines)

        self.assertIn("low-risk", content)
        self.assertIn("Docs clearly cover", content)

    def test_main_writes_output_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            opportunities = temp_path / "opportunities.json"
            profile = temp_path / "profile.json"
            output = temp_path / "brief.md"
            opportunities.write_text(json.dumps({"accepted": [{"score": 1, "title": "Task"}]}), encoding="utf-8")
            profile.write_text(json.dumps({"client_name": "Client"}), encoding="utf-8")

            exit_code = None
            argv_backup = sys.argv
            try:
                sys.argv = [
                    "build_client_brief.py",
                    "--opportunities",
                    str(opportunities),
                    "--client-profile",
                    str(profile),
                    "--output",
                    str(output),
                ]
                exit_code = build_client_brief.main()
            finally:
                sys.argv = argv_backup

            self.assertEqual(exit_code, 0)
            self.assertIn("Starter Audit Brief: Client", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
