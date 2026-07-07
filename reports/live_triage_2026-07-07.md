# Live GitHub Opportunity Triage - 2026-07-07

Source snapshot: `reports/live_snapshot_2026-07-07.md`

## Summary

The live scan produced 20 candidates. Manual review removed the top-ranked candidates that were noisy, already accepted by another contributor, or outside the low-risk contribution boundary. The best near-term move is still to keep the public service funnel visible, monitor the open PRs, and avoid opening another Bitbox PR until #125 receives maintainer feedback.

## Opportunity List

| Project / Platform | Link | Task Type | Difficulty | Estimated Value | Time | Acceptance Standard | Failure Risk | Worth Doing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `jatinkrmalik/vocalinux` | https://github.com/jatinkrmalik/vocalinux/issues/233 | Wikipedia/documentation request | Low-Medium | Portfolio only; no clear bounty | 1-4 hours | Maintainer accepts a compliant external Wikipedia page | Wikipedia notability and platform-rule risk; already noisy | No |
| `kike-alt/DeWordle` | https://github.com/kike-alt/DeWordle/issues/795 | CI/CD composite action | Medium | Possible program points, not a direct bounty | 2-6 hours | Shared Node setup used by at least two workflows, CI remains green | Another contributor was accepted and a related PR was merged | No |
| `RIOT-OS/Release-Specs` | https://github.com/RIOT-OS/Release-Specs/issues/337 | Release / CI support | Medium | Portfolio only unless explicitly assigned | 2-6 hours | Release process contribution accepted by maintainers | Release coordination can be broad and time-sensitive | Maybe, only after maintainer-specific scope is clear |
| `josdem/py-vetlog-buddy` | https://github.com/josdem/py-vetlog-buddy/issues/185 | Python entry point | Medium | Portfolio value; possible client-relevant Python example | 3-8 hours | `uv run stats --year ${year}` works and tests pass | Another contributor already asked to be assigned | Backup only; do not claim now |
| `abduznik/bitbox` | https://github.com/abduznik/bitbox/issues/145 | Small Python tool | Low-Medium | Portfolio value; fast credibility if accepted | 1-2 hours | `run(text: str) -> str` returns `"True"` for valid `YYYY-MM-DD` ISO dates | Same repository already has our #125 waiting for review | Worth doing later, not before #125 review |
| `abduznik/bitbox` | https://github.com/abduznik/bitbox/issues/144 | Small Python tool | Low-Medium | Portfolio value; fast credibility if accepted | 1-2 hours | `run(text: str) -> str` returns `"True"` for valid UUIDs | Same repository already has our #125 waiting for review | Worth doing later, not before #125 review |
| `fossasia/voxbento` | https://github.com/fossasia/voxbento/issues/246 | HTML/CSS extraction | Low-Medium | Portfolio value | 1-4 hours | Extract stylesheet without visual change | Maintainer explicitly told another contributor to raise a PR | No |

## Selected Direction

1. Keep `George4177/github-income-scout` and the profile README as the public service funnel.
2. Monitor `abduznik/bitbox#125` and `profit-coders/tg-spam-filter#3` for review feedback.
3. If Bitbox #125 is accepted or maintainers respond positively, prepare the next single Bitbox tool PR from #144 or #145.

## Action Taken

- Generated the new live opportunity snapshot: `reports/live_snapshot_2026-07-07.md`.
- Updated the GitHub profile README so service request links appear near the top of the profile.
- Skipped GitHub profile status because the current token lacks GitHub's required `user` scope for the `changeUserStatus` mutation.

## Revenue Impact

This does not directly create revenue yet. It improves the public conversion path and prevents low-quality duplicate PR behavior, which is important for sustainable GitHub-based client acquisition.
