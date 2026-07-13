# Weekly Scout Workflow

The repository includes a GitHub Actions workflow that can run GitHub Income Scout on a schedule or on demand.

Workflow file: `.github/workflows/weekly-scout.yml`

## What It Produces

Each run creates a `weekly-scout-reports` artifact with:

- `opportunity-report.md`
- `opportunities.json`
- `opportunities.csv`
- `opportunities.html`
- `starter-audit-bundle/summary.md`
- `starter-audit-bundle/audit_report.md`
- `starter-audit-bundle/opportunities.json`
- `starter-audit-bundle/opportunities.csv`

These files are intended for review and manual triage. They are not instructions to spam maintainers or claim issues without reading the repository first.

## How To Run It

1. Open the repository on GitHub.
2. Go to **Actions**.
3. Select **Weekly GitHub Opportunity Scout**.
4. Click **Run workflow**.
5. Download the `weekly-scout-reports` artifact after the run completes.

The workflow also runs weekly on Monday at 01:00 UTC.

## Configuration

Edit `examples/queries.json` to change the search queries.

Recommended first query areas:

- Python automation
- GitHub Actions and CI cleanup
- documentation and README fixes
- small developer tools
- data/report scripts

## Token Use

The workflow uses GitHub's default `GITHUB_TOKEN` to increase API rate limits for public search and repository metadata requests.

Do not add personal access tokens, payment details, private credentials, or client secrets to this workflow.

## Safety Rules

Before acting on an opportunity:

- Open the issue and README.
- Check assignment and duplicate PRs.
- Read the contribution guide.
- Confirm the test or validation path.
- Avoid exploit work, fake engagement, credential handling, scraping behind logins, and platform-rule bypasses.
- Do not comment or open a PR until the scope is clear.

## Service Use

This workflow supports the free version of GitHub Income Scout and can also seed a paid Starter Audit or Profile + Opportunity Pack.

It does not guarantee income, bounty awards, sponsorship, merged pull requests, stars, or maintainer responses.
