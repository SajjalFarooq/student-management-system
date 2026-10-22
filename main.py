# main.py
# Mini definition: This is the entry point of the full system.
# It shows a menu, reads the user's choice, and calls the right
# StudentManagement method for that choice, in a loop until the user exits.
# Every input is checked with try/except, so a wrong input does not crash it.

from management import StudentManagement
from student import Student


def read_marks():
    # Read marks as numbers separated by spaces, for example: 85 90 78
    # int() converts each piece of text into a number.
    text = input("Enter marks separated by spaces: ")
    return [int(part) for part in text.split()]


def main():
    # Create one management object that will hold all students.
    system = StudentManagement()
    # Try to load previously saved students, if a save file already exists.
    system.load_from_file()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. List all students")
        print("3. Search student by ID")
        print("4. Search student by name")
        print("5. Update student marks")
        print("6. Remove student")
        print("7. Show top student")
        print("8. Save and exit")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            # Add: collect all fields, then add the new Student object.
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            field = input("Enter field of study: ")
            try:
                marks = read_marks()
            except ValueError:
                print("Invalid marks. Please enter numbers only.")
                continue
            student = Student(student_id, name, field, marks)
            if system.add_student(student):
                print("Student added successfully.")
            else:
                print("Error: A student with this ID already exists.")
        elif choice == "2":
            # List: print every student, using each object's __str__ method.
            if not system.list_students():
                print("No students yet.")
            for student in system.list_students():
                print(student)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            student = system.find_by_id(student_id)
            print(student if student else "Student not found.")
        elif choice == "4":
            name = input("Enter student name: ")
            results = system.find_by_name(name)
            if not results:
                print("No student found with that name.")
            for student in results:
                print(student)
        elif choice == "5":
            student_id = input("Enter student ID: ")
            try:
                marks = read_marks()
            except ValueError:
                print("Invalid marks. Please enter numbers only.")
                continue
            if system.update_marks(student_id, marks):
                print("Marks updated successfully.")
            else:
                print("Student not found.")
        elif choice == "6":
            student_id = input("Enter student ID: ")
            if system.remove_student(student_id):
                print("Student removed successfully.")
            else:
                print("Student not found.")
        elif choice == "7":
            top = system.top_student()
            print(f"Top student: {top}" if top else "No students yet.")
        elif choice == "8":
            # Save before exit, so data is not lost when the program ends.
            system.save_to_file()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    # This check means main() runs only when this file is run directly,
    # not when it is imported by another file.
    main()
