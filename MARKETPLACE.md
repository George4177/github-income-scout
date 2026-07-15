# GitHub Marketplace Publication Status

Status date: 2026-07-15

## Current Publication State

- v0.4.0 remains the latest public release.
- An exact public Marketplace search for `Low-Risk GitHub Opportunity Scout` and `github-income-scout` did not return a listing on 2026-07-15.
- GitHub's owner-only Marketplace controls and Developer Agreement state cannot be verified from the signed-out public release page.
- The remaining operation must be completed while signed in as the repository owner.

## Ready

- Public repository with one root `action.yml`
- Unique Action name: `Low-Risk GitHub Opportunity Scout`
- Composite Action interface with documented inputs and outputs
- Public semantic release: `v0.4.0`
- GitHub-hosted Ubuntu smoke test passed
- Release ZIP published with SHA-256 verification
- README installation example uses `George4177/github-income-scout@v0.4.0`

The Action can already be consumed by public workflows without a Marketplace listing.

## Marketplace Step Requiring Account Owner

GitHub requires the repository owner to select **Publish this Action to the GitHub Marketplace**, accept the GitHub Marketplace Developer Agreement if it has not already been accepted, choose Marketplace categories, and complete the release action with two-factor authentication. GitHub documents this flow in [Publishing actions in GitHub Marketplace](https://docs.github.com/en/actions/how-tos/create-and-publish-actions/publish-in-github-marketplace).

These are account and agreement actions and are intentionally not automated. No payment account, payout method, private token, password, or two-factor code is required by this repository.

## Exact Owner Handoff

1. Sign in to GitHub as `George4177`.
2. Open [`action.yml`](https://github.com/George4177/github-income-scout/blob/main/action.yml) and use the Marketplace publication banner, or open the [v0.4.0 release edit page](https://github.com/George4177/github-income-scout/releases/edit/v0.4.0).
3. Select **Publish this Action to the GitHub Marketplace**.
4. If GitHub disables the control, review and personally accept the Marketplace Developer Agreement.
5. Wait for GitHub to show **Everything looks good!** for the action metadata.
6. Choose **Utilities** as the primary category if available. Choose **Continuous integration** as the optional secondary category if available.
7. Keep tag `v0.4.0`, title `v0.4.0 - Shareable HTML Reports`, and the existing factual release body.
8. Publish or update the release and complete GitHub's normal 2FA confirmation.
9. Verify that the resulting Marketplace page links back to `George4177/github-income-scout` and displays the current `action.yml` description.

Do not create another release solely to retry the form unless GitHub's UI requires a new release. Do not share a password, token, recovery code, or one-time authentication code with an automation tool.

## Suggested Listing Copy

**Name:** Low-Risk GitHub Opportunity Scout

**Short description:** Score public GitHub issues and export a conservative Markdown, JSON, CSV, or HTML opportunity report.

**Positioning:** A read-only issue research Action for developers and small teams that want a screened shortlist without automated comments, claims, pull requests, or unsafe bounty work.

**Support link:** https://github.com/George4177/github-income-scout/issues/new?template=custom-automation.yml

**Suggested primary category:** Utilities

**Suggested secondary category:** Continuous integration

## Verification

- Release: https://github.com/George4177/github-income-scout/releases/tag/v0.4.0
- Smoke run: https://github.com/George4177/github-income-scout/actions/runs/29205709269
- Action metadata: https://github.com/George4177/github-income-scout/blob/v0.4.0/action.yml
