# GitHub Income Scout

GitHub Income Scout helps independent developers find low-risk GitHub opportunities they can act on without spamming maintainers or chasing vague "make money online" ideas.

## Hire This as a Starter Audit

If you want this workflow applied to your own GitHub profile, the fixed-scope Starter Audit is the fastest entry point.

You provide your GitHub profile, preferred languages/tools, weekly time budget, and work boundaries. The deliverable is a short report with screened opportunities, top 3 recommended actions, risk notes, and one positioning suggestion.

Suggested first package: USD 29-49. Start from the [landing page](https://george4177.github.io/github-income-scout/), or see [SERVICE_MENU.md](SERVICE_MENU.md), [service_offer.md](service_offer.md), [pricing.md](pricing.md), and [examples/starter_audit_case_study.md](examples/starter_audit_case_study.md).

It searches public GitHub issues, scores them with conservative heuristics, and produces a Markdown report with:

- task type
- estimated difficulty
- estimated value
- likely time cost
- acceptance signals
- failure risks
- whether the issue is worth pursuing

The first target users are developers who can do Python automation, GitHub Actions, documentation fixes, CI cleanup, data scripts, README improvements, and small developer tools.

## What This Is Not

This tool does not automate pull requests, comments, account creation, bounty claims, scraping behind logins, fake engagement, exploit work, or platform rule bypasses. It is a research assistant for choosing better work.

## Quick Start

```powershell
cd path\to\github-income-scout
python scripts\issue_scout.py --config examples\queries.json --output reports\opportunities.md
```

Optional: set `GITHUB_TOKEN` to increase GitHub API rate limits. The tool works without a token for light use.

To include the safety-filter table and hide weak matches:

```powershell
python scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --output reports\opportunities.md
```

To add repository health signals such as stars, forks, last push date, and activity hints:

```powershell
python scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --enrich-repos --output reports\opportunities.md
```

Export JSON or CSV for spreadsheets, dashboards, or client delivery:

```powershell
python scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --format json --output reports\opportunities.json
python scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --format csv --output reports\opportunities.csv
```

Build a full Starter Audit delivery bundle:

```powershell
python scripts\build_audit_bundle.py --config examples\queries.json --output-dir reports\starter_audit_bundle --min-score 60 --enrich-repos
```

Build a client-ready Starter Audit brief from a generated JSON report:

```powershell
python scripts\build_client_brief.py --opportunities examples\starter_audit_bundle\opportunities.json --client-profile examples\client_profile.json --output reports\client_brief.md --max-items 3
```

```powershell
$env:GITHUB_TOKEN = "ghp_your_token_here"
```

Do not commit tokens or paste private credentials into issue reports.

## Use as a GitHub Action

The repository includes a zero-dependency Composite Action for generating a report inside another repository. It reads public issue data and does not create comments, claims, or pull requests.

```yaml
name: Weekly opportunity report

on:
  workflow_dispatch:
  schedule:
    - cron: "0 1 * * 1"

permissions:
  contents: read

jobs:
  scout:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - id: scout
        uses: George4177/github-income-scout@v0.3.0
        with:
          token: ${{ github.token }}
          min-score: "60"
          include-rejected: "true"
          output: reports/github-opportunities.md
      - uses: actions/upload-artifact@v7
        with:
          name: github-opportunity-report
          path: ${{ steps.scout.outputs.report-path }}
```

Use `config` for a repository-specific query file, `format` for `markdown`, `json`, or `csv`, and `enrich-repos: "true"` when repository health metadata is worth the additional API calls. The optional `offline-input` supports deterministic tests without network access.

See [MARKETPLACE.md](MARKETPLACE.md) for the verified release status and the account-owner step required for a Marketplace listing.

## Weekly Scout Workflow

The repository includes a scheduled GitHub Actions workflow that generates Markdown, JSON, CSV, and Starter Audit bundle artifacts.

See [docs/weekly_scout_workflow.md](docs/weekly_scout_workflow.md) for how to run it and download the reports.

## Codex Skill

The repository includes an installable `github-income-scout` Codex skill in
[`codex-skills/github-income-scout`](codex-skills/github-income-scout). It can
screen GitHub issues, reject unsafe or already-claimed work, and package a
Starter Audit or pull-request action pack.

Install it from this public repository:

```powershell
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" `
  --repo George4177/github-income-scout `
  --path codex-skills/github-income-scout
```

Restart Codex after installation, then invoke it with:

```text
Use $github-income-scout to screen current Python and GitHub Actions issues for a 3-hour weekly budget.
```

Validate a local checkout with the Skill Creator validator:

```powershell
python "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" `
  codex-skills/github-income-scout
```

## Example Output

See [examples/sample_opportunities.md](examples/sample_opportunities.md).

## Free Version

The free version includes:

- configurable GitHub issue queries
- conservative scoring
- safety filtering for exploit, fake-engagement, credential, bypass, automated bounty-feed, dependency-dashboard, and generic vulnerability work
- Markdown report output
- JSON and CSV export
- optional repository health signals
- no external services
- no account writes
- reusable Composite Action with a deterministic offline smoke test

## Paid Customization Ideas

These are service ideas, not guaranteed earnings:

- one-time GitHub opportunity audit for a developer profile
- custom query packs for Python, CI/CD, docs, data analysis, or creator automation
- GitHub profile and README positioning package
- weekly opportunity report for a small team
- private deployment with saved filters and local history

See [pricing.md](pricing.md) for professional, non-hype packaging.

See [SERVICE_MENU.md](SERVICE_MENU.md) for a public service menu that can be shared directly with potential clients.

## Validation

Run the smoke test:

```powershell
python scripts\issue_scout.py --offline examples\sample_issues.json --output reports\offline_check.md
```

The command should create `reports/offline_check.md` and include scored opportunities.

In restricted environments or CI logs, print the report instead of writing a file:

```powershell
python scripts\issue_scout.py --offline examples\sample_issues.json --output -
```

Run the zero-dependency unit tests:

```powershell
python -m unittest discover -s tests
```

Run the full local validation suite:

```powershell
python scripts\check_all.py
```

## Example Service Package

The repository includes a sample client-facing audit in [examples/sample_audit.md](examples/sample_audit.md). It shows how the free tool can support a paid Starter Audit without promising income or submitting low-quality pull requests.

It also includes [examples/sample_client_brief.md](examples/sample_client_brief.md), a short client-ready brief generated from opportunity JSON and a client profile.

For a clearer sales example, see [examples/starter_audit_case_study.md](examples/starter_audit_case_study.md). It explains the client input, screening process, rejected-match logic, deliverables, and follow-up offer.

For the mid-tier service format, see [examples/profile_opportunity_pack_example.md](examples/profile_opportunity_pack_example.md), [templates/profile_opportunity_pack_template.md](templates/profile_opportunity_pack_template.md), and [templates/profile_pack_delivery_checklist.md](templates/profile_pack_delivery_checklist.md).

## Launch Assets

The repository includes public-launch assets so the MVP can be published quickly:

- [RELEASE_NOTES.md](RELEASE_NOTES.md): v0.1.0 release body and launch copy
- [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md): first-week publishing and revenue checklist
- [PUBLISHING.md](PUBLISHING.md): repository setup steps
- [templates/outreach/launch_sequence.md](templates/outreach/launch_sequence.md): cautious first-launch outreach drafts
- [docs/weekly_scout_workflow.md](docs/weekly_scout_workflow.md): scheduled report workflow guide
- [scripts/create_release_bundle.ps1](scripts/create_release_bundle.ps1): local ZIP bundle helper for `v0.1.0`
- [scripts/publish_repo.ps1](scripts/publish_repo.ps1): publish helper for `gh` or `GITHUB_TOKEN` environments
- [scripts/publish_profile_repo.ps1](scripts/publish_profile_repo.ps1): publishes the prepared GitHub Profile README repository

## Lead Capture

The repository includes GitHub issue forms for:

- Starter Audit requests
- Profile + Opportunity Pack requests
- Custom Automation requests

Direct request links:

- [Starter Audit request](https://github.com/George4177/github-income-scout/issues/new?template=starter-audit.yml)
- [Profile + Opportunity Pack request](https://github.com/George4177/github-income-scout/issues/new?template=profile-opportunity-pack.yml)
- [Custom Automation request](https://github.com/George4177/github-income-scout/issues/new?template=custom-automation.yml)

These forms are intentionally scoped to avoid secrets, credentials, fake engagement, exploit work, and platform bypasses.

The `templates/outreach/` folder includes low-pressure publishing and reply drafts for GitHub profile placement, community posts, direct messages, and Starter Audit inquiries.

## Release Bundle

Create a local release ZIP:

```powershell
.\scripts\create_release_bundle.ps1 -Version v0.1.0
```

The generated `dist/` folder is intentionally ignored by Git.

## Static Site

The published landing page is available at <https://george4177.github.io/github-income-scout/>.

The `site/` folder contains the no-build landing page for GitHub Pages. It presents the tool, Starter Audit service, boundaries, direct request links, and example commands.

The included `Deploy GitHub Pages` workflow publishes the `site/` folder when GitHub Pages is configured to use GitHub Actions.

## Current Release

- [v0.2.0 - Installable Codex Skill](https://github.com/George4177/github-income-scout/releases/tag/v0.2.0)
- [v0.2.0 Release ZIP](https://github.com/George4177/github-income-scout/releases/download/v0.2.0/github-income-scout-v0.2.0.zip)
- [v0.1.0 - Starter Audit MVP](https://github.com/George4177/github-income-scout/releases/tag/v0.1.0)
- [Release ZIP](https://github.com/George4177/github-income-scout/releases/download/v0.1.0/github-income-scout-v0.1.0.zip)
