# Live GitHub Opportunity Triage - 2026-07-11

This shortlist was manually checked against current public issue and pull-request state. Revenue estimates distinguish direct payment from portfolio value; none of the retained issues currently provides a verified cash payout.

| Project / platform | Link | Task type | Difficulty | Estimated return | Time | Acceptance standard | Main failure risk | Worth doing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KryptosAI/mcp-observatory #230 | [issue](https://github.com/KryptosAI/mcp-observatory/issues/230) | GitHub Actions / GHCR | Low-Medium | Portfolio proof; no verified payout | 1-3 hours after dependency lands | Release and manual triggers publish `latest` and version tags; published image can be pulled | Depends on the still-separate Dockerfile work in #227; cannot currently pass end-to-end acceptance alone | Later, after #227 is merged |
| aadi-joshi/cngx #44 | [issue](https://github.com/aadi-joshi/cngx/issues/44) | Codex/agent documentation | Low-Medium | Portfolio proof; possible service lead; no verified payout | 2-4 hours | Accurate recipes for Claude Code, Cursor, Codex, aider, and PR bots; linked in docs nav; each recipe under the requested size | Very small repository and young project; low discovery value | Yes, after cloning and command verification |
| profit-coders/tg-spam-filter #3 | [PR](https://github.com/profit-coders/tg-spam-filter/pull/3) | Existing documentation PR | Low | Credibility only; no verified payout | 10-20 minutes if feedback arrives | Maintainer accepts the contribution or requests a scoped correction | Maintainer inactivity; no checks or review activity since opening | Monitor only; do not send repeated reminders |
| Lee-Dongwook/E2E-Self-Heal #2 | [issue](https://github.com/Lee-Dongwook/E2E-Self-Heal/issues/2) | README / GitHub Action positioning | Low | Portfolio proof; no verified payout | 1-2 hours | README clearly leads with the Action and provides a verified one-line installation path | Existing comment may indicate another contributor is already engaging; new repository has limited proof value | Skip unless it remains clearly unclaimed |
| KryptosAI/mcp-observatory #227 | [issue](https://github.com/KryptosAI/mcp-observatory/issues/227) | Docker packaging | Medium | Portfolio proof; no verified payout | 2-4 hours | Image builds, `--version` works, and production image remains reasonably small | Issue instructions assume prebuilt `dist/`; build context and runtime paths require real repository validation | Maybe; only with full Docker validation |

## Rejected Matches

- Recent bounty searches were dominated by vulnerability work, crypto-token payouts, heavily contested issues, or repositories with weak payout credibility. These were rejected under the project's safety and sustainability rules.
- `SecureBananaLabs/bug-bounty` results had hundreds to more than one thousand comments and security/engagement signals. They are not suitable low-risk opportunities.
- Smart-contract and security-challenge tasks were rejected because they exceed the authorized risk boundary.
- Newly created repositories with several vague `good first issue` tickets were deprioritized when acceptance criteria, maintainer history, or durable portfolio value were weak.

## Recommended Order

1. Keep `tg-spam-filter#3` quiet until maintainer feedback arrives.
2. Prepare `cngx#44` only after cloning succeeds and every documented command is checked against the current CLI.
3. Revisit `mcp-observatory#230` after #227 supplies a usable Dockerfile, or consider #227 itself only when local Docker validation is available.

No issue was claimed and no external commitment was made during this triage.
