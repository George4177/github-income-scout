# Publishing Checklist

Use this checklist before publishing the repository or making external GitHub moves.

## Local Checks

```powershell
C:\Users\77\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\check_all.py
```

Optional release bundle:

```powershell
.\scripts\create_release_bundle.ps1 -Version v0.1.0
```

## Repository Setup

- Create a public GitHub repository named `github-income-scout`
- Push the local files
- Enable Actions only after verifying the workflow uses the repository `GITHUB_TOKEN`
- Pin the repository on the GitHub profile
- Add a concise repo description: `Find and score low-risk GitHub issue opportunities for practical open-source contribution.`
- Keep issue forms enabled so visitors can request a Starter Audit or Custom Automation project.
- Enable GitHub Pages in repository settings. The included `Deploy GitHub Pages` workflow publishes the `site/` folder.

Automated helper when `git` and `gh` are available:

```powershell
.\scripts\publish_repo.ps1
```

## First Public Release

- Tag: `v0.1.0`
- Include: README, release notes, launch checklist, sample audit, pricing notes, service offer, static site, tests
- Use [RELEASE_NOTES.md](RELEASE_NOTES.md) as the release body.
- Use [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md) for first-week execution.
- Avoid: income guarantees, bounty guarantees, fake urgency, mass outreach

## GitHub Pages

After publishing:

1. Open repository Settings.
2. Go to Pages.
3. Choose GitHub Actions as the source.
4. Run the `Deploy GitHub Pages` workflow or push a change under `site/`.

## First Lead Channel

Use one low-pressure channel first:

- GitHub profile README
- pinned repository README
- repository issue forms
- personal website
- a single relevant community post where self-promotion is allowed

## External Action Guardrails

Confirm tool access and safety boundaries before:

- commenting on any issue
- opening or updating any PR
- applying for a bounty
- connecting payment accounts
- posting public service offers under the user's name

Current standing authorization allows low-risk GitHub publishing and PR preparation, but do not use payment information, private tokens, credentials, exploit work, fake engagement, or platform bypasses.
