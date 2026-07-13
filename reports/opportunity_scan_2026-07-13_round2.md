# GitHub Opportunity Scan - Round 2

Date: 2026-07-13

This round searched recently created, open, unassigned Python issues with `help wanted`, `good first issue`, documentation, CI, or GitHub Actions signals. Automated incident reports, secret-setup requests, maintainer-recruitment floods, security work, claimed issues, and repositories without credible activity were excluded before deep review.

## Opportunity List

| Project / platform | Link | Task type | Estimated difficulty | Estimated value | Estimated time | Acceptance standard | Failure risk | Worth doing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub Income Scout Starter Audit | [Service issue #1](https://github.com/George4177/github-income-scout/issues/1) | Fixed-scope research service | Low-Medium | USD 29-49 per qualified order | 2-4 hours | Deliver screened opportunities, top actions, risks, rejected matches, and requested export formats | No external request yet | **Yes: shortest direct-revenue path** |
| traceopt-ai/traceml | [Issue #200](https://github.com/traceopt-ai/traceml/issues/200) | Python CLI, subprocess I/O, tests, docs | Medium | Portfolio and maintainer-trust value; no advertised payout | 3-6 hours | Opt-in flag/env, continuous pipe drain, byte-identical console tee, bounded tail, local artifact, no default behavior change | Pipe deadlock, unbounded memory, output corruption, or changing the child exit code | **Yes: implemented as PR #203** |
| ansible-collections/ansible.mysql | [Issue #848](https://github.com/ansible-collections/ansible.mysql/issues/848) | CI diagnosis across Ansible/MySQL/PyMySQL | Medium-High | Strong CI portfolio value; no advertised payout | 5-10 hours plus matrix setup | Reproduce the exact stable-2.20/MySQL 8.4.9/PyMySQL 1.2.0 failure and fix it if collection-owned | Docker/database matrix cost and possibility that the defect is upstream | No for this round |
| pypsa-meets-earth/pypsa-earth | [Issue #1937](https://github.com/pypsa-meets-earth/pypsa-earth/issues/1937) | Remote dataset retrieval and CI | Medium-High | Scientific Python portfolio value; no advertised payout | 4-10 hours | Restore HydroBASINS retrieval without re-hosting licensed data and make CI pass | Remote provider behavior, licensing constraints, large geospatial environment | No for this round |
| infinum/ai | [Issue #11](https://github.com/infinum/ai/issues/11) | Installer TUI state and Claude plugin discovery | Low-Medium | Codex/Claude workflow portfolio value; no advertised payout | 2-4 hours | Preselect live installed plugins per marketplace, handle disabled/query-failure cases, preserve non-interactive behavior | Very small repository reach and ambiguous installed-versus-enabled semantics | Maybe, lower priority |

## Selection Evidence

`traceopt-ai/traceml#200` was selected because:

- the Apache-2.0 Python project is active, has about 175 stars, and merges external contributions;
- the issue was open, unassigned, and had no implementation PR;
- RFC-0001 section 4.3 defines the design and explicit failure modes;
- the task is CPU-testable and does not require credentials, private data, payment accounts, or GPU access;
- the output is reusable proof for Python automation and reliability work.

The project's contribution guide asks contributors to comment before starting. A scoped implementation note was posted only after reading the RFC and code paths.

## Rejected Scan Noise

The raw scan also contained automated status issues, security-sensitive agent-control challenges, secret-configuration tasks, dependency dashboards, mass-created maintainer requests, already-triaged tickets requiring assignment, and repetitive one-function repositories. These were not treated as viable opportunities and received no comments or pull requests.

No bounty, payment, wallet, credential, or guaranteed-income claim was made.
