param(
    [string]$RepoName = "github-income-scout",
    [string]$Description = "Find and score low-risk GitHub issue opportunities for practical open-source contribution.",
    [string]$SourceDir = "",
    [string]$CommitMessage = "Publish repository contents",
    [switch]$Private
)

$ErrorActionPreference = "Stop"

function Test-Command {
    param([string]$Name)
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Invoke-GitHubApi {
    param(
        [string]$Method,
        [string]$Path,
        [object]$Body = $null
    )

    if (-not $env:GITHUB_TOKEN) {
        throw "GITHUB_TOKEN is not set. Install/login gh, or set a token with repo creation permissions."
    }

    $headers = @{
        "Accept" = "application/vnd.github+json"
        "Authorization" = "Bearer $env:GITHUB_TOKEN"
        "X-GitHub-Api-Version" = "2022-11-28"
        "User-Agent" = "github-income-scout-publisher"
    }

    $uri = "https://api.github.com$Path"
    if ($null -eq $Body) {
        return Invoke-RestMethod -Method $Method -Uri $uri -Headers $headers
    }

    $json = $Body | ConvertTo-Json -Depth 8
    return Invoke-RestMethod -Method $Method -Uri $uri -Headers $headers -ContentType "application/json" -Body $json
}

function Get-GitHubOwner {
    if (Test-Command gh) {
        $owner = gh api user --jq .login 2>$null
        if ($LASTEXITCODE -eq 0 -and $owner) {
            return $owner.Trim()
        }
    }

    $user = Invoke-GitHubApi -Method "Get" -Path "/user"
    return $user.login
}

function Ensure-GitHubRepository {
    param(
        [string]$Owner,
        [string]$Name,
        [string]$RepoDescription,
        [bool]$IsPrivate
    )

    if (Test-Command gh) {
        $existing = gh repo view "$Owner/$Name" --json name --jq .name 2>$null
        if ($LASTEXITCODE -eq 0 -and $existing) {
            return
        }

        $visibility = if ($IsPrivate) { "--private" } else { "--public" }
        gh repo create "$Owner/$Name" $visibility --description $RepoDescription
        if ($LASTEXITCODE -ne 0) {
            throw "gh failed to create repository $Owner/$Name"
        }
        return
    }

    try {
        Invoke-GitHubApi -Method "Get" -Path "/repos/$Owner/$Name" | Out-Null
        return
    } catch {
        $status = $_.Exception.Response.StatusCode.value__
        if ($status -ne 404) {
            throw
        }
    }

    $body = @{
        name = $Name
        description = $RepoDescription
        private = $IsPrivate
        auto_init = $false
        has_issues = $true
        has_projects = $false
        has_wiki = $false
    }
    Invoke-GitHubApi -Method "Post" -Path "/user/repos" -Body $body | Out-Null
}

function Invoke-GitPush {
    param(
        [bool]$UseToken
    )

    git branch -M main
    if ($UseToken) {
        git -c "http.https://github.com/.extraheader=AUTHORIZATION: bearer $env:GITHUB_TOKEN" push -u origin main
    } else {
        git push -u origin main
    }

    if ($LASTEXITCODE -ne 0) {
        throw "git push failed"
    }
}

$root = if ($SourceDir) {
    Resolve-Path $SourceDir
} else {
    Resolve-Path (Join-Path $PSScriptRoot "..")
}

Set-Location $root

if (-not (Test-Command git)) {
    throw "Required command not found: git"
}

$hasGh = Test-Command gh
$hasToken = [bool]$env:GITHUB_TOKEN
if (-not $hasGh -and -not $hasToken) {
    throw "No GitHub publish path available. Install/login gh, or set GITHUB_TOKEN with repo creation permissions."
}

if (-not (Test-Path ".git")) {
    git init
}

git add .
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m $CommitMessage
}

$owner = Get-GitHubOwner
Ensure-GitHubRepository -Owner $owner -Name $RepoName -RepoDescription $Description -IsPrivate ([bool]$Private)

$remoteUrl = "https://github.com/$owner/$RepoName.git"
$currentRemote = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0 -or -not $currentRemote) {
    git remote add origin $remoteUrl
} elseif ($currentRemote -ne $remoteUrl) {
    git remote set-url origin $remoteUrl
}

Invoke-GitPush -UseToken (-not $hasGh -and $hasToken)

Write-Host "Published repository: https://github.com/$owner/$RepoName"
