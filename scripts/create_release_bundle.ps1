param(
    [string]$Version = "v0.1.0",
    [string]$OutputDir = "dist"
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$outputPath = Join-Path $root $OutputDir
$bundleName = "github-income-scout-$Version.zip"
$bundlePath = Join-Path $outputPath $bundleName
$stagingPath = Join-Path $outputPath "release-staging"

if (-not (Test-Path $outputPath)) {
    New-Item -ItemType Directory -Path $outputPath | Out-Null
}

if (Test-Path $stagingPath) {
    Remove-Item -LiteralPath $stagingPath -Recurse -Force
}

if (Test-Path $bundlePath) {
    Remove-Item -LiteralPath $bundlePath -Force
}

New-Item -ItemType Directory -Path $stagingPath | Out-Null

$includePaths = @(
    "README.md",
    "RELEASE_NOTES.md",
    "SERVICE_MENU.md",
    "LAUNCH_CHECKLIST.md",
    "PUBLISHING.md",
    "LICENSE",
    "pyproject.toml",
    "pricing.md",
    "roadmap.md",
    "service_offer.md",
    ".github",
    "codex-skills",
    "docs",
    "examples",
    "profile",
    "scripts",
    "site",
    "templates",
    "tests"
)

foreach ($relativePath in $includePaths) {
    $source = Join-Path $root $relativePath
    if (-not (Test-Path $source)) {
        Write-Warning "Skipping missing path: $relativePath"
        continue
    }

    $destination = Join-Path $stagingPath $relativePath
    $destinationParent = Split-Path -Parent $destination
    if (-not (Test-Path $destinationParent)) {
        New-Item -ItemType Directory -Path $destinationParent -Force | Out-Null
    }

    Copy-Item -LiteralPath $source -Destination $destination -Recurse -Force
}

$excludeDirs = @("__pycache__", ".pytest_cache")
foreach ($dir in $excludeDirs) {
    Get-ChildItem -LiteralPath $stagingPath -Directory -Recurse -Force |
        Where-Object { $_.Name -eq $dir } |
        ForEach-Object { Remove-Item -LiteralPath $_.FullName -Recurse -Force }
}

$stagedItems = Get-ChildItem -LiteralPath $stagingPath -Force
if (-not $stagedItems) {
    throw "Release staging directory is empty: $stagingPath"
}

Compress-Archive -Path (Join-Path $stagingPath "*") -DestinationPath $bundlePath -Force
if (-not (Test-Path $bundlePath)) {
    throw "Release bundle was not created: $bundlePath"
}

Remove-Item -LiteralPath $stagingPath -Recurse -Force

Write-Host "Created release bundle: $bundlePath"
