# Live GitHub Opportunity Snapshot

Date: 2026-07-06

Source query:

```text
state:open label:"good first issue" label:"help wanted" language:Python created:>2026-06-01 -label:security
```

This snapshot uses public GitHub issue search results. It is a screening pass, not a claim that a bounty exists or that a PR will be accepted.

## Shortlist

| Project | Link | Task type | Difficulty | Est. value | Est. time | Acceptance standard | Failure risk | Worth doing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Abhigyan-Shekhar/Waggle-mcp | https://github.com/Abhigyan-Shekhar/Waggle-mcp/issues/442 | Documentation | Low | Portfolio and credibility; no verified bounty | 1-2 hours | Add a docs walkthrough for `recompute_communities`, `get_communities`, cluster id ordering, `resolution`, and Graph Studio community coloring | Need to read surrounding docs and verify terminology; comments may contain hidden context | Yes, good fallback PR candidate |
| Abhigyan-Shekhar/Waggle-mcp | https://github.com/Abhigyan-Shekhar/Waggle-mcp/issues/444 | Documentation | Low-Medium | Portfolio and credibility; no verified bounty | 1-3 hours | Add a docs example for code-aware memory behavior, including fenced Python code, resulting code entity nodes, `code-analysis` extra, and regex fallback | Need to verify current implementation before documenting behavior | Maybe, after reading implementation |
| optiland/optiland | https://github.com/optiland/optiland/issues/659 | Bug fix | Medium | Portfolio value; no verified bounty | 3-6 hours | Planar surface with a curvature solve is converted to a standard/non-planar surface; add or update tests | Domain-specific optics code and Python 3.13 setup may slow validation | Maybe, higher technical setup risk |

## Rejected Or Deferred

| Project | Link | Reason |
| --- | --- | --- |
| vllm-project/vllm-omni | https://github.com/vllm-project/vllm-omni/issues/4884 | Already assigned and model integration scope is likely too large for a fast credibility PR |

## Best Next Move

For a fast public credibility contribution, `Abhigyan-Shekhar/Waggle-mcp#442` is the best current candidate. It is docs-only, has clear acceptance criteria, and avoids security, credentials, scraping, payment, and platform-rule risks.

For direct income, publishing GitHub Income Scout and offering the Starter Audit remains the stronger path because these issues do not show verified payouts.

## Follow-Up Recheck

After deeper review, `Waggle-mcp#442` should not be executed as-is. It depends on PR #419, but #419 is closed, marked invalid, and not merged. Current `main` does not contain the requested `recompute_communities` / `get_communities` tools or Graph Studio community toggle, so a PR based on that issue would risk documenting non-existent behavior.

Replacement candidate selected:

| Project | Link | Task type | Difficulty | Est. value | Est. time | Worth doing |
| --- | --- | --- | --- | --- | --- | --- |
| NDilanka/orrery | https://github.com/NDilanka/orrery/issues/15 | Documentation | Low | Portfolio credibility; no verified bounty | 1-2 hours | Yes, local PR branch prepared |
