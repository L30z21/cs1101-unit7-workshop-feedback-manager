def clean_feedback(message):
    s = message.strip().lower()
    s = s.replace("speaker", "presenter")
    s = " ".join(s.split())
    return s.title()


# Question 1
raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "
cleaned_feedback = clean_feedback(raw_feedback)

print(f"Cleaned feedback: {cleaned_feedback}")


# Question 2
feedback_list = [
    "The presenter was great.",
    "The workshop was informative.",
    "The room was comfortable."
]

with open("feedback.txt", "w", encoding="utf-8") as file:
    for feedback in feedback_list:
        file.write(feedback + "\n")

print("\nInitial feedback:")
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

with open("feedback.txt", "a", encoding="utf-8") as file:
    file.write("The examples were great.\n")

print("\nUpdated feedback:")
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# Question 3
print("\nException handling:")
try:
    with open("feedback.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")
except PermissionError:
    print("Permission denied. Close the file and try again.")
finally:
    print("Operation completed.")


# Question 4
with open("feedback.txt", "r", encoding="utf-8") as file:
    feedback_lines = file.readlines()

total_feedback = len(feedback_lines)
great_mentions = sum(
    1 for line in feedback_lines
    if "great" in line.lower()
)

summary = (
    "=== Workshop Feedback Summary ===\n"
    f"Total Feedback: {total_feedback}\n"
    f"Mentions of 'Great': {great_mentions}\n"
)

with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("\n" + summary, end="")
