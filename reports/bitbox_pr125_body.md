## Summary

Adds the `seconds_to_hms` tool requested in #99.

## Behavior

- Converts integer seconds to `h:mm:ss`.
- Pads minutes and seconds to two digits.
- Returns clear error messages for missing, extra, non-integer, or negative input.

## Testing

- `python bitbox.py seconds_to_hms "3661"` -> `1:01:01`
- `python bitbox.py seconds_to_hms "59"` -> `0:00:59`
- `python bitbox.py seconds_to_hms "0"` -> `0:00:00`
- `python bitbox.py seconds_to_hms "-1"` -> `Error: seconds must be non-negative`
- `python bitbox.py seconds_to_hms "abc"` -> `Error: seconds must be an integer`
- `python bitbox.py seconds_to_hms` -> `Error: expected exactly one argument: seconds`
- `python bitbox.py seconds_to_hms "1" "2"` -> `Error: expected exactly one argument: seconds`
- `python bitbox.py --list` shows `seconds_to_hms`.

Closes #99
