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
python -m pytest tests/test_solves.py -q -o addopts=
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
python -m pytest tests/test_solves.py -q -o addopts=
```

Result: `17 passed in 1.37s`

Fixes #659
````

## Push Checklist

Status update on 2026-07-06: do not open this PR now. A duplicate upstream PR appeared after the local fix was prepared:

- https://github.com/optiland/optiland/pull/660

Keep the local branch as a reference implementation and portfolio-quality exercise, but avoid submitting a duplicate PR unless the existing PR is closed without resolution and the issue remains open.
