# College Student Manager

College Student Manager is a beginner-friendly Python application designed to manage basic student information, marks, attendance, and document submission status through a simple menu-based interface.

## Overview

This project provides a simple way to maintain student records in one place. It allows the user to add, search, update, and delete student information, while also managing marks, subject-wise attendance, and required documents.

The project was created as a first-year Python project to practice fundamental programming concepts.

## Features

* Add new students
* View all students
* Search students using roll number
* Update student name or branch
* Delete student records
* Add subject-wise marks
* Manage subject-wise attendance
* Automatically calculate attendance percentage
* Track required student documents
* Mark documents as Submitted ✓ or Not Submitted ✗
* Generate a complete student report
* Simple menu-based interface

## Technologies Used

* Python
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* User Input
* Basic Data Handling

## Project Structure

```text
College-Student-Manager/
│
├── College manager.py
└── README.md
```

## Main Modules

### Student Management

The student management section allows the user to:

* Add a student
* View students
* Search for a student
* Update student information
* Delete a student

### Marks Management

Marks can be added for different subjects using the student's roll number.

Example:

```text
Mathematics : 85
Python : 91
Physics : 78
```

### Attendance Manager

Attendance is maintained separately for each subject.

The program records:

* Number of classes attended
* Number of classes missed
* Attendance percentage

Example:

```text
Subject: Python
Present: 18
Absent: 2
Attendance: 90.0%
```

### Document Manager

The program maintains a checklist of required student documents.

Each document can be marked as:

```text
✓ Submitted
✗ Not Submitted
```

The system also shows the total number of submitted documents and whether the student's document status is complete or pending.

## How to Run

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open `College manager.py`.
5. Run the Python file.
6. Select options from the menu.

## Example Menu

```text
================================
     COLLEGE STUDENT MANAGER
================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Add Marks
7. Attendance Manager
8. Document Manager
9. Student Report
10. Exit
```

## Concepts Practiced

This project helped in practicing basic Python concepts such as:

* Variables
* Strings
* Lists
* Dictionaries
* Functions
* `for` loops
* `while` loops
* `if-elif-else`
* Nested dictionaries
* User input
* Basic calculations


## License

This project was created for college project for VITYARTHI.
