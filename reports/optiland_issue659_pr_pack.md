# Optiland Issue 659 PR Pack

Date: 2026-07-06

## Target

- Repository: `optiland/optiland`
- Issue: https://github.com/optiland/optiland/issues/659
- Local checkout: `D:/George/Github/optiland-issue659` equivalent workspace path
- Branch: `fix-curvature-solve-planar-surface`
- Local commit: `0e7354d fix: convert planar surfaces in curvature solves`

## Why This Was Selected

- Open issue, unassigned, no comments.
- Labels include `bug`, `help wanted`, and `good first issue`.
- No obvious duplicate open PR was found in the first 100 open PRs.
- Reproduction is self-contained and included in the issue body.
- The fix is small and isolated to curvature solve radius updates.

## Change Summary

- Added `CurvatureSolve._set_curvature()` to route radius changes through `optic.updater.set_radius()`.
- This reuses existing updater behavior that converts planar surfaces to `StandardGeometry` when a finite radius is applied.
- Preserves `geometry.c` caches for geometries that expose a `c` attribute.
- Updated both marginal and chief ray angle curvature solves to use the shared helper.
- Added a regression test based on the issue reproduction, asserting a planar surface becomes `StandardGeometry`.

## Verification

Command:

```powershell
$env:MPLCONFIGDIR='D:/George/Github/optiland-issue659/.mplconfig'
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m pytest tests/test_solves.py -q -o addopts=
```

Result:

```text
17 passed in 1.37s
```

Notes:

- `pytest`, Optiland runtime dependencies, and `vtk` were installed into the bundled Python runtime to run the targeted tests.
- `.mplconfig/` was generated only as a local cache directory and removed before commit.

## PR Title

```text
Fix curvature solves for planar surfaces
```

## PR Body Draft

````markdown
## Summary

- route curvature solve radius updates through `optic.updater.set_radius()`
- convert planar surfaces to `StandardGeometry` when a finite curvature solve is applied
- add a regression test for the planar-surface reproduction from #659

## Verification

```powershell
$env:MPLCONFIGDIR='D:/George/Github/optiland-issue659/.mplconfig'
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m pytest tests/test_solves.py -q -o addopts=
```

Result: `17 passed in 1.37s`

Fixes #659
````

## Push Checklist

1. Ensure the user's GitHub write path can fork/push to `George4177/optiland`.
2. Push branch `fix-curvature-solve-planar-surface`.
3. Open a PR against `optiland/optiland:master`.
4. Use the PR title and body above.
5. Do not claim bounty/payment; this is a portfolio credibility PR unless maintainers explicitly offer compensation.
