param(
    [string]$Username = "George4177",
    [string]$ProfileRepoPath = "../George4177"
)

$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$sourceReadme = Join-Path $root "profile/README.md"
$targetCandidate = Join-Path $root $ProfileRepoPath

if (-not (Test-Path $targetCandidate)) {
    New-Item -ItemType Directory -Path $targetCandidate -Force | Out-Null
}

$targetRepo = Resolve-Path $targetCandidate
$targetReadme = Join-Path $targetRepo "README.md"

if (-not (Test-Path $sourceReadme)) {
    throw "Missing profile README source: $sourceReadme"
}

Copy-Item -LiteralPath $sourceReadme -Destination $targetReadme -Force

& (Join-Path $PSScriptRoot "publish_repo.ps1") `
    -RepoName $Username `
    -Description "GitHub profile README for fixed-scope Python automation and GitHub Starter Audit services." `
    -SourceDir $targetRepo `
    -CommitMessage "Update profile service README"
