Task 1 — Data Parsing & Profile Cleaning (5 marks)
You are given the following raw student data. Notice that the names have inconsistent spacing and casing, roll numbers are stored as strings, and marks are stored as a single comma-separated string rather than a list.

raw_students = [
{"name": " ayesha SHARMA ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
{"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
{"name": " Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
{"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
{"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
Requirements:

Loop through raw_students and for each student, produce a cleaned version where:

name has leading/trailing whitespace removed and is converted to Title Case.
roll is converted from a string to an integer.
marks_str is split on ", " and each element is converted to an integer, producing a marks list.
For each cleaned student, verify the name is valid: check that every word in the name contains only alphabetic characters. Print "✓ Valid name" or "✗ Invalid name" next to each student.

Print a formatted profile card for each cleaned student using f-strings:

================================
Student : Ayesha Sharma
Roll No : 101
Marks : [88, 72, 95, 60, 78]
After processing all students, print the name in ALL CAPS and lowercase for the student with roll number 103.

Why this matters: Raw data from forms, spreadsheets, or APIs is almost never clean. Parsing and normalising it is one of the most common real-world programming tasks.