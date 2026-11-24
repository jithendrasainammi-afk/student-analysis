# 🎓 Student Performance Analysis System

> A menu-driven Python console application that automates recording student marks, calculating averages, assigning grades and identifying weak performance areas.

**Bennett University** · School of Computer Science Engineering and Technology
**Course:** Computational Thinking and Programming (2026CSAE100) · **Academic Year:** 2026–27

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Libraries](https://img.shields.io/badge/Libraries-standard%20library%20only-green) ![Status](https://img.shields.io/badge/Status-Working-brightgreen)

---

## 👥 Project Team

| # | Name | Enrollment No. | Batch / Section | Role |
|---|------|----------------|-----------------|------|
| 1 | Jithendra Sai | S26CSEU1856 | 53 | Team Lead |
| 2 | Prince Kumar | S26CSEU1841 | 53 | Team Member |
| 3 | Priyanshu Kumar | S26CSEU1840 | 53 | Team Member |
| 4 | Sai Charan | S26CSEU1920 | 55 | Team Member |

---

## 📌 Problem Statement

Manually tracking student marks, calculating subject averages, assigning grades and spotting weak academic areas is tedious, time-consuming and prone to calculation errors. Teachers, instructors and academic administrators handling large cohorts face this problem daily.

This project automates performance evaluation, saves administrative time, gives instant insight into student progress and helps educators quickly find students who need extra support.

## 🎯 Objectives

1. Maintain and manage marks for multiple students across various subjects.
2. Calculate subject-wise and student-wise averages automatically.
3. Assign letter grades based on defined percentage thresholds.
4. Identify the highest and lowest performers in the class.
5. Generate clear student-level and class-level performance summaries.

## 🧩 Modules

| # | Module | Description |
|---|--------|-------------|
| 1 | Student Record Module | Inputs and stores names, roll numbers and marks (with validation) |
| 2 | Calculation Module | Computes totals, percentages and averages |
| 3 | Grading Module | Assigns letter grades from percentage thresholds |
| 4 | Performance Analysis Module | Finds top/low performers and weak subjects |
| 5 | Summary & Report Module | Produces the grade sheet and class summary |

## 📝 Student Record Module *(by Jithendra Sai)*

- Collects the number of students (1–60) and subjects (1–8), plus subject names.
- Takes roll number, name and marks for each student.
- **Input validation:** text, negative values and marks above 100 are rejected and the user is re-prompted.
- Rejects duplicate roll numbers and empty names.
- Stores records in memory as a **list of dictionaries**: `{"roll": ..., "name": ..., "marks": [...]}`.

---
## 🧮 Calculation & Grading Modules *(by Prince Kumar)*

### Formulas

| Quantity | Formula |
|----------|---------|
| Total | sum of marks across all subjects |
| Percentage | `total / number_of_subjects` (each subject is out of 100) |
| Subject average | sum of that subject's marks for all students ÷ number of students |
| Class average | mean of all student percentages |

### Grading Scale

| Percentage | Grade |
|-----------|-------|
| 90 and above | **A** |
| 75 – 89.99 | **B** |
| 60 – 74.99 | **C** |
| 40 – 59.99 | **D** |
| Below 40 | **F** |

Grades are assigned in `assign_grade()` using an `if-elif-else` chain. Thresholds can be changed in that one function.

### Python Concepts Used

| Concept | Where it is used |
|---------|------------------|
| Variables & data types | Names, roll numbers, marks, totals, percentages |
| Conditional statements | `if-elif-else` grading |
| Loops | `for` / `while` loops over students, subjects and input prompts |
| Lists & dictionaries | Student records and marks |
| Functions | Grade calculation, input, reporting |
| File handling | Saving/loading CSV |
| Exception handling | `try-except` around numeric input |
| Libraries | Built-in `csv` and `os` modules |

---
⚙️ Installation & Usage (by Priyanshu Kumar)
Requirements
Python 3.8 or newer
No external packages (uses only the standard library, no pip install needed)
Run the Program
bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python student_analysis.py

VS Code users: run it in the Terminal (or ▷ → Run Python File), not the Output tab, because the Output tab cannot accept keyboard input.

Main Menu
============================================
     STUDENT PERFORMANCE ANALYSIS SYSTEM
============================================
  1. Add student records
  2. View grade sheet
  3. Class performance analysis
  4. Save records to CSV file
  5. Load records from CSV file
  6. Exit
============================================
Option	What it does
1	Enter students, subjects and marks (validated)
2	Show the grade sheet with total, % and grade
3	Show class analysis and weak subjects
4	Save all records to students.csv
5	Load records from students.csv
6	Exit
💾 File Handling (CSV)

Records are saved as students.csv:

csv
roll,name,Maths,Physics,Programming
101,Aarav Sharma,92.0,88.0,95.0
102,Diya Patel,78.0,72.0,85.0
103,Rohan Mehta,65.0,58.0,70.0
104,Sneha Reddy,45.0,52.0,60.0
105,Karan Singh,35.0,28.0,42.0
If students.csv does not exist when loading, an empty one is created automatically.
Invalid or malformed rows are skipped with a message showing the line number.
## 📊 Performance Analysis Module *(by Sai Charan)*

The analysis engine processes scores to compute aggregates and flag problem areas:

- **Highest / lowest performer** by percentage
- **Class average** and **subject-wise averages**
- **Weak subjects:** any subject whose class average is below 60
- **Extra support list:** students scoring below 40%
- **Grade distribution** across A–F

### Sample Output (5 students, 3 subjects)

**Grade Sheet**
```
Roll  Name           Maths  Physics  Program   Total      %  Grade
101   Aarav Sharma      92       88       95     275   91.7      A
102   Diya Patel        78       72       85     235   78.3      B
103   Rohan Mehta       65       58       70     193   64.3      C
104   Sneha Reddy       45       52       60     157   52.3      D
105   Karan Singh       35       28       42     105   35.0      F
```

**Class Analysis**
```
Total students     : 5
Class average      : 64.3%
Highest performer  : Aarav Sharma (91.7%)
Lowest performer   : Karan Singh (35.0%)

Subject-wise class average:
  Maths           63.0
  Physics         59.6  <-- weak subject
  Programming     70.4

Students needing extra support (below 40%):
  Karan Singh
Weak subjects: Physics
```

## 🧪 Testing

| # | Test Input | Expected Output | Result |
|---|-----------|-----------------|--------|
| 1 | Normal marks (75, 80, 85) | Correct total, percentage, Grade B | ✅ Pass |
| 2 | Boundary marks (39 or 100) | Correct boundary grade | ✅ Pass |
| 3 | Invalid input (text / negative) | Error message and re-prompt | ✅ Pass |
| 4 | Empty student record set | Warning to add records first | ✅ Pass |
| 5 | Missing CSV file on load | New file created automatically | ✅ Pass |

## 🧗 Challenges & Learnings

- **Challenge:** handling incorrect inputs (letters instead of numbers) and managing nested data for multiple subjects per student.
- **Solution:** `try-except` blocks around every input loop, and dictionaries for clean record lookup.
- **Learnings:** modular programming, CSV file I/O, defensive programming and collaborative Git workflow.

## 🚀 Future Improvements

- GUI using **Tkinter** for easier navigation
- Charts and progress curves using **Matplotlib**

## 📚 References

1. Python Software Foundation Documentation: https://docs.python.org
2. Bennett University course lecture notes and lab manuals
3. Online Python references for file handling

## 📄 License

This project was developed for academic purposes at Bennett University.
