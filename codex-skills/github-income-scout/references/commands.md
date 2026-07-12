# GitHub CLI Commands

Use these commands when the GitHub Income Scout project scripts are unavailable.
Require an authenticated `gh` session for higher rate limits and private account
context, but never print or request the token itself.

## Search

Find recent unassigned starter issues:

```powershell
gh search issues --state open --no-assignee --label "good first issue" `
  --sort updated --order desc --limit 50 `
  --json repository,number,title,url,labels,assignees,commentsCount,updatedAt
```

Search `help wanted` separately because GitHub label filters are additive rather
than OR expressions:

```powershell
gh search issues --state open --no-assignee --label "help wanted" `
  --sort updated --order desc --limit 50 `
  --json repository,number,title,url,labels,assignees,commentsCount,updatedAt
```

Search explicit bounty labels, then manually verify whether the reward was
successfully funded and whether payout terms are cash, platform credit, or a
token:

```powershell
gh search issues --state open --no-assignee --label bounty `
  --sort updated --order desc --limit 100 `
  --json repository,number,title,url,labels,assignees,commentsCount,updatedAt
```

## Candidate Precheck

Read the full issue, including assignment and comments:

```powershell
gh issue view ISSUE --repo OWNER/REPO `
  --json title,body,state,assignees,comments,labels,url,updatedAt
```

Search open pull requests using both the issue number and key title terms:

```powershell
gh pr list --repo OWNER/REPO --state open --search "ISSUE OR key terms" `
  --json number,title,url,author,headRefName
```

Inspect repository activity and licensing before recommending implementation:

```powershell
gh repo view OWNER/REPO `
  --json description,defaultBranchRef,licenseInfo,stargazerCount,forkCount,updatedAt,url
```

## Decision Gate

Reject or defer a candidate when any of these are true:

- another contributor is assigned or has received permission to proceed
- an open pull request already covers the issue
- the reward command failed, funding is pending, or payment is only speculative credit
- acceptance depends on missing upstream work
- the repository has no usable license or no credible maintainer activity
- the task requires exploits, credentials, fake engagement, payment bypasses, or platform abuse

Only move to implementation after recording the acceptance standard, verification
command, expected time, likely value, and principal failure risk.
