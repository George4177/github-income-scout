# Starter Audit Case Study

This case study shows how GitHub Income Scout can support a small paid service without promising income, merged pull requests, bounty awards, or sponsorship.

## Client Snapshot

- Profile: independent developer building proof of work for Python automation and GitHub workflows
- Weekly time: 3-5 hours
- Preferred work: documentation fixes, small scripts, CI cleanup, README improvements
- Boundaries: no exploit work, fake engagement, credential handling, scraping behind logins, or platform bypasses

## Input

The client provides:

- GitHub profile link
- preferred languages and tools
- time available per week
- examples of repositories or topics they like
- any task types they want to avoid

No private tokens, passwords, payment details, or production credentials are needed.

## Process

1. Run GitHub issue searches from the configured query pack.
2. Score matches for fit, clarity, likely effort, and safety.
3. Reject high-risk, stale, unclear, assigned, or fake-engagement matches.
4. Review the top candidates manually before recommending action.
5. Convert the best matches into a short client-ready brief.

## Example Findings

| Rank | Opportunity Type | Why It Fits | First Action |
| ---: | --- | --- | --- |
| 1 | Documentation quickstart | Low-risk, clear acceptance criteria, visible contribution | Read README and contribution guide, then prepare a focused docs PR |
| 2 | Small Python script issue | Practical automation scope with limited blast radius | Reproduce expected behavior locally before commenting |
| 3 | GitHub Actions cleanup | Useful portfolio signal and repeatable service angle | Inspect failing workflow logs and propose the smallest fix |

## Rejected Matches

| Rejection Reason | Why It Was Rejected |
| --- | --- |
| Security exploitation | Too risky and outside the service boundary |
| Trading or speculative finance | Poor fit for a low-risk service offer |
| Assigned issue | Higher chance of duplicated work |
| Missing acceptance criteria | Too much uncertainty for a fixed-scope starter package |
| Feature depends on unmerged PR | Risk of documenting or building against unavailable behavior |

## Deliverables

The Starter Audit delivery includes:

- Markdown report with screened opportunities
- CSV or JSON export when useful
- top 3 action plan
- acceptance criteria summary
- failure-risk notes
- rejected-match summary
- one GitHub profile or README positioning suggestion

## Example Client Recommendation

Start with one documentation quickstart or small automation issue. It is more likely to become a credible portfolio artifact than a vague bounty hunt, and it can be completed without asking for secrets or making public claims before the work is understood.

## Follow-Up Offer

After the Starter Audit, a fixed-scope follow-up can help with:

- preparing a clean pull request
- rewriting a project README
- building a small automation script
- setting up a recurring weekly opportunity report
- turning the audit process into a reusable GitHub Action or private dashboard

Follow-up work should always define scope, acceptance criteria, and boundaries before implementation.
