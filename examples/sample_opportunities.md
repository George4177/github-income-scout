# Sample Opportunities

Run:

```powershell
python scripts\issue_scout.py --offline examples\sample_issues.json --output reports\offline_check.md
```

Expected result:

- a Markdown report in `reports/offline_check.md`
- a ranked table of issue opportunities
- detailed risk and acceptance notes

To show rejected high-risk matches:

```powershell
python scripts\issue_scout.py --offline examples\sample_issues.json --min-score 60 --include-rejected --output -
```

To export client-friendly JSON or CSV:

```powershell
python scripts\issue_scout.py --offline examples\sample_issues.json --min-score 60 --include-rejected --format json --output -
python scripts\issue_scout.py --offline examples\sample_issues.json --min-score 60 --include-rejected --format csv --output -
```
