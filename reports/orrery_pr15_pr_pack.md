# Orrery #15 PR Pack

## PR Title

```text
docs: add headless engine quickstart
```

## PR Body

```markdown
## Summary

- Add `docs/headless-quickstart.md` for running the Orrery engine from a terminal without starting the desktop app.
- Link the new guide from the README's standalone engine section.
- Cover install options, the hello dry-run, real runner commands, `.loop/` state files, `loop-stop`, `loop-bmad`, and a minimal `loop.json`.

## Testing

- [x] Confirmed `docs/headless-quickstart.md` exists.
- [x] Confirmed README links to `docs/headless-quickstart.md`.
- [x] Confirmed documented console commands are defined in `engine/pyproject.toml`.
- [ ] `WAGGLE_MODEL=deterministic pytest -q` (not applicable; this is not Waggle)
- [ ] `ruff check src/ tests/` (not applicable; docs-only Orrery change)
- [ ] `ruff format --check src/ tests/` (not applicable; docs-only Orrery change)

### Test report

```text
Local documentation checks:
- docs/headless-quickstart.md exists
- README.md contains docs/headless-quickstart.md
- engine/pyproject.toml defines loop, loop-bmad, loop-stop, and loop-supervise
```

Fixes #15
```

## Push Commands When GitHub Write Access Is Available

```bash
cd $WORKSPACE/orrery-pr15
git remote -v
git status
git push -u origin docs/headless-quickstart
```

If working from a fork, push to the fork remote and open a PR against:

```text
NDilanka/orrery:main
```

## Final Pre-PR Checklist

- Recheck https://github.com/NDilanka/orrery/issues/15 is still open.
- Recheck there is no newer PR for `headless-quickstart`.
- Confirm the branch diff only changes `README.md` and `docs/headless-quickstart.md`.
- Do not mention bounty or guaranteed compensation.
