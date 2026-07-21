# Roadmap

Status date: 2026-07-21

## Shipped

- Search public GitHub issues from configurable queries
- Score low-risk opportunities and expose assignment/comment risk
- Reject exploit, fake-engagement, credential, unfunded, and platform-abuse tasks
- Generate Markdown, JSON, CSV, and standalone print-friendly HTML reports
- Enrich reports with repository health signals such as stars, forks, last push date, and activity hints
- Support deterministic offline validation and client-ready sample data
- Build Starter Audit and Profile + Opportunity Pack delivery bundles
- Run as a reusable Composite Action and scheduled GitHub Actions workflow
- Publish GitHub Pages, public delivery examples, a Profile offer, and release v0.4.0
- Publish v0.4.0 as Low-Risk GitHub Opportunity Scout in GitHub Marketplace
- Enable repository Discussions and publish a template-compliant GitHub Community Actions question
- Score issue-body clarity signals such as reproduction steps, expected/actual behavior, acceptance criteria, environment details, and verification steps
- Apply capped confidence penalties for `blocked`, `needs discussion`, `needs reproduction`, and clarification-needed labels
- Explain clarity and status-label adjustments in generated opportunity risk notes without adding API requests
- Release v0.5.0 with explainable issue clarity scoring and focused regression coverage
- Verify v0.5.0 as the Marketplace latest version and pass the released Action consumer smoke test

## Now: Discovery and Conversion

- Observe the first genuine non-collaborator request-form flow without creating a synthetic test account
- Monitor open iMOD, Kubeflow, and directory PRs for actionable review
- Complete the first qualified paid Starter Audit and convert its feedback into evidence-backed improvements

## Next Product Improvements

- Add an automated duplicate-PR and competing-claim precheck for top candidates
- Cache repository-level metrics within each workflow run and distinguish meaningful maintainer activity from reactions or claim comments
- Add maintainer response-time and open-PR-volume signals without exhausting API limits
- Add local historical snapshots and saved accept/reject decisions
- Add client/profile-specific scoring weights with explicit configuration

## Later

- Add a local history dashboard only after saved-history data exists
- Add direct PDF export only if print-to-PDF from the HTML deliverable proves insufficient
- Add private recurring-monitoring deployment for a paying client
