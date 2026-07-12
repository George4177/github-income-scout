# Release Notes

## v0.3.0 - Reusable GitHub Action

GitHub Income Scout v0.3.0 adds an installable Composite Action so a repository can generate conservative opportunity reports without copying the scanner scripts.

### Added

- root `action.yml` with Markdown, JSON, and CSV report inputs
- bundled-query, custom-query, and deterministic offline modes
- report path and format outputs for artifact upload steps
- input validation and focused error messages in `scripts/action_entrypoint.py`
- deterministic GitHub Actions smoke workflow

### Improved

- safety filtering rejects automated bounty feeds, dependency dashboards, generic vulnerability trackers, and engagement-gated bounty claims
- XP-only contest tasks are downgraded instead of presented as direct-income opportunities
- the public opportunity list records manual duplicate, assignment, acceptance, and payout checks

### Validation

- 25 zero-dependency unit tests pass
- the Composite Action entrypoint generates a report and writes valid Action outputs
- the offline Action smoke workflow verifies the published interface
- the full local validation suite passes

This release does not guarantee income, bounty payouts, merged pull requests, sponsorships, or client leads. The Action does not post comments, claim work, open pull requests, collect credentials, or perform payment operations.

## v0.2.0 - Installable Codex Skill

GitHub Income Scout v0.2.0 packages the opportunity-screening workflow as an
installable Codex skill and strengthens the public evidence behind the fixed-scope
Starter Audit service.

### Added

- installable `github-income-scout` Codex skill with UI metadata
- standalone GitHub CLI commands for issue search, assignment checks, repository
  health review, and duplicate pull-request checks
- Profile + Opportunity Pack request form, delivery template, example, and checklist
- weekly GitHub Action artifacts in Markdown, JSON, CSV, and Starter Audit formats
- three accepted open-source contribution case studies plus an active Kubeflow MCP
  Server documentation contribution

### Improved

- opportunity scoring records assignees and downgrades contested issues
- public service menu now covers Starter Audit, Profile + Opportunity Pack, and
  Custom Automation requests
- landing page presents current verification evidence and direct request links
- release bundle includes service and workflow documentation

### Validation

- 16 unit tests pass
- static site checks pass
- offline Markdown, JSON, CSV, bundle, and client-brief dry runs pass
- the bundled Codex skill passes Skill Creator `quick_validate.py`

This release does not guarantee income, bounty payouts, merged pull requests,
sponsorships, or client leads. It does not automate payment, bounty claims,
maintainer messages, exploit work, credentials, fake engagement, or platform bypasses.

## v0.1.0 - Starter Audit MVP

GitHub Income Scout v0.1.0 is the first public-ready MVP for finding low-risk GitHub contribution opportunities and packaging them into a small paid audit service.

### Included

- GitHub issue search from configurable query packs
- Offline sample mode for testing without network access
- Conservative opportunity scoring
- Safety filters for exploit work, fake engagement, credential collection, bypass work, and spammy tasks
- Markdown, JSON, and CSV exports
- Optional repository health enrichment
- Starter Audit bundle generator
- Static GitHub Pages landing page
- GitHub issue forms for Starter Audit and Custom Automation requests
- Outreach templates and profile copy
- Unit tests and a one-command local validation script

### Intended Users

- independent developers looking for practical open-source contribution leads
- consultants packaging a small GitHub opportunity audit
- teams that want a low-risk weekly issue shortlist
- Codex users who want reusable GitHub workflow assets

### Boundaries

This release does not automate comments, pull requests, bounty applications, payment collection, account creation, fake engagement, exploit work, or platform bypasses.

### Validation

Run:

```powershell
python scripts\check_all.py
```

Expected result: unit tests pass, the static site check passes, reports render, the Starter Audit bundle dry run succeeds, and outreach templates pass the boundary checks.

### Suggested Launch Copy

Short repository description:

```text
Find and score low-risk GitHub issue opportunities for practical open-source contribution.
```

Release summary:

```text
First public MVP: configurable GitHub issue scouting, conservative safety filters, Markdown/JSON/CSV exports, a Starter Audit bundle generator, GitHub Pages landing page, and service-ready templates.
```

### Next Release Candidates

- saved scan history
- query packs by niche
- better duplicate PR detection
- HTML report export
- profile-specific scoring presets
- hosted private dashboard for recurring clients
