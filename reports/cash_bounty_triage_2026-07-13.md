# Cash Bounty Opportunity Triage

Date: 2026-07-13

This scan targeted issues that advertised a fiat amount or referenced a named bounty platform. An advertised amount is not treated as verified payment until funding, claim eligibility, selection rules, and payout evidence are clear.

## Opportunity List

| Project / platform | Link | Task type | Difficulty | Advertised return | Estimated time | Acceptance standard | Failure risk | Worth doing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Builders Bounty / Opire | [issue #1](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1) | Changelog skill or script | Low-Medium | USD 50 advertised | 2-4 hours | Generate categorized changelog since latest tag, sample output, short README | 1,812 issue comments and more than 3,000 repository PRs; many duplicate submissions | No |
| CyberNinja-Dojo | [issue #2](https://github.com/Saiaaax/CyberNinja-Dojo/issues/2) | Python CI stale-artifact gate | Medium | USD 10 advertised | 3-6 hours | Two flags, four tests, operations docs, diagnostic artifact | 36 comments, many claims, and several completed PRs; wallet-heavy payout discussion | No |
| TentOfTrials | [issue #5](https://github.com/weilixiong/TentOfTrials/issues/5) | Python parser fixtures | Low-Medium | USD 25 advertised | 2-5 hours | Independent fixtures and passing parser tests | At least seven related implementations were already visible; repository has a high-volume fork-bounty pattern | No |
| Crystal-PDF / Opire | [issue #3](https://github.com/iii123iii/Crystal-PDF/issues/3) | Responsive frontend fix | Medium | USD 100 advertised | 4-8 hours | Mobile layout from 320px, no overflow, build/lint and visual evidence | Approximately 29 open same-scope PRs and multiple claims | No |
| Baraza Protocol | [issue #26](https://github.com/Build-Africa-DAO/baraza-protocol/issues/26) | Solana deployment documentation | Medium-High | Amount unverified; USD 750 was discussed | 6-12 hours plus devnet access | Live program IDs, explorer links, deploy signatures, repeatable smoke test | Maintainer explicitly stated the USD 750 figure could not be confirmed as a funded bounty; two solid PRs were closed as superseded | No |
| microG GmsCore | [issue #2994](https://github.com/microg/GmsCore/issues/2994) | Android RCS implementation | Very High | USD 14,999 advertised | Multiple weeks or months | Production-quality RCS support accepted upstream | 571 comments, major Android protocol scope, far outside a fast Python/automation engagement | No |
| cybersecurity-roadmap | [issue #1](https://github.com/iamHarshops/cybersecurity-roadmap/issues/1) | Unclear HTML submission | Unscoped | No verified amount | Unknown | No acceptance criteria found | Issue body is an entire HTML page, with no scoped bounty or payout terms | No |
| OpenAgents | [issue #190](https://github.com/ClankerNation/OpenAgents/issues/190) | Solidity meta-transactions | High | USD 7,000 advertised | Multiple days | Signed relay, reimbursement, tests and audit evidence | Requires contributors to paste complete startup instructions and local environment details; outside skill and privacy boundaries | No |
| SecureBananaLabs bug-bounty | [issue #743](https://github.com/SecureBananaLabs/bug-bounty/issues/743) | Recursive issue-generation automation | Unscoped | USD 700 advertised | Unknown | Create child issues and implementation PRs | 1,395 comments, recursive issue creation, repeated claims, and high spam risk | No |
| UnsafeLabs Bounty-Hunters | [issue #827](https://github.com/UnsafeLabs/Bounty-Hunters/issues/827) | TypeScript schema tests | Medium | USD 25 advertised | 3-6 hours | Round-trip and negative tests for all exported schemas | Marked "AI only allowed - no humans", 12 comments, unconventional selection boundary, outside primary Python focus | No |

## Decision

No candidate passed the execution gates. Opening another PR would create duplicate work with a low probability of selection or payment. No claim comment, payout account, wallet address, or bounty application was submitted.

Tasks that request system prompts, startup instructions, home directories, shell details, or other private runtime context are rejected even when the advertised amount is high.

## Reusable Query Pack

Run the cash-focused query pack with:

```powershell
python scripts\issue_scout.py --config examples\cash_bounty_queries.json --min-score 60 --include-rejected --output reports\cash_bounty_opportunities.md
```

Every result still requires manual checks for linked PRs, claim comments, funded payout terms, repository history, and maintainer confirmation.
