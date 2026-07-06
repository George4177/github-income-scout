# GitHub Income Scout

GitHub Income Scout helps independent developers find low-risk GitHub opportunities they can act on without spamming maintainers or chasing vague "make money online" ideas.

## Hire This as a Starter Audit

If you want this workflow applied to your own GitHub profile, the fixed-scope Starter Audit is the fastest entry point.

You provide your GitHub profile, preferred languages/tools, weekly time budget, and work boundaries. The deliverable is a short report with screened opportunities, top 3 recommended actions, risk notes, and one positioning suggestion.

Suggested first package: USD 29-49. Start from the [landing page](https://george4177.github.io/github-income-scout/), or see [service_offer.md](service_offer.md), [pricing.md](pricing.md), and [examples/starter_audit_case_study.md](examples/starter_audit_case_study.md).

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
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\issue_scout.py --config examples\queries.json --output reports\opportunities.md
```

Optional: set `GITHUB_TOKEN` to increase GitHub API rate limits. The tool works without a token for light use.

To include the safety-filter table and hide weak matches:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --output reports\opportunities.md
```

To add repository health signals such as stars, forks, last push date, and activity hints:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --enrich-repos --output reports\opportunities.md
```

Export JSON or CSV for spreadsheets, dashboards, or client delivery:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --format json --output reports\opportunities.json
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\issue_scout.py --config examples\queries.json --min-score 60 --include-rejected --format csv --output reports\opportunities.csv
```

Build a full Starter Audit delivery bundle:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\build_audit_bundle.py --config examples\queries.json --output-dir reports\starter_audit_bundle --min-score 60 --enrich-repos
```

Build a client-ready Starter Audit brief from a generated JSON report:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\build_client_brief.py --opportunities examples\starter_audit_bundle\opportunities.json --client-profile examples\client_profile.json --output reports\client_brief.md --max-items 3
```

```powershell
$env:GITHUB_TOKEN = "ghp_your_token_here"
```

Do not commit tokens or paste private credentials into issue reports.

## Example Output

See [examples/sample_opportunities.md](examples/sample_opportunities.md).

## Free Version

The free version includes:

- configurable GitHub issue queries
- conservative scoring
- safety filtering for exploit, fake-engagement, credential, and bypass work
- Markdown report output
- JSON and CSV export
- optional repository health signals
- no external services
- no account writes

## Paid Customization Ideas

These are service ideas, not guaranteed earnings:

- one-time GitHub opportunity audit for a developer profile
- custom query packs for Python, CI/CD, docs, data analysis, or creator automation
- GitHub profile and README positioning package
- weekly opportunity report for a small team
- private deployment with saved filters and local history

See [pricing.md](pricing.md) for professional, non-hype packaging.

## Validation

Run the smoke test:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\issue_scout.py --offline examples\sample_issues.json --output reports\offline_check.md
```

The command should create `reports/offline_check.md` and include scored opportunities.

In restricted environments or CI logs, print the report instead of writing a file:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\issue_scout.py --offline examples\sample_issues.json --output -
```

Run the zero-dependency unit tests:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m unittest discover -s tests
```

Run the full local validation suite:

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\check_all.py
```

## Example Service Package

The repository includes a sample client-facing audit in [examples/sample_audit.md](examples/sample_audit.md). It shows how the free tool can support a paid Starter Audit without promising income or submitting low-quality pull requests.

It also includes [examples/sample_client_brief.md](examples/sample_client_brief.md), a short client-ready brief generated from opportunity JSON and a client profile.

For a clearer sales example, see [examples/starter_audit_case_study.md](examples/starter_audit_case_study.md). It explains the client input, screening process, rejected-match logic, deliverables, and follow-up offer.

## Launch Assets

The repository includes public-launch assets so the MVP can be published quickly:

- [RELEASE_NOTES.md](RELEASE_NOTES.md): v0.1.0 release body and launch copy
- [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md): first-week publishing and revenue checklist
- [PUBLISHING.md](PUBLISHING.md): repository setup steps
- [templates/outreach/launch_sequence.md](templates/outreach/launch_sequence.md): cautious first-launch outreach drafts
- [scripts/create_release_bundle.ps1](scripts/create_release_bundle.ps1): local ZIP bundle helper for `v0.1.0`
- [scripts/publish_repo.ps1](scripts/publish_repo.ps1): publish helper for `gh` or `GITHUB_TOKEN` environments
- [scripts/publish_profile_repo.ps1](scripts/publish_profile_repo.ps1): publishes the prepared GitHub Profile README repository

## Lead Capture

The repository includes GitHub issue forms for:

- Starter Audit requests
- Custom Automation requests

Direct request links:

- [Starter Audit request](https://github.com/George4177/github-income-scout/issues/new?template=starter-audit.yml)
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

- [v0.1.0 - Starter Audit MVP](https://github.com/George4177/github-income-scout/releases/tag/v0.1.0)
- [Release ZIP](https://github.com/George4177/github-income-scout/releases/download/v0.1.0/github-income-scout-v0.1.0.zip)
