# GitHub Income Opportunity Triage

Date: 2026-07-13

Source: [`live_snapshot_2026-07-13.json`](live_snapshot_2026-07-13.json), followed by manual issue and duplicate-PR checks.

## Opportunity List

| Project / platform | Link | Task type | Difficulty | Estimated return | Time | Acceptance standard | Failure risk | Worth doing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kubeflow MCP Server #68 | [issue](https://github.com/kubeflow/mcp-server/issues/68) | Python unit tests for Trainer MCP tools | Medium-High | Portfolio proof; no verified payout | 8-16 hours for stated scope | Clear TODOs, Pattern C tests for write tools, `make test-python` green | Large scope, depends on PR #6, another contributor already requested a section | No, do not compete now |
| IntelMQ #2382 | [issue](https://github.com/certtools/intelmq/issues/2382) | Python URL validation regression | Medium | Portfolio proof; no verified payout | 3-8 hours | Maintainer-approved URL policy and focused regression tests | Existing PR #2714 already implements one approach; design remains under discussion | No, duplicate work exists |
| NightmareNet #183 | [issue](https://github.com/Adit-Jain-srm/NightmareNet/issues/183) | README badge correction | Low | Event XP / portfolio only; no verified cash payout | Under 1 hour | Python and framework badges match project metadata | Another contributor requested assignment; contest task has weak income value | No, do not compete |
| MergeOS Lappa #1 | [issue](https://github.com/mergeos-bounties/Lappa/issues/1) | Windows quickstart documentation | Low-Medium | 25 MRG token; fiat value and payout liquidity unverified | 2-5 hours | `docs/WINDOWS.md`, README link, accurate screenshots | Requires starring repositories, already has a full implementation comment, related PR #19 closed | No, engagement-gated and contested |
| prompt-preflight #57 | [issue](https://github.com/akg268/prompt-preflight/issues/57) | Non-coding prompt templates | Low-Medium | Portfolio only; no verified payout | 2-4 hours | Templates match repository schema and tests | Small project, unclear demand, comment activity requires claim check | Backup only |

## Rejected Noise Classes

- Automated `Bounty Alert` issues are feeds, not implementation tasks.
- Renovate-style `Dependency Dashboard` issues are maintenance indexes, not scoped contributor work.
- Generic vulnerability and zero-day trackers are outside the low-risk boundary.
- Bounties requiring repository stars before a claim are rejected as engagement-gated work.
- ECSoC/XP contest issues are downgraded because points are not verified income.
- Expensify USD 250 issues in this snapshot were already assigned and heavily discussed, so they are not available opportunities.

## Selected Execution

No external issue passed all gates for a responsible PR. Instead, the scanner was corrected so a paid Starter Audit will not present these false positives as high-value work. The change adds regression tests for engagement-gated bounties, automated bounty feeds, dependency dashboards, and XP-only contests.

## Next Check

Prioritize a candidate only when it is open, unassigned, not already implemented, has a clear test or documentation acceptance path, and offers either verified cash terms or strong portfolio relevance without requiring promotional engagement.
