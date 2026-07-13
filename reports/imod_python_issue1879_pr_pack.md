# iMOD Python Issue #1879 PR Pack

Date: 2026-07-13

## Opportunity Assessment

| Field | Assessment |
| --- | --- |
| Project / platform | [Deltares/imod-python](https://github.com/Deltares/imod-python) |
| Issue | [#1879: Better explain difference between Well and LayeredWell](https://github.com/Deltares/imod-python/issues/1879) |
| Task type | Python API documentation and executable user-guide example |
| Estimated difficulty | Low-Medium |
| Estimated value | Portfolio and maintainer-trust value; no direct bounty advertised |
| Estimated time | 2-4 hours |
| Acceptance standard | Explain both layer-assignment paths accurately and add an example that executes in the project test workflow |
| Failure risk | Domain-specific terminology, incorrect expected rate allocation, or documentation CI failure |
| Worth doing | Yes: clear scope, active project, no assignee, no comments, and no duplicate PR at start |

## Precheck

- The issue was open and unassigned before implementation.
- The issue had no comments or competing claim.
- Searches for open PRs containing `1879` or `LayeredWell` returned no matches.
- The branch started even with upstream `master`.
- The contribution guide requires Ruff formatting and executable examples; user-guide files are run by `imod/tests/test_examples.py`.
- The repository is MIT licensed and active.

## Implementation

- `imod/mf6/wel.py`: explains that `Well` derives cells from screen elevations and distributes the total rate by transmissivity.
- `imod/mf6/wel.py`: explains that `LayeredWell` retains explicit model layers and pre-allocated rates.
- `imod/mf6/wel.py`: corrects the shared `to_mf6_pkg` documentation so it describes both subclasses.
- `examples/user-guide/04-wells.py`: adds a deterministic two-layer example with executable assertions.

The example demonstrates:

- `Well`: a total rate of `-40` is distributed as `-10` and `-30` because layer transmissivities are in a 1:3 ratio.
- `LayeredWell`: explicit layer rates of `-20` and `-20` remain unchanged despite different hydraulic conductivities.

## Verification

- New example executed successfully with Python 3.12 in an isolated virtual environment.
- `ruff check examples/user-guide/04-wells.py imod/mf6/wel.py`: passed.
- `ruff format --check examples/user-guide/04-wells.py imod/mf6/wel.py`: passed.
- `git diff --check`: passed.
- The first 1x1 draft was rejected during local execution because iMOD requires explicit cell-size metadata for singleton coordinates; the committed example uses a valid 2x2 grid.

## External Action

- Pull request: [Deltares/imod-python#1880](https://github.com/Deltares/imod-python/pull/1880)
- Branch: `George4177:docs/well-vs-layeredwell`
- Commit: `e67d9813 Docs explain Well layer assignment`
- Initial state: open, mergeable, review required, no checks reported yet.
- No bounty, payment, or guaranteed outcome was claimed.

## Revenue Relevance

This PR has no advertised direct payout. Its purpose is credible public proof in Python documentation, scientific-data tooling, and tested examples. Revenue remains USD 0 until a paid request is accepted and delivered.
