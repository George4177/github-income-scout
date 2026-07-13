# TraceML Issue #200 PR Pack

Date: 2026-07-13

## Upstream Scope

- Issue: [traceopt-ai/traceml#200](https://github.com/traceopt-ai/traceml/issues/200)
- Design reference: RFC-0001 section 4.3 on the upstream `rfc-robustness` branch.
- Task: optionally persist the bounded stderr tail of the launched training process without changing default console behavior.
- Starting state: open, unassigned, no comments, and no implementation PR.
- Contribution requirement: comment on the matching issue before starting.
- Branch: `feat/capture-stderr-tail`
- Commit: `8cbbf48 Capture bounded child stderr tails`

## Files Changed

- `src/traceml_ai/launcher/process.py`: continuously drains piped stderr on a daemon thread, tees original bytes, and retains an exact 64 KiB tail.
- `src/traceml_ai/launcher/cli.py`: adds `--capture-stderr`.
- `src/traceml_ai/launcher/commands.py`: supports `TRACEML_CAPTURE_STDERR=1`, starts and finishes capture, and preserves child exit status.
- `src/traceml_ai/launcher/manifest.py`: registers `crash_stderr.log` when present.
- `tests/runtime/test_stderr_capture.py`: verifies opt-in resolution, unchanged disabled `Popen` behavior, flood resistance, byte-identical tee, nonzero child exit, and exact tail bounds.
- `tests/runtime/test_launcher.py`: verifies parser defaults and manifest artifact discovery.
- `docs/user_guide/faq.md`: documents usage, output location, bound, default-off behavior, and local-only storage.

## Acceptance Mapping

- Flag and environment opt-in: implemented.
- Default off: the disabled path does not pass a `stderr` argument to `Popen`.
- Continuous drain: the reader starts immediately and drains in 8 KiB chunks.
- No full-pipe deadlock: a test emits more than the OS pipe capacity and completes within 10 seconds.
- Console output preserved: the test compares the complete tee byte-for-byte.
- Bounded memory: only the last 64 KiB is retained; the focused test uses a 4 KiB bound and asserts the exact suffix.
- Local artifact: `logs/<run-name>/crash_stderr.log` is written and added to `manifest.json`.
- Training safety: tee/write failures are best-effort, and the launcher returns the original child status.

## Verification

- `python -m pytest tests/runtime/test_stderr_capture.py tests/runtime/test_launcher.py -q`: 29 passed.
- `pre-commit run --all-files --show-diff-on-failure`: all hooks passed using the repository-pinned hook versions.
- `git diff --check`: passed.
- A broader runtime collection was not used as pass evidence because the lightweight local environment intentionally omitted PyTorch; the upstream integration job installs the Torch extra.

## External Action

- Contribution note: [issue comment](https://github.com/traceopt-ai/traceml/issues/200#issuecomment-4958593804)
- Pull request: [traceopt-ai/traceml#203](https://github.com/traceopt-ai/traceml/pull/203)
- Initial PR state: open, mergeable, review required, and awaiting CI.
- No direct payout is advertised.

## Revenue Relevance

The PR is public proof of Python subprocess reliability, bounded buffering, CLI design, tests, and documentation. It can support fixed-scope automation proposals, but it is not counted as revenue or a qualified lead.
