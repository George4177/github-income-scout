# Live Opportunity Triage - 2026-07-12

This shortlist was manually rechecked against current issue assignments,
comments, open pull requests, repository scope, and local verification options.
Estimated value is portfolio or lead value unless a project publishes explicit
bounty terms.

| Project / platform | Link | Task type | Difficulty | Estimated value | Time | Acceptance standard | Failure risk | Worth doing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kubeflow Website / MCP Server | [mcp-server#54](https://github.com/kubeflow/mcp-server/issues/54) | Official documentation | Low-Medium | Strong portfolio proof; no stated bounty | 2-4 hours | MCP Server appears under Kubeflow Subprojects with Overview, Getting Started, and repository navigation; Hugo build passes | DCO/Prow workflow and maintainer review | **Yes - implemented locally** |
| header-handler | [header-handler#10](https://github.com/curtyo18/header-handler/issues/10) | TypeScript cleanup/performance | Medium | Portfolio value | 4-8 hours | Four stated cleanups pass extension tests without behavior regressions | Browser-extension setup and broader scope than current portfolio | Maybe, second choice |
| Hekmo | [Hekmo#9](https://github.com/Sherwin-14/Hekmo/issues/9) | GitHub Actions CI | Low-Medium | Portfolio value | 2-4 hours | Ruff and tests run on push/PR; package builds on releases | Maintainer already told another contributor to proceed | **No - already claimed** |
| pyfenn/fenn | [fenn#220](https://github.com/pyfenn/fenn/issues/220) | Python ML feature | Medium-High | Portfolio value | 8-16 hours | Scikit-learn-style perceptron API delegates training to existing trainers | Assigned to another contributor; new API requires maintainer collaboration | **No - assigned** |
| Kubeflow MCP Server | [mcp-server#53](https://github.com/kubeflow/mcp-server/issues/53) | README badges/video | Low | Minor portfolio value | 1-2 hours | Requested assets and badges render and point to valid targets | Existing comments and externally hosted video dependency | Defer |
| mcp-observatory | [mcp-observatory#230](https://github.com/KryptosAI/mcp-observatory/issues/230) | GHCR workflow | Medium | Portfolio value | 3-6 hours after dependency lands | Image builds, publishes, and uses requested tags | Root Dockerfile from #227 is still a prerequisite | **No - dependency blocked** |

## Rejected Search Noise

- High-volume contest repositories with thousands of near-identical component
  issues were excluded because they create duplicate-work and spam risk.
- Trivia/data-entry issues were excluded because they add little evidence for
  Python automation, CI/CD, or documentation services.
- Security, credential, exploit, crypto, and fake-engagement work remains outside
  scope regardless of stated payout.

## Selected Action

Issue `kubeflow/mcp-server#54` was selected. The target repository is
`kubeflow/website`, where no open pull request matching "MCP Server" was found at
the final duplicate check. A DCO-signed local commit and full Hugo build are
prepared for submission.
