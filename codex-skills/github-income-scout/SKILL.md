---
name: github-income-scout
description: Find, filter, and package low-risk GitHub income opportunities. Use when Codex should scan GitHub issues for practical Python, automation, GitHub Actions, documentation, CI/CD, README, data-reporting, or small-tool opportunities; reject unsafe bounty work; generate Starter Audit deliverables; or prepare low-risk open-source PR action packs.
---

# GitHub Income Scout

Use this skill to turn GitHub issue research into concrete, low-risk income-oriented artifacts.

## Workflow

1. Define the target profile: skills, preferred task types, time available, and strict avoid list.
2. Run or adapt the `github-income-scout` project script when available:
   - Markdown report for human review
   - CSV export for spreadsheet triage
   - JSON export for dashboards or follow-up automation
   If the project script is unavailable, use the GitHub CLI queries in
   `references/commands.md` and perform the same manual checks.
3. Reject unsafe matches:
   - exploit or vulnerability abuse
   - fake stars, fake reviews, or spam engagement
   - credential handling
   - scraping behind logins
   - payment or platform bypasses
4. For the top 1-3 candidates, read the issue, README, contribution guide, and test instructions before recommending work.
5. Create concrete deliverables:
   - opportunity list
   - Starter Audit report
   - PR precheck
   - claim comment draft
   - branch name, commit message, PR title/body
   - service positioning notes

## Boundaries

Do not submit low-quality PRs, spam maintainers, bypass platform rules, work on exploit chains, use private credentials, or claim guaranteed income. Treat bounties as uncertain until the issue explicitly states payout terms and acceptance criteria.

## References

Read `references/workflow.md` when preparing a paid audit, GitHub profile package, or PR action pack.

Read `references/commands.md` when scanning with GitHub CLI, checking assignments,
or excluding duplicate pull requests without the main project scripts.
