# Starter Audit Delivery Bundle

This file describes the recommended bundle for a paid Starter Audit.

See `examples/starter_audit_bundle/` for a static sample bundle.

## Files To Deliver

1. `audit_report.md`
   - human-readable summary
   - top opportunities
   - top recommendation
   - rejected matches and reasons
   - next-step checklist

2. `opportunities.csv`
   - spreadsheet-friendly table
   - useful for sorting by score, task type, time, or risk

3. `opportunities.json`
   - automation-friendly export
   - useful for dashboards, follow-up scripts, or recurring reports

## Suggested Commands

```powershell
python scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --output reports\audit_report.md
python scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --format csv --output reports\opportunities.csv
python scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --format json --output reports\opportunities.json
```

Add `--enrich-repos` when live GitHub API access is stable and repository health signals are useful for the client.

Or build the full bundle in one command:

```powershell
python scripts\build_audit_bundle.py --config examples\queries.json --output-dir reports\starter_audit_bundle --min-score 60 --enrich-repos
```

Use `--dry-run` to validate the summary without writing files.

## Delivery Note

The audit is a decision-support artifact. It should help the client choose better GitHub work, not push them into low-quality PRs or risky bounty tasks.
