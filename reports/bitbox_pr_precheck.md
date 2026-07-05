# Bitbox PR Precheck

Candidate issue: https://github.com/abduznik/bitbox/issues/99

## What I Verified

- Repository exists: `abduznik/bitbox`
- Root files include `CONTRIBUTING.md`, `README.md`, `bitbox.py`, `template.py`, and `tools/`
- Contribution guide says to copy `template.py` into `tools/your_tool_name.py`
- Tool files must define one `run` function
- Tool files must use standard library only
- PR title format must be `[tool] your_tool_name`
- The issue is a small tool request: convert seconds to `h:mm:ss`

## Before External Action

Need user confirmation before:

- commenting to claim the issue
- forking/cloning and pushing a branch
- opening a PR

Need the GitHub username to use in the file header unless it can be safely read from the logged-in GitHub session.

## Proposed Implementation

File: `tools/seconds_to_hms.py`

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
        seconds = int(raw_seconds)
    except ValueError:
        return "Error: seconds must be an integer"

    if seconds < 0:
        return "Error: seconds must be non-negative"

    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02d}:{seconds:02d}"
```

## Local Test Commands

```bash
python bitbox.py seconds_to_hms "3661"
python bitbox.py seconds_to_hms "59"
python bitbox.py seconds_to_hms "0"
python bitbox.py seconds_to_hms "-1"
```

Expected outputs:

- `1:01:01`
- `0:00:59`
- `0:00:00`
- `Error: seconds must be non-negative`

## Draft PR Description

Title:

```text
[tool] seconds_to_hms
```

Body:

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

Closes #99
```

