## Summary

- Add `docs/headless-quickstart.md` for running the Orrery engine from a terminal without starting the desktop app.
- Link the new guide from the README's standalone engine section.
- Cover install options, the hello dry-run, real runner commands, `.loop/` state files, `loop-stop`, `loop-bmad`, and a minimal `loop.json`.

## Testing

- [x] Confirmed `docs/headless-quickstart.md` exists.
- [x] Confirmed README links to `docs/headless-quickstart.md`.
- [x] Confirmed documented console commands are defined in `engine/pyproject.toml`.

### Test report

```text
Local documentation checks:
- docs/headless-quickstart.md exists
- README.md contains docs/headless-quickstart.md
- engine/pyproject.toml defines loop, loop-bmad, loop-stop, loop-qa, and loop-supervise
```

Fixes #15
