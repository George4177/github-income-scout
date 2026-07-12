# GitHub Marketplace Publication Status

Status date: 2026-07-13

## Ready

- Public repository with one root `action.yml`
- Unique Action name: `Low-Risk GitHub Opportunity Scout`
- Composite Action interface with documented inputs and outputs
- Public semantic release: `v0.3.0`
- GitHub-hosted Ubuntu smoke test passed
- Release ZIP published with SHA-256 verification
- README installation example uses `George4177/github-income-scout@v0.3.0`

The Action can already be consumed by public workflows without a Marketplace listing.

## Marketplace Step Requiring Account Owner

GitHub requires the repository owner to select **Publish this Action to the GitHub Marketplace**, accept the GitHub Marketplace Developer Agreement if it has not already been accepted, choose Marketplace categories, and complete the release action with two-factor authentication.

These are account and agreement actions and are intentionally not automated. No payment account, payout method, private token, password, or two-factor code is required by this repository.

## Suggested Listing Copy

**Name:** Low-Risk GitHub Opportunity Scout

**Short description:** Score public GitHub issues and export a conservative Markdown, JSON, or CSV opportunity report.

**Positioning:** A read-only issue research Action for developers and small teams that want a screened shortlist without automated comments, claims, pull requests, or unsafe bounty work.

**Support link:** https://github.com/George4177/github-income-scout/issues/new?template=custom-automation.yml

## Verification

- Release: https://github.com/George4177/github-income-scout/releases/tag/v0.3.0
- Smoke run: https://github.com/George4177/github-income-scout/actions/runs/29205709269
- Action metadata: https://github.com/George4177/github-income-scout/blob/v0.3.0/action.yml
