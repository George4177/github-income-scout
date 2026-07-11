# cngx Issue #44 PR Pack

Date: 2026-07-11

## Upstream Scope

- Issue: [aadi-joshi/cngx#44](https://github.com/aadi-joshi/cngx/issues/44)
- Task: add copy-paste verification recipes for Claude Code, Cursor, Codex, aider, and PR/merge bots.
- Current issue state at review: open, unassigned, no comments.
- Duplicate check: no related open PR was identified during the initial review.
- Local checkout: `D:/乔治/Github/cngx-44`
- Branch: `docs/coding-agent-recipes`
- Commit: `f4b2975 docs: add coding agent verification recipes`

## Files Changed

- `docs/guides/coding-agent-recipes.md`: concise recipes with command, verified outcome, and blocked outcome.
- `docs/guides/gate-coding-agent.md`: links the tool-specific recipe page from the main guide and Related section.
- `mkdocs.yml`: adds the recipe page to the Guides navigation.

## Verification

- `python -m cngx verify --help`: passed; confirmed `--output-file`, `--stdin`, and command-after-`--` syntax.
- `python -m pytest tests/integration/test_verify_cli.py tests/unit/test_github_action.py::test_action_yml_exists_and_has_required_inputs -q`: 6 passed in 1.01 seconds.
- `python -m mkdocs build --strict`: passed.
- `git diff --check`: passed.
- Full Action local smoke was not used as evidence because it performs a separate package installation and stalled under the current intermittent network. No product code or Action implementation changed.

## Acceptance Mapping

- Claude Code, Cursor, Codex: each uses `--output-file agent.md` with a real command.
- aider: uses `--stdin` with a piped last assistant message.
- PR/merge bots: uses the repository's composite GitHub Action and explains required-check behavior.
- Output behavior: every recipe distinguishes `VERIFIED` from `BLOCKED`.
- Discoverability: linked from `gate-coding-agent.md` and `mkdocs.yml`.
- Style: no em dashes were introduced in the new recipe page.

## Proposed PR Title

`docs: add coding agent verification recipes`

## Proposed PR Body

```markdown
## Summary

- add copy-paste `cngx verify` recipes for Claude Code, Cursor, Codex, and aider
- add a GitHub Actions recipe for PR and merge bots
- link the new page from the existing agent-gating guide and docs navigation

## Why

Users often arrive with a specific coding agent already in their workflow. These short recipes show how to bind that agent's final claim to a real test command and make the `VERIFIED` or `BLOCKED` result actionable.

Closes #44.

## Verification

- `python -m cngx verify --help`
- `python -m pytest tests/integration/test_verify_cli.py tests/unit/test_github_action.py::test_action_yml_exists_and_has_required_inputs -q` (6 passed)
- `python -m mkdocs build --strict`
- `git diff --check`
```

## External Action Status

Submitted as [aadi-joshi/cngx#45](https://github.com/aadi-joshi/cngx/pull/45) on 2026-07-11.

- Fork: `George4177/cngx`
- Head branch: `docs/coding-agent-recipes`
- Initial state: open, ready for review, mergeable
- Initial reviews/comments/checks: none reported
- No bounty or payment claim was made
