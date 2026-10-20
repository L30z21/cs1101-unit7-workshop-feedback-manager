# CS 1101 Unit 7 — Python Strings and File Handling

This project demonstrates Python string processing, file operations, basic exception handling, and a simple text-file summary for the Unit 7 reading assignment.

## Topics demonstrated

1. **String processing:** `strip()`, `capitalize()`, `replace()`, and `title()`.
2. **File modes:** `w` writes/overwrites a file, `r` reads a file, and `a` appends to a file.
3. **Error handling:** handles `FileNotFoundError` and `PermissionError`.
4. **Summary generation:** counts feedback entries and those containing the word “great”, without case sensitivity.

## Requirements

- Python 3
- No third-party packages are required.

## Run the program

From this repository's directory, run:

```bash
python workshop_feedback_manager.py
```

The program creates or updates `feedback.txt` and `summary.txt` in the current working directory.

## Files

- `workshop_feedback_manager.py` — complete source code.
- `sample_output.txt` — example terminal output.
- `feedback.txt` — generated feedback file.
- `summary.txt` — generated summary file.

The generated files are created when the program runs; they do not need to exist beforehand.

## Note for submission

The repository is a reference to the project. Include the complete source code in the assignment document as required by the assignment instructions, even when providing this GitHub link.
