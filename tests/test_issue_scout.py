import importlib.util
import json
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "issue_scout.py"
SPEC = importlib.util.spec_from_file_location("issue_scout", MODULE_PATH)
issue_scout = importlib.util.module_from_spec(SPEC)
sys.modules["issue_scout"] = issue_scout
SPEC.loader.exec_module(issue_scout)


class IssueScoutTests(unittest.TestCase):
    def test_classification_does_not_treat_classification_as_ci(self):
        item = {
            "title": "Add classification helper",
            "html_url": "https://github.com/example/repo/issues/1",
            "repository_url": "https://api.github.com/repos/example/repo",
            "labels": [{"name": "help wanted"}],
            "comments": 0,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
            "body": "Support a classification model API.",
        }

        opportunity = issue_scout.score_issue(item)

        self.assertEqual(opportunity.task_type, "Open-source contribution")

    def test_small_tool_issue_is_scored_and_rendered(self):
        item = {
            "title": "[tool] seconds_to_hms",
            "html_url": "https://github.com/abduznik/bitbox/issues/99",
            "repository_url": "https://api.github.com/repos/abduznik/bitbox",
            "labels": [{"name": "help wanted"}, {"name": "good first issue"}],
            "comments": 0,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
            "body": "Converts seconds to h:mm:ss.",
        }

        opportunity = issue_scout.score_issue(item)
        report = issue_scout.render_markdown([opportunity], "test")

        self.assertEqual(opportunity.task_type, "Small tool")
        self.assertIn("abduznik/bitbox", report)
        self.assertIn("seconds_to_hms", report)

    def test_security_exploit_issue_is_rejected(self):
        item = {
            "title": "[BUG] HTTP Desync Attack Request Smuggling User Impersonation $100",
            "html_url": "https://github.com/example/repo/issues/2",
            "repository_url": "https://api.github.com/repos/example/repo",
            "labels": [{"name": "bounty"}, {"name": "security"}],
            "comments": 1,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
            "body": "Exploit request smuggling to demonstrate impersonation.",
        }

        opportunity = issue_scout.score_issue(item)

        self.assertTrue(opportunity.rejected)
        self.assertIn("security exploitation work", opportunity.rejection_reason)
        self.assertEqual(opportunity.worth_doing, "No, rejected by safety filter")

    def test_min_score_split_keeps_rejected_separate(self):
        low_score = {
            "title": "Unclear idea",
            "html_url": "https://github.com/example/repo/issues/3",
            "repository_url": "https://api.github.com/repos/example/repo",
            "labels": [],
            "comments": 0,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
            "body": "Needs discussion.",
        }
        good_tool = {
            "title": "[tool] slugify",
            "html_url": "https://github.com/example/repo/issues/4",
            "repository_url": "https://api.github.com/repos/example/repo",
            "labels": [{"name": "help wanted"}, {"name": "good first issue"}],
            "comments": 0,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
            "body": "Small Python automation tool.",
        }

        results = issue_scout.split_results(
            [issue_scout.score_issue(low_score), issue_scout.score_issue(good_tool)],
            min_score=60,
        )

        self.assertEqual([item.title for item in results.accepted], ["[tool] slugify"])
        self.assertEqual([item.title for item in results.rejected], ["Unclear idea"])

    def test_json_report_groups_accepted_and_rejected(self):
        accepted = issue_scout.score_issue(
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
        rejected = issue_scout.score_issue(
            {
                "title": "Exploit credential bypass",
                "html_url": "https://github.com/example/repo/issues/5",
                "repository_url": "https://api.github.com/repos/example/repo",
                "labels": [{"name": "bounty"}],
                "comments": 0,
                "created_at": "2026-01-01T00:00:00Z",
                "updated_at": "2026-01-01T00:00:00Z",
                "body": "Bypass credential checks.",
            }
        )

        report = issue_scout.render_report(
            issue_scout.ScoutResult(accepted=[accepted], rejected=[rejected]),
            "test",
            "json",
            include_rejected=True,
        )
        data = json.loads(report)

        self.assertEqual(data["accepted"][0]["title"], "[tool] slugify")
        self.assertEqual(data["rejected"][0]["title"], "Exploit credential bypass")

    def test_csv_report_contains_core_audit_fields(self):
        accepted = issue_scout.score_issue(
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

        report = issue_scout.render_report(
            issue_scout.ScoutResult(accepted=[accepted], rejected=[]),
            "test",
            "csv",
            include_rejected=False,
        )

        self.assertIn("score,repository,title,url,task_type", report)
        self.assertIn("[tool] slugify", report)

    def test_repo_health_enrichment_affects_score_and_output(self):
        item = {
            "title": "[tool] slugify",
            "html_url": "https://github.com/example/repo/issues/4",
            "repository_url": "https://api.github.com/repos/example/repo",
            "labels": [{"name": "help wanted"}, {"name": "good first issue"}],
            "comments": 0,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
            "body": "Small Python automation tool.",
        }
        repo = {
            "stargazers_count": 120,
            "forks_count": 12,
            "pushed_at": "2026-07-01T00:00:00Z",
            "archived": False,
            "disabled": False,
        }

        opportunity = issue_scout.score_issue(item, repo=repo)
        report = issue_scout.render_markdown([opportunity], "test")

        self.assertEqual(opportunity.repo_health, "active-looking")
        self.assertEqual(opportunity.repo_stars, 120)
        self.assertIn("Repository health: active-looking", report)

    def test_archived_repo_is_risky(self):
        item = {
            "title": "[tool] slugify",
            "html_url": "https://github.com/example/repo/issues/4",
            "repository_url": "https://api.github.com/repos/example/repo",
            "labels": [{"name": "help wanted"}, {"name": "good first issue"}],
            "comments": 0,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
            "body": "Small Python automation tool.",
        }
        repo = {
            "stargazers_count": 120,
            "forks_count": 12,
            "pushed_at": "2026-07-01T00:00:00Z",
            "archived": True,
            "disabled": False,
        }

        opportunity = issue_scout.score_issue(item, repo=repo)

        self.assertEqual(opportunity.repo_health, "avoid: archived or disabled")
        self.assertLess(opportunity.score, 60)


if __name__ == "__main__":
    unittest.main()
