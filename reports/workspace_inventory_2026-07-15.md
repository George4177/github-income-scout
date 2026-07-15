# Workspace Inventory

Date: 2026-07-15

This inventory separates active working copies from completed or superseded copies. It does not authorize deleting a directory; archive or removal should happen only after confirming that no local-only artifact is still needed.

## Keep Active

| Directory | Reason |
| --- | --- |
| `github-income-scout` | Primary product, service assets, reports, and release source |
| `George4177` | Public GitHub Profile repository |
| `imod-python` | PR #1880 is open and awaiting review |
| `kubeflow-website-54` | PR #4431 is open and awaiting owner review |
| `awesome-codex-skills-income-scout` | Directory PR #172 is open in the renamed `composio-community` repository |
| `awesome-ai-automations-scout` | Directory PR #1 is open |
| `tg-spam-filter-issue2` | PR #3 remains open, although it is low priority |

## Safe Archive Candidates

| Directory | Reason |
| --- | --- |
| `traceml` | PR #203 merged on 2026-07-14 |
| `bitbox` | PR #125 merged |
| `cngx-44` | PR #45 merged |
| `orrery-pr15` | PR #23 merged |
| `optiland-issue659` | Superseded by merged upstream PR #660; must not be submitted |
| `Waggle-mcp-pr442` | Candidate was rejected after dependency and competing-work checks; local checkout has no task changes |
| `awesome-github-actions-scout` | Submission was rejected by the distribution gate; the uncommitted listing line has been removed |

## Workspace Metadata

- The top-level `.git` and `.agents` directories are empty and are not a usable repository or active agent workspace.
- The `George4177` checkout is clean, but its directory owner differs from the current Windows account. Use a narrowly scoped safe-directory override or correct the directory owner before normal Git maintenance; do not add a blanket wildcard exception.
