# student.py
# Mini definition: Inheritance lets a child class reuse a parent class.
# Student inherits from Person, so it gets Person's name and introduce method,
# and adds its own student-specific data: student_id, field and marks.

from person import Person


class Student(Person):
    """A student, built on top of the Person base class."""

    def __init__(self, student_id, name, field, marks):
        # super() calls the parent class __init__, so name is set by Person.
        super().__init__(name)
        # student_id is unique for each student, so it is used to find a student.
        self.student_id = student_id
        self.field = field
        # marks is a list of numbers, for example [85, 90, 78, 92].
        self.marks = marks

    def average(self):
        # sum() adds all marks, len() counts them, so this is the mean mark.
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def grade(self):
        # The grade is decided from the real average, not from a single mark.
        average_marks = self.average()
        if average_marks >= 90:
            return "A"
        elif average_marks >= 75:
            return "B"
        elif average_marks >= 60:
            return "C"
        else:
            return "F"

    def __str__(self):
        # __str__ defines the readable text shown when a Student is printed.
        return (
            f"ID: {self.student_id}, Name: {self.name}, Field: {self.field}, "
            f"Marks: {self.marks}, Average: {self.average():.2f}, Grade: {self.grade()}"
        )

    def to_dict(self):
        # to_dict converts a Student into a plain dictionary, so it can be
        # saved to a JSON file. This is how data is stored between runs.
        return {
            "student_id": self.student_id,
            "name": self.name,
            "field": self.field,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data):
        # from_dict does the opposite: it rebuilds a Student from saved data.
        # @classmethod means this method belongs to the class, not one object.
        return cls(data["student_id"], data["name"], data["field"], data["marks"])
