param(
    [string]$RepoName = "github-income-scout",
    [string]$Description = "Find and score low-risk GitHub issue opportunities for practical open-source contribution.",
    [switch]$Private
)

$ErrorActionPreference = "Stop"

function Require-Command {
    param([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command not found: $Name"
    }
}

Require-Command git
Require-Command gh

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $root

if (-not (Test-Path ".git")) {
    git init
}

git add .
if (-not (git diff --cached --quiet)) {
    git commit -m "Initial GitHub Income Scout MVP"
}

$visibility = if ($Private) { "--private" } else { "--public" }
$existing = gh repo view $RepoName --json name --jq .name 2>$null
if (-not $existing) {
    gh repo create $RepoName $visibility --description $Description --source . --remote origin --push
} else {
    if (-not (git remote get-url origin 2>$null)) {
        $owner = gh api user --jq .login
        git remote add origin "https://github.com/$owner/$RepoName.git"
    }
    git branch -M main
    git push -u origin main
}

Write-Host "Published repository: $RepoName"

