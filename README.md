# CS 1101 Unit 7 — Python Strings and File Handling

This repository contains the full Python code supplied for the Unit 7 assignment, plus sample output.

## Questions covered

1. **String processing:** trims leading/trailing whitespace with `strip()`, converts text to lowercase with `lower()`, replaces `speaker` with `presenter`, normalizes repeated whitespace with `split()` and `join()`, and formats the result with `title()`.
2. **File handling:** writes feedback using `w`, reads it using `r`, and appends another entry using `a`.
3. **Exception handling:** handles `FileNotFoundError` and `PermissionError`; the `finally` block always prints a completion message.
4. **Summary:** counts feedback entries and counts entries that contain “great”, case-insensitively, then writes the result to `summary.txt`.

## Requirements

- Python 3
- No third-party packages required

## Run

From this repository directory, run:

```bash
python workshop_feedback_manager.py
```

The program creates or overwrites `feedback.txt` and `summary.txt` in the current working directory.

## Repository files

- `workshop_feedback_manager.py` — complete source code for Questions 1–4.
- `sample_output.txt` — expected output for the supplied code.

## Submission reminder

The assignment instructions say that the complete source code must also be included in the submitted document. This repository link is an additional reference and does not replace the code in your Word document.
