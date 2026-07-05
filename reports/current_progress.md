# Current Progress Report

Date: 2026-07-05

## Routes Chosen

1. Build a reusable GitHub opportunity scouting tool that can become a service-ready repository.
2. Use the tool to identify one low-risk open-source PR candidate after review and user confirmation.
3. Package the result with README, pricing, and service copy so it can support GitHub profile positioning.

## Opportunities Found

- Own MVP: GitHub Income Scout, a local tool and service package for finding low-risk GitHub issue opportunities.
- Algora UI bug: unauthorized edit/delete controls visible on bounty listings. Possible portfolio PR, uncertain direct payout.
- Algora auth redirect bug: successful GitHub login redirects to `/home` 404. Higher setup risk due OAuth reproduction.
- Bitbox `seconds_to_hms`: small Python tool contribution. Low effort, no verified payout, useful as a clean PR candidate.
- PyFenn SingleLayerPerceptron: larger Python ML API enhancement. Good portfolio value, too large for first monetization step.
- OpenOperator Action Memory Summarizer: live query candidate, likely broader LLM integration scope, not first.
- Rejected current bounty-search results involving security exploitation or fake-engagement/onboarding tasks.

## Files Completed

- `README.md`: installation, validation, free/paid positioning
- `scripts/issue_scout.py`: configurable GitHub issue scanner with scoring, safety filtering, optional repository health enrichment, `--min-score`, `--include-rejected`, and Markdown/JSON/CSV export
- `examples/queries.json`: default query pack
- `examples/live_quick.json`: small live-query config
- `examples/sample_issues.json`: offline validation data
- `examples/sample_opportunities.md`: sample usage note
- `examples/delivery_bundle.md`: recommended Markdown/CSV/JSON Starter Audit delivery bundle
- `.github/ISSUE_TEMPLATE/starter-audit.yml`: GitHub issue form for Starter Audit requests
- `.github/ISSUE_TEMPLATE/custom-automation.yml`: GitHub issue form for scoped automation requests
- `profile/README.md`: GitHub profile README package
- `profile/SERVICES.md`: profile services page
- `scripts/publish_repo.ps1`: helper to publish the repo when `git` and `gh` are available
- `scripts/prepare_bitbox_pr.ps1`: helper to fork Bitbox, add the tool, test, push, and open PR when `git` and `gh` are available
- `codex-skills/github-income-scout/SKILL.md`: reusable Codex skill draft for GitHub opportunity scouting
- `codex-skills/github-income-scout/agents/openai.yaml`: UI metadata for the skill draft
- `codex-skills/github-income-scout/references/workflow.md`: skill workflow reference
- `site/index.html`: static landing page for GitHub Pages
- `site/styles.css`: responsive landing page styling
- `site/README.md`: GitHub Pages setup notes
- `scripts/check_site.py`: static site smoke test
- `scripts/build_audit_bundle.py`: one-command Starter Audit bundle builder for Markdown, CSV, JSON, and summary
- `scripts/check_all.py`: one-command local validation suite
- `examples/starter_audit_bundle/summary.md`: static sample bundle summary
- `examples/starter_audit_bundle/audit_report.md`: static sample client report
- `examples/starter_audit_bundle/opportunities.csv`: static sample spreadsheet export
- `examples/starter_audit_bundle/opportunities.json`: static sample automation export
- `.github/workflows/pages.yml`: GitHub Pages deployment workflow for the static landing page
- `pricing.md`: professional service packaging
- `roadmap.md`: MVP and next steps
- `service_offer.md`: client-facing service description
- `.github/workflows/weekly-scout.yml`: scheduled GitHub Actions report workflow
- `PUBLISHING.md`: repository publishing checklist
- `LICENSE`: MIT license
- `pyproject.toml`: Python project metadata
- `examples/sample_audit.md`: example paid Starter Audit deliverable
- `reports/opportunity_list.md`: initial money opportunity list
- `reports/bitbox_pr_precheck.md`: Bitbox contribution precheck
- `reports/bitbox_external_action_pack.md`: Bitbox issue claim, implementation, test, commit, and PR drafts
- `reports/live_snapshot_2026-07-05.md`: real GitHub query output captured from the tool
- `reports/github_profile_readme_draft.md`: GitHub profile README draft
- `templates/client_intake.md`: client intake form for paid Starter Audit
- `templates/delivery_checklist.md`: delivery checklist and quality bar
- `templates/github_repo_description.md`: copy for publishing/pinning the repository
- `templates/starter_audit_report_template.md`: reusable paid audit report template
- `templates/outreach/README.md`: outreach guardrails
- `templates/outreach/pinned_repo_copy.md`: pinned repository/profile copy
- `templates/outreach/community_post.md`: community post drafts
- `templates/outreach/direct_message.md`: low-pressure direct-message drafts
- `templates/outreach/service_reply.md`: Starter Audit inquiry reply template
- `reports/current_progress.md`: this progress report

## Validation Status

- Offline read path works.
- Script now supports `--output -` so it can be validated in restricted environments and used in GitHub Actions.
- Standard-library unit tests pass with `python -m unittest discover -s tests` with 8 tests.
- Optional repository health enrichment is covered by tests and offline sample data.
- Safety filter tests pass and reject exploit/fake-engagement examples.
- Offline safety-filter report passes with `--min-score 60 --include-rejected`.
- JSON and CSV exports validate on offline sample data.
- PowerShell helper scripts parse successfully.
- Codex skill draft was created; `quick_validate.py` could not complete because the current bundled Python environment lacks the `yaml` module.
- Static site smoke test passes with `python scripts/check_site.py`.
- GitHub Pages workflow file exists and publishes the `site/` folder through GitHub Actions.
- Starter Audit bundle dry-run passes and is included in the weekly workflow.
- Full validation suite passes with `python scripts/check_all.py`.
- Static sample Starter Audit bundle is checked by `check_all.py`.
- Outreach templates are checked by `check_all.py` for non-hype, low-risk boundary language.
- Local file generation through normal shell/Python is blocked by the current desktop sandbox, but the script code includes normal file output for user environments.
- Live GitHub API calls were intermittently available; initial issue data was retrieved, later calls timed out.
- A 5-hour heartbeat automation was created to continue this same thread once the current work window ends.
- Bitbox #99 was rechecked live: open, unassigned, 0 comments, and no open PR named `seconds_to_hms`.
- Real live-query report generated from `examples/live_quick.json` and saved as `reports/live_snapshot_2026-07-05.md`.
- Live quick query still runs after adding safety-filter flags; latest run returned PyFenn, Bitbox, and OpenOperator.
- Live quick query also validates with JSON export.
- Latest live quick query attempt timed out with WinError 10060; previous live runs succeeded, so this is currently treated as network instability rather than a script failure.
- Local Git initialization is blocked by the current environment's `.git` write restriction, so publishing remains a user-confirmed next step.
- GitHub CLI is not installed in this environment, so the logged-in GitHub username could not be read from `gh`; Bitbox PR author header still needs confirmation before external PR work.
- GitHub connector attempted to comment on `abduznik/bitbox#99` but GitHub returned 403 `Resource not accessible by integration`; external comment/PR still needs browser, `gh`, or a connector with broader write access.
- GitHub connector currently returns no installed repositories for publishing targets.

## PR Status

- No external comments, PRs, bounty claims, or account-bound actions have been made.
- Next external candidate: `abduznik/bitbox#99`; contribution guide and open PR state have been checked, and the external action pack plus `prepare_bitbox_pr.ps1` helper are ready.

## Most Likely Income Action

The fastest income path is to publish/polish GitHub Income Scout as a portfolio repo and offer a small "Starter Audit" service at USD 29-49. This is more controllable than waiting for bounty approval and can directly target developers who want contribution opportunities.

## Next Confirmation Needed

Authorized next external moves when tool access allows:

1. Publish `github-income-scout` as a new GitHub repository.
2. Comment on `abduznik/bitbox#99` to claim the `seconds_to_hms` issue.
3. Open a draft PR for Bitbox after creating the tool file with the correct GitHub username in the header.

## Gap to Covering Membership Cost

The project still needs:

- a public GitHub repository or profile placement
- outreach channel or marketplace listing
- optionally one small accepted PR to increase credibility
- tool access that can create repositories or write to external GitHub issues/PRs, such as local `gh` login or broader GitHub connector installation
