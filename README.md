# Student Management System

A full student management system built with object-oriented programming in Python. This is a complete system, not a single example: it can add, list, search, update and remove students, calculate averages and grades, find the top student, and save data to a file so it is not lost when the program ends.

## Features

- Add a student, with a unique student ID
- List all students
- Search a student by ID
- Search students by name
- Update a student's marks
- Remove a student
- Show the top student, based on average marks
- Save students to a JSON file and load them back
- Duplicate student IDs are rejected
- Invalid input is handled, so the program does not crash

## Project structure

- `person.py` — Person base class. It stores only what every person has: a name.
- `student.py` — Student class, inherited from Person. It adds student ID, field of study and marks, and methods to calculate average and grade. It can also convert itself to and from a dictionary for file storage.
- `management.py` — StudentManagement class. It holds all students and provides the full operations: add, remove, update, search, list, top student, save and load.
- `main.py` — The full interactive system. It shows a menu, reads the user's choice, and calls the right management method, in a loop until the user chooses to save and exit.
- `demo.py` — An automated demo. It runs every feature without waiting for user input, so you can check that the whole system works.
- `README.md` — This file.

## Comments and mini definitions

Every new code type in this project is explained with a mini definition in the text above it, and with proper comments inside the code, so you can see why each piece of code is used. For example, the code explains why `__init__` runs automatically, why `self` is used, why a student ID must be unique, and why data is saved as JSON.

## How to run

### Full interactive system

```bash
python main.py
```

Then choose from the menu:

```
1. Add student
2. List all students
3. Search student by ID
4. Search student by name
5. Update student marks
6. Remove student
7. Show top student
8. Save and exit
```

Data is saved to `students.json` when you choose option 8, and loaded back automatically the next time you run the program.

### Automated demo

```bash
python demo.py
```

This runs every feature at once, without input, and prints the result of each step.

## Example output from demo.py

```
--- Adding students ---
Added S001: True
Added S002: True
Added S003: True
Added duplicate S001: False

--- Listing all students ---
ID: S001, Name: Sajjal, Field: Computer Science, Marks: [85, 90, 78, 92], Average: 86.25, Grade: B
ID: S002, Name: Ali, Field: Mathematics, Marks: [70, 65, 72], Average: 69.00, Grade: C
ID: S003, Name: Ayesha, Field: Computer Science, Marks: [95, 92, 98], Average: 95.00, Grade: A

--- Top student ---
ID: S003, Name: Ayesha, Field: Computer Science, Marks: [95, 92, 98], Average: 95.00, Grade: A
```

This output is real output from running `demo.py` before upload. GitHub itself does not run code; to run this project yourself, download it and run `python main.py` or `python demo.py` on your own computer, in VS Code, or in a terminal with Python installed.

## Requirements

- Python 3 only
- No external packages are needed. Only the Python standard library is used.
