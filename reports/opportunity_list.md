# Money Opportunity List

Generated on 2026-07-05.

## 1. GitHub Income Scout MVP

- Project/platform: Own GitHub repository
- Link: local project in this workspace
- Task type: reusable automation tool and service package
- Estimated difficulty: low-medium
- Estimated value: no guaranteed direct payout; realistic first service target USD 29-199
- Estimated time: MVP 2-5 hours, first public polish 1-2 days
- Acceptance standard: runs locally, has README, sample output, pricing notes, and clear no-spam policy
- Failure risk: no audience yet, needs GitHub profile/README distribution, may require examples from real client profiles
- Worth doing: yes

## 2. Algora issue: unauthorized edit/delete controls visible

- Project/platform: algora-io/algora
- Link: https://github.com/algora-io/algora/issues/238
- Task type: UI bug fix
- Estimated difficulty: medium
- Estimated value: uncertain; issue is related to a bounty platform but no explicit bounty amount was verified
- Estimated time: 3-8 hours after reading repo setup
- Acceptance standard: unauthorized users do not see edit/delete controls; backend protection remains unchanged; UI tests or regression check pass
- Failure risk: local app setup may require services/accounts; issue may already be stale or have hidden permission logic
- Worth doing: maybe, only after reading README and setup cost

## 3. Algora issue: GitHub login redirects to /home 404

- Project/platform: algora-io/algora
- Link: https://github.com/algora-io/algora/issues/329
- Task type: auth redirect bug investigation
- Estimated difficulty: medium-high
- Estimated value: uncertain; no explicit bounty amount verified
- Estimated time: 4-10 hours
- Acceptance standard: successful login redirects to a valid page; regression test or route check is added
- Failure risk: OAuth reproduction may require account state and local secrets; higher risk of blocked setup
- Worth doing: not first

## 4. Bitbox issue: seconds_to_hms tool

- Project/platform: abduznik/bitbox
- Link: https://github.com/abduznik/bitbox/issues/99
- Task type: small Python tool contribution
- Estimated difficulty: low
- Estimated value: portfolio/reputation; no direct payout verified
- Estimated time: 30-90 minutes
- Acceptance standard: function returns h:mm:ss for valid input and has tests/docs following project style
- Failure risk: auto-generated issue may require commenting before work; no money attached
- Worth doing: yes as a low-cost PR candidate, after user confirms external comment/PR
- Current verification: as of 2026-07-05, issue is open, unassigned, has 0 comments, and open PRs do not include `seconds_to_hms`

## 5. PyFenn issue: SingleLayerPerceptron class

- Project/platform: pyfenn/fenn
- Link: https://github.com/pyfenn/fenn/issues/220
- Task type: Python ML API enhancement
- Estimated difficulty: medium-high
- Estimated value: portfolio/reputation; no direct payout verified
- Estimated time: 6-16 hours
- Acceptance standard: class API matches maintainers' expectations, uses existing Trainer, includes tests and docs
- Failure risk: issue asks for collaboration first; new paradigm decision may change scope
- Worth doing: not first unless you want ML library contribution experience

## 6. OpenOperator issue: Action Memory Summarizer

- Project/platform: trmxvibs/OpenOperator
- Link: https://github.com/trmxvibs/OpenOperator/issues/81
- Task type: LLM integration / open-source contribution
- Estimated difficulty: medium
- Estimated value: portfolio/reputation; no direct payout verified
- Estimated time: 3-8 hours after reading architecture
- Acceptance standard: summarizer integrates with existing action memory flow and follows project test style
- Failure risk: LLM integration scope can expand; may require project-specific context and API design decisions
- Worth doing: maybe later, not before Bitbox or publishing the MVP

## Selected Execution Routes

1. Build GitHub Income Scout MVP and package it as a service-ready repo.
2. Use the scout output to pick one low-risk PR candidate, likely Bitbox, after reading its README and contribution guide.
3. Improve GitHub profile/project presentation around automation services once the MVP has sample output.

## Rejected Opportunities

- Security exploit bounty issues involving request smuggling, impersonation, XS-Search, privilege escalation, or similar attack chains. Rejected because they are high-risk and outside the agreed low-risk scope.
- Onboarding bounty issues asking for stars, open PR reviews, or comparison posts. Rejected because they can become fake engagement or low-quality promotional activity.
