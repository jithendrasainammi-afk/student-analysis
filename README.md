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
