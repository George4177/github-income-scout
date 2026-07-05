param(
    [Parameter(Mandatory = $true)]
    [string]$GitHubUsername,
    [string]$WorkDir = ".worktrees"
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

New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null
Set-Location $WorkDir

if (-not (Test-Path "bitbox")) {
    gh repo fork abduznik/bitbox --clone --remote
}

Set-Location "bitbox"
git fetch upstream
git checkout main
git pull upstream main

$branch = "tool/seconds-to-hms"
git checkout -B $branch

$toolPath = Join-Path "tools" "seconds_to_hms.py"
@"
# tool: seconds_to_hms
# description: Converts a number of seconds to h:mm:ss format
# author: @$GitHubUsername
# example: seconds_to_hms "3661" -> "1:01:01"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: expected exactly one argument: seconds"

    raw_seconds = str(args[0]).strip()
    try:
        total_seconds = int(raw_seconds)
    except ValueError:
        return "Error: seconds must be an integer"

    if total_seconds < 0:
        return "Error: seconds must be non-negative"

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02d}:{seconds:02d}"
"@ | Set-Content -Encoding UTF8 -Path $toolPath

python bitbox.py seconds_to_hms "3661"
python bitbox.py seconds_to_hms "59"
python bitbox.py seconds_to_hms "0"
python bitbox.py seconds_to_hms "-1"
python bitbox.py seconds_to_hms "abc"

git add $toolPath
git commit -m "Add seconds_to_hms tool"
git push -u origin $branch

gh pr create `
    --repo abduznik/bitbox `
    --title "[tool] seconds_to_hms" `
    --body "## Summary

Adds the seconds_to_hms tool requested in #99.

## Behavior

- Converts integer seconds to h:mm:ss
- Pads minutes and seconds to two digits
- Returns clear error messages for missing, non-integer, or negative input

## Testing

- python bitbox.py seconds_to_hms `"3661`" -> 1:01:01
- python bitbox.py seconds_to_hms `"59`" -> 0:00:59
- python bitbox.py seconds_to_hms `"0`" -> 0:00:00
- python bitbox.py seconds_to_hms `"-1`" -> Error: seconds must be non-negative
- python bitbox.py seconds_to_hms `"abc`" -> Error: seconds must be an integer

Closes #99"

