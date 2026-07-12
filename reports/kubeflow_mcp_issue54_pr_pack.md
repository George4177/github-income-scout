# Kubeflow MCP Server Issue #54 PR Pack

Date: 2026-07-12

## Scope

- Issue: [kubeflow/mcp-server#54](https://github.com/kubeflow/mcp-server/issues/54)
- Target repository: [kubeflow/website](https://github.com/kubeflow/website)
- Local checkout: `D:/乔治/Github/kubeflow-website-54`
- Branch: `docs/add-kubeflow-mcp-server`
- Commit: `68fee1e docs: add Kubeflow MCP Server subproject`
- DCO: commit includes `Signed-off-by` using the account's GitHub noreply address

## Files

- `content/en/docs/components/mcp-server/_index.md`
- `content/en/docs/components/mcp-server/overview.md`
- `content/en/docs/components/mcp-server/getting-started.md`
- `content/en/docs/components/mcp-server/github.md`

## Acceptance Mapping

- Kubeflow Subprojects: adds a weighted MCP Server section to the generated menu.
- Overview: explains the MCP integration, supported workflow areas, and mutation safeguards.
- Getting Started: includes source installation, server startup, authentication guidance, and one client example.
- GitHub Repository: adds an external-link navigation item using the existing site pattern.
- Duplicate check: no matching open PR was found in `kubeflow/website` immediately before commit.

## Verification

- `git diff --check`: passed.
- Hugo Extended `0.124.1`: downloaded as a portable tool, matching the repository's documented version.
- Docsy submodule: checked out at repository-pinned commit `5597d435dc74ce68240e0c3871addf24567493b0`.
- `hugo --gc --minify --destination public-test`: passed; only existing remote-resource warnings were reported.
- Generated navigation was inspected and contains Overview, Getting Started, and GitHub Repository.

## PR Description

```markdown
## Summary

- add Kubeflow MCP Server to the Kubeflow Subprojects navigation
- add concise Overview and Getting Started pages based on the project's current README
- link the upstream GitHub repository using the existing external-navigation pattern

## Why

Kubeflow MCP Server is an official subproject with its own repository and KEP,
but it is currently missing from the Kubeflow website's subproject navigation.
This gives users a discoverable entry point without duplicating the full upstream
reference documentation.

Closes kubeflow/mcp-server#54.

## Verification

- `git diff --check`
- Hugo Extended 0.124.1 full site build with the pinned Docsy submodule
- inspected generated MCP Server section navigation and pages
```

## Submission State

The local contribution is complete. Fork creation and push are pending recovery
of the intermittent GitHub API connection. No bounty or payment claim is involved.
