"""
Student Performance Analysis System
Bennett University | Computational Thinking and Programming (2026CSAE100)

Menu-driven console program. Uses only Python's standard library (csv, os).
Run with:  python student_analysis.py
"""

import csv
import os

CSV_FILE = "students.csv"
MAX_STUDENTS = 60
MAX_SUBJECTS = 8
SUPPORT_THRESHOLD = 40.0   # students below this % need extra support
WEAK_SUBJECT_THRESHOLD = 60.0  # subject averages below this are "weak"

# In-memory data
students = []   # list of dicts: {"roll": str, "name": str, "marks": [float, ...]}
subjects = []   # list of subject names (same order as marks)


# ---------------------------------------------------------------- input helpers
def read_int(prompt, low, high):
    """Read an integer in [low, high], re-prompting on invalid input."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("  Error: invalid input, please enter a number.")
            continue
        if low <= value <= high:
            return value
        print(f"  Error: enter a number between {low} and {high}.")


def read_marks(prompt):
    """Read marks between 0 and 100, re-prompting on invalid input."""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("  Error: invalid input, please enter a number.")
            continue
        if 0 <= value <= 100:
            return value
        print("  Error: marks must be between 0 and 100.")


def read_nonempty(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("  Error: this field cannot be empty.")


# ------------------------------------------------------------- calculation module
def total_marks(student):
    return sum(student["marks"])


def percentage(student):
    return total_marks(student) / len(student["marks"])  # each subject is out of 100


def subject_averages():
    """Average marks per subject across all students."""
    return [
        sum(s["marks"][i] for s in students) / len(students)
        for i in range(len(subjects))
    ]


# ---------------------------------------------------------------- grading module
def assign_grade(pct):
    if pct >= 90:
        return "A"
    elif pct >= 75:
        return "B"
    elif pct >= 60:
        return "C"
    elif pct >= 40:
        return "D"
    else:
        return "F"


# --------------------------------------------------------- student record module
def add_students():
    global subjects

    if students:
        print(f"\nExisting subjects will be used: {', '.join(subjects)}")
        room = MAX_STUDENTS - len(students)
        if room <= 0:
            print("  Maximum number of students reached.")
            return
        n = read_int(f"Enter number of students to add (1-{room}): ", 1, room)
    else:
        n = read_int(f"Enter number of students (1-{MAX_STUDENTS}): ", 1, MAX_STUDENTS)
        m = read_int(f"Enter number of subjects (1-{MAX_SUBJECTS}): ", 1, MAX_SUBJECTS)
        subjects = [read_nonempty(f"Name of subject {j + 1}: ") for j in range(m)]

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        while True:
            roll = read_nonempty("  Roll number: ")
            if any(s["roll"] == roll for s in students):
                print("  Error: this roll number already exists.")
            else:
                break
        name = read_nonempty("  Name: ")
        marks = [read_marks(f"  Marks in {sub} (0-100): ") for sub in subjects]
        students.append({"roll": roll, "name": name, "marks": marks})

    print(f"\n{n} student record(s) added.")


# ------------------------------------------------------- summary & report module
def show_grade_sheet():
    if not students:
        print("\n  Warning: no records found. Please add student records first.")
        return

    col = max(8, *(len(s) + 1 for s in subjects))
    name_w = max(12, max(len(s["name"]) for s in students) + 2)
    width = 6 + name_w + col * len(subjects) + 8 + 8 + 7
    line = "=" * width

    print("\n" + line)
    print("STUDENT GRADE SHEET".center(width))
    print(line)
    header = f"{'Roll':<6}{'Name':<{name_w}}"
    header += "".join(f"{sub[:col - 1]:>{col}}" for sub in subjects)
    header += f"{'Total':>8}{'%':>8}{'Grade':>7}"
    print(header)
    print("-" * width)
    for s in students:
        pct = percentage(s)
        row = f"{s['roll']:<6}{s['name']:<{name_w}}"
        row += "".join(f"{m:>{col}.0f}" if m == int(m) else f"{m:>{col}.1f}" for m in s["marks"])
        row += f"{total_marks(s):>8.0f}{pct:>8.1f}{assign_grade(pct):>7}"
        print(row)
    print(line)


def class_analysis():
    if not students:
        print("\n  Warning: no records found. Please add student records first.")
        return

    pcts = [percentage(s) for s in students]
    best = students[pcts.index(max(pcts))]
    worst = students[pcts.index(min(pcts))]
    class_avg = sum(pcts) / len(pcts)
    sub_avgs = subject_averages()
    lowest_avg = min(sub_avgs)

    line = "=" * 52
    print("\n" + line)
    print("CLASS PERFORMANCE ANALYSIS".center(52))
    print(line)
    print(f"Total students     : {len(students)}")
    print(f"Class average      : {class_avg:.1f}%")
    print(f"Highest performer  : {best['name']} ({max(pcts):.1f}%)")
    print(f"Lowest performer   : {worst['name']} ({min(pcts):.1f}%)")

    print("\nSubject-wise class average:")
    weak = []
    for sub, avg in zip(subjects, sub_avgs):
        is_weak = avg < WEAK_SUBJECT_THRESHOLD or (avg == lowest_avg and len(subjects) > 1
                                                   and avg < WEAK_SUBJECT_THRESHOLD)
        if is_weak:
            weak.append(sub)
        flag = "  <-- weak subject" if is_weak else ""
        print(f"  {sub:<14}{avg:>6.1f}{flag}")

    needs_support = [s["name"] for s, p in zip(students, pcts) if p < SUPPORT_THRESHOLD]
    print(f"\nStudents needing extra support (below {SUPPORT_THRESHOLD:.0f}%):")
    if needs_support:
        for name in needs_support:
            print(f"  {name}")
    else:
        print("  None")
    print(f"Weak subjects: {', '.join(weak) if weak else 'None'}")

    # Grade distribution (bonus summary)
    print("\nGrade distribution:")
    for g in "ABCDF":
        count = sum(1 for p in pcts if assign_grade(p) == g)
        print(f"  {g}: {'#' * count} ({count})")


# ----------------------------------------------------------------- file handling
def save_csv(filename=CSV_FILE):
    if not students:
        print("\n  Warning: no records to save. Please add student records first.")
        return
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["roll", "name"] + subjects)
            for s in students:
                writer.writerow([s["roll"], s["name"]] + s["marks"])
        print(f"\nRecords saved to '{filename}'.")
    except OSError as e:
        print(f"\n  Error: could not save file ({e}).")


def load_csv(filename=CSV_FILE):
    global subjects
    if not os.path.exists(filename):
        # Missing file: create a new, initialised one automatically
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(["roll", "name"])
            print(f"\n'{filename}' not found. A new empty file has been created.")
        except OSError as e:
            print(f"\n  Error: could not create file ({e}).")
        return

    loaded, new_subjects = [], []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if not header or len(header) < 3:
                print(f"\n'{filename}' has no student records to load.")
                return
            new_subjects = header[2:]
            for line_no, row in enumerate(reader, start=2):
                if not row:
                    continue
                try:
                    if len(row) != len(header):
                        raise ValueError("wrong number of columns")
                    marks = [float(x) for x in row[2:]]
                    if any(m < 0 or m > 100 for m in marks):
                        raise ValueError("marks out of range")
                    loaded.append({"roll": row[0], "name": row[1], "marks": marks})
                except ValueError as e:
                    print(f"  Skipped line {line_no}: {e}.")
    except OSError as e:
        print(f"\n  Error: could not read file ({e}).")
        return

    if not loaded:
        print(f"\n'{filename}' has no valid student records to load.")
        return

    subjects[:] = new_subjects
    students[:] = loaded
    print(f"\nLoaded {len(loaded)} record(s) from '{filename}'.")


# -------------------------------------------------------------------- main menu
def show_menu():
    print("\n" + "=" * 44)
    print("     STUDENT PERFORMANCE ANALYSIS SYSTEM")
    print("=" * 44)
    print("  1. Add student records")
    print("  2. View grade sheet")
    print("  3. Class performance analysis")
    print("  4. Save records to CSV file")
    print("  5. Load records from CSV file")
    print("  6. Exit")
    print("=" * 44)


def main():
    while True:
        show_menu()
        try:
            choice = input("Enter your choice (1-6): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if choice == "1":
            add_students()
        elif choice == "2":
            show_grade_sheet()
        elif choice == "3":
            class_analysis()
        elif choice == "4":
            save_csv()
        elif choice == "5":
            load_csv()
        elif choice == "6":
            print("\nThank you for using the Student Performance Analysis System. Goodbye!")
            break
        else:
            print("  Error: invalid choice, please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
