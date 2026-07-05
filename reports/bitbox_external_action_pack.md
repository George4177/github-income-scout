# Bitbox External Action Pack

Target issue: https://github.com/abduznik/bitbox/issues/99

Status verified on 2026-07-05:

- issue state: open
- assignees: none
- comments: 0
- open PRs checked: no `seconds_to_hms` PR found

No external action has been taken yet.

## Claim Comment Draft

Use only after user confirmation:

```text
Hi, I would like to work on this.

I plan to add `tools/seconds_to_hms.py` following the contribution guide, using stdlib only, with behavior matching the requested example:

`seconds_to_hms "3661"` -> `1:01:01`
```

## Branch Name

```text
tool/seconds-to-hms
```

## Commit Message

```text
Add seconds_to_hms tool
```

## Tool File Draft

Replace `@YOUR_GITHUB_USERNAME` before opening the PR.

```python
# tool: seconds_to_hms
# description: Converts a number of seconds to h:mm:ss format
# author: @YOUR_GITHUB_USERNAME
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
```

## Test Commands

```bash
python bitbox.py seconds_to_hms "3661"
python bitbox.py seconds_to_hms "59"
python bitbox.py seconds_to_hms "0"
python bitbox.py seconds_to_hms "-1"
python bitbox.py seconds_to_hms "abc"
```

Expected:

```text
1:01:01
0:00:59
0:00:00
Error: seconds must be non-negative
Error: seconds must be an integer
```

## PR Title

```text
[tool] seconds_to_hms
```

## PR Body

```text
## Summary

Adds the `seconds_to_hms` tool requested in #99.

## Behavior

- Converts integer seconds to `h:mm:ss`
- Pads minutes and seconds to two digits
- Returns clear error messages for missing, non-integer, or negative input

## Testing

- `python bitbox.py seconds_to_hms "3661"` -> `1:01:01`
- `python bitbox.py seconds_to_hms "59"` -> `0:00:59`
- `python bitbox.py seconds_to_hms "0"` -> `0:00:00`
- `python bitbox.py seconds_to_hms "-1"` -> `Error: seconds must be non-negative`
- `python bitbox.py seconds_to_hms "abc"` -> `Error: seconds must be an integer`

Closes #99
```

## Automated Helper

When `git` and `gh` are available locally:

```powershell
.\scripts\prepare_bitbox_pr.ps1 -GitHubUsername YOUR_GITHUB_USERNAME
```

This helper forks/clones Bitbox, creates `tools/seconds_to_hms.py`, runs the local examples, commits, pushes, and opens the PR.
