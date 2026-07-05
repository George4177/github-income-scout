# Launch Checklist

Use this checklist to turn the local MVP into a public, service-ready GitHub asset.

## Before Publishing

- Run `scripts\check_all.py`.
- Confirm `README.md`, `pricing.md`, `service_offer.md`, and `site/index.html` do not promise guaranteed income.
- Confirm no token, API key, payment detail, or private account information is present.
- Confirm `examples/` and `reports/` only contain safe sample or intentionally public data.
- Create a release bundle with `scripts\create_release_bundle.ps1`.

## Repository Setup

- Create a public GitHub repository named `github-income-scout`.
- Use this repository description:

```text
Find and score low-risk GitHub issue opportunities for practical open-source contribution.
```

- Push the local `main` branch.
- Enable issue forms.
- Enable GitHub Pages with GitHub Actions as the source.
- Pin the repository on the GitHub profile.
- Add the profile README copy from `profile/README.md` where appropriate.

## v0.1.0 Release

- Tag the first release as `v0.1.0`.
- Use `RELEASE_NOTES.md` as the release body.
- Attach the local release bundle if desired.
- Keep the release factual: no bounty guarantees, no income guarantees, no fake urgency.

## First Week Actions

- Day 1: publish the repository, enable Pages, pin it, and test the public page.
- Day 2: post one low-pressure community update where self-promotion is allowed.
- Day 3: run one fresh GitHub opportunity scan and save a public-safe sample report.
- Day 4: offer 2 discounted Starter Audits to collect feedback.
- Day 5: convert feedback into README and service copy improvements.
- Day 6: prepare one small open-source PR candidate, such as Bitbox `seconds_to_hms`, only after verifying it is still open.
- Day 7: review inbound issues, profile views, stars, and direct replies; adjust the offer if there is no clear interest.

## Revenue Milestone

The first practical milestone is one Starter Audit sale at USD 29-49. That is more controllable than waiting for a bounty payout and creates proof for a recurring weekly audit offer.

## Stop Conditions

Pause a channel or task if it requires:

- fake stars, fake reviews, or fake engagement
- exploit development or unauthorized testing
- private credentials, payment data, or account sharing
- mass unsolicited comments or messages
- misleading income claims
