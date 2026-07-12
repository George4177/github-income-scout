import importlib.util
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "action_entrypoint.py"
SPEC = importlib.util.spec_from_file_location("action_entrypoint", MODULE_PATH)
action_entrypoint = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(action_entrypoint)


class ActionEntrypointTests(unittest.TestCase):
    def test_default_command_uses_bundled_config(self):
        command, output, report_format = action_entrypoint.build_command({"GITHUB_ACTION_PATH": str(ROOT)})

        self.assertIn(str(ROOT / "examples" / "queries.json"), command)
        self.assertIn("--include-rejected", command)
        self.assertNotIn("--enrich-repos", command)
        self.assertEqual(output, "github-income-scout-report.md")
        self.assertEqual(report_format, "markdown")

    def test_offline_input_disables_repo_enrichment(self):
        command, _, _ = action_entrypoint.build_command(
            {
                "GITHUB_ACTION_PATH": str(ROOT),
                "INPUT_OFFLINE": "issues.json",
                "INPUT_ENRICH_REPOS": "true",
            }
        )

        self.assertIn("--offline", command)
        self.assertNotIn("--config", command)
        self.assertNotIn("--enrich-repos", command)

    def test_invalid_inputs_fail_before_execution(self):
        with self.assertRaisesRegex(ValueError, "between 0 and 100"):
            action_entrypoint.build_command(
                {"GITHUB_ACTION_PATH": str(ROOT), "INPUT_MIN_SCORE": "101"}
            )
        with self.assertRaisesRegex(ValueError, "include-rejected"):
            action_entrypoint.build_command(
                {"GITHUB_ACTION_PATH": str(ROOT), "INPUT_INCLUDE_REJECTED": "yes"}
            )
        with self.assertRaisesRegex(ValueError, "single-line"):
            action_entrypoint.build_command(
                {"GITHUB_ACTION_PATH": str(ROOT), "INPUT_OUTPUT": "report.md\nunsafe=true"}
            )

    def test_entrypoint_generates_report_and_outputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            report = temp / "report.md"
            outputs = temp / "github-output.txt"
            env = os.environ.copy()
            env.update(
                {
                    "GITHUB_ACTION_PATH": str(ROOT),
                    "GITHUB_OUTPUT": str(outputs),
                    "INPUT_OFFLINE": str(ROOT / "examples" / "sample_issues.json"),
                    "INPUT_MIN_SCORE": "60",
                    "INPUT_FORMAT": "markdown",
                    "INPUT_OUTPUT": str(report),
                    "INPUT_INCLUDE_REJECTED": "true",
                    "INPUT_ENRICH_REPOS": "false",
                }
            )

            result = subprocess.run([sys.executable, str(MODULE_PATH)], env=env, text=True, capture_output=True)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("GitHub Opportunity Report", report.read_text(encoding="utf-8"))
            output_text = outputs.read_text(encoding="utf-8")
            self.assertIn(f"report-path={report}", output_text)
            self.assertIn("report-format=markdown", output_text)

    def test_action_manifest_exposes_contract(self):
        manifest = (ROOT / "action.yml").read_text(encoding="utf-8")
        for marker in (
            "using: composite",
            "offline-input:",
            "report-path:",
            "scripts/action_entrypoint.py",
            "GITHUB_TOKEN: ${{ inputs.token }}",
        ):
            self.assertIn(marker, manifest)

        unsafe_descriptions = re.findall(r'^\s*description:\s+[^"\'].*:\s', manifest, re.MULTILINE)
        self.assertEqual(unsafe_descriptions, [])


if __name__ == "__main__":
    unittest.main()
