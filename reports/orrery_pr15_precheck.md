# Orrery #15 PR Precheck

Date: 2026-07-06

## Opportunity

- Project: `NDilanka/orrery`
- Issue: https://github.com/NDilanka/orrery/issues/15
- Type: documentation
- Labels: `documentation`, `good first issue`
- Status checked: open, unassigned, 0 comments
- Open related PRs checked: none found in the first open PR page

## Why This Was Chosen

This is a low-risk credibility PR candidate:

- docs-only scope
- no security exploit work
- no trading or financial automation
- no fake engagement
- no credential handling
- clear acceptance criteria
- no current assignee

Expected direct income: none verified. Expected value is portfolio credibility that supports the Starter Audit service offer.

## Acceptance Criteria From Issue

- Add `docs/headless-quickstart.md`
- Explain how to run the engine without the desktop app
- Include install instructions for `orrery-loop` or editable `./engine`
- Show a minimal `loop.json` path
- Explain `loop` / `loop-bmad`
- Explain `.loop/` state and logs
- Explain safe stop through `loop-stop`
- Link the new page from README

## Repository Facts Verified

- `engine/pyproject.toml` defines console scripts:
  - `loop`
  - `loop-bmad`
  - `loop-qa`
  - `loop-supervise`
  - `loop-stop`
- `examples/hello/loop.json` is a working generic loop seed.
- `examples/hello/README.md` documents the dry-run and real-run flow.
- `README.md` already has an "engine, standalone" section, which is the right link location.

## Local Work Prepared

Local clone:

```text
$WORKSPACE/orrery-pr15
```

Branch:

```text
docs/headless-quickstart
```

Local commit:

```text
2ed3391 docs: add headless engine quickstart
```

Changed files:

- `README.md`
- `docs/headless-quickstart.md`

## Validation Performed

- Confirmed `docs/headless-quickstart.md` exists.
- Confirmed README links to `docs/headless-quickstart.md`.
- Confirmed documented command names exist in `engine/pyproject.toml`.
- Confirmed local Orrery working tree is clean after commit.

Full project tests were not run because this is a documentation-only change and installing Orrery's full frontend/engine toolchain is outside the current low-risk preparation scope.

## Risk Notes

- The project is new and small, so PR merge probability is uncertain.
- No direct bounty or payout was found.
- Do not push/open the PR until GitHub write access is available and the issue is rechecked as still open/unassigned.
