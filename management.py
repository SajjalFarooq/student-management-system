# management.py
# Mini definition: A management class holds a collection of objects and
# provides the full operations on them: create, read, update and delete
# (often called CRUD), plus search and reporting. It does not store data
# in the Student objects themselves; it manages the whole list.

import json
from student import Student


class StudentManagement:
    """A full student management system, with file storage."""

    def __init__(self):
        # students is a list that holds all Student objects in the system.
        self.students = []

    def add_student(self, student):
        # Check first: a student_id must be unique, so duplicates are rejected.
        if self.find_by_id(student.student_id) is not None:
            return False
        self.students.append(student)
        return True

    def remove_student(self, student_id):
        # Find the student, then remove that exact object from the list.
        student = self.find_by_id(student_id)
        if student is None:
            return False
        self.students.remove(student)
        return True

    def update_marks(self, student_id, new_marks):
        # Update only the marks of the matching student, nothing else changes.
        student = self.find_by_id(student_id)
        if student is None:
            return False
        student.marks = new_marks
        return True

    def find_by_id(self, student_id):
        # Search by id: return the matching Student, or None if not found.
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_by_name(self, name):
        # Search by name: return a list, because more than one student
        # could have a similar name. The search is case-insensitive.
        return [s for s in self.students if name.lower() in s.name.lower()]

    def list_students(self):
        # Return a copy of the list, so outside code cannot change it by mistake.
        return list(self.students)

    def top_student(self):
        # max() with a key finds the student with the highest average.
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())

    def save_to_file(self, filename="students.json"):
        # Convert every Student to a dictionary, then save the list as JSON.
        # JSON is a plain text format, so the data survives after the program ends.
        data = [student.to_dict() for student in self.students]
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
        return True

    def load_from_file(self, filename="students.json"):
        # Load saved data back: if the file does not exist yet, start empty
        # instead of crashing. This is why try/except is used here.
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return False
        # Rebuild Student objects from the saved dictionaries.
        self.students = [Student.from_dict(item) for item in data]
        return True
