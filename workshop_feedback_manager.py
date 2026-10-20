"""
CS 1101 Unit 7 Reading Assignment
Demonstrates string methods, file modes, and basic file error handling.
"""

def clean_feedback():
    """Clean a feedback string using string methods."""
    feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "
    cleaned = feedback.strip().capitalize()
    cleaned = cleaned.replace("The speaker", "The Presenter")
    cleaned = cleaned.title()
    print("Q1 - String Processing")
    print("Cleaned feedback:", cleaned)
    print()


def manage_feedback_file():
    """Write, read, and append feedback using file modes."""
    feedback_items = [
        "The workshop was informative.",
        "The presenter was great.",
        "The room was cold."
    ]

    print("Q2 - File Handling")

    # 'w' creates a file or replaces its existing contents.
    with open("feedback.txt", "w", encoding="utf-8") as file:
        for item in feedback_items:
            file.write(item + "\n")

    # 'r' opens a file for reading.
    with open("feedback.txt", "r", encoding="utf-8") as file:
        print("Initial feedback:")
        print(file.read(), end="")

    # 'a' adds new content to the end of an existing file.
    with open("feedback.txt", "a", encoding="utf-8") as file:
        file.write("The examples were great.\n")

    with open("feedback.txt", "r", encoding="utf-8") as file:
        all_feedback = file.read().splitlines()

    print("\nFeedback after appending:")
    for item in all_feedback:
        print(item)
    print()
    return all_feedback


def read_feedback_safely(filename):
    """Show how common file errors can be handled."""
    print("Q3 - File Error Handling")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
            print(contents if contents else "(The file is empty.)")
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
    except PermissionError:
        print(f"Error: permission denied when opening '{filename}'.")
    print()


def create_summary(feedback_items):
    """Write a summary file and count feedback containing 'great'."""
    great_count = sum(1 for item in feedback_items if "great" in item.lower())

    with open("summary.txt", "w", encoding="utf-8") as file:
        file.write(f"Total Feedback: {len(feedback_items)}\n")
        file.write(f"Mentions of 'Great': {great_count}\n")

    print("Q4 - Feedback Summary")
    print(f"Total Feedback: {len(feedback_items)}")
    print(f"Mentions of 'Great': {great_count}")


def main():
    clean_feedback()
    feedback_items = manage_feedback_file()
    read_feedback_safely("feedback.txt")
    create_summary(feedback_items)


if __name__ == "__main__":
    main()
