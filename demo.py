# demo.py
# Mini definition: A demo script runs the full system automatically, without
# waiting for user input. It is used to prove that every feature works,
# because its output can be checked after every run.

from management import StudentManagement
from student import Student


def main():
    # Create the management object that holds all students.
    system = StudentManagement()

    print("--- Adding students ---")
    # Add three students. add_student returns True if the ID was new.
    print("Added S001:", system.add_student(Student("S001", "Sajjal", "Computer Science", [85, 90, 78, 92])))
    print("Added S002:", system.add_student(Student("S002", "Ali", "Mathematics", [70, 65, 72])))
    print("Added S003:", system.add_student(Student("S003", "Ayesha", "Computer Science", [95, 92, 98])))
    # Try a duplicate ID: this must fail, because IDs must be unique.
    print("Added duplicate S001:", system.add_student(Student("S001", "Duplicate", "Physics", [50])))

    print("\n--- Listing all students ---")
    for student in system.list_students():
        print(student)

    print("\n--- Searching by ID: S002 ---")
    print(system.find_by_id("S002"))

    print("\n--- Searching by name: Sajjal ---")
    for student in system.find_by_name("Sajjal"):
        print(student)

    print("\n--- Updating marks for S002 ---")
    print("Updated:", system.update_marks("S002", [80, 85, 90]))
    print(system.find_by_id("S002"))

    print("\n--- Top student ---")
    print(system.top_student())

    print("\n--- Saving to file and loading back ---")
    system.save_to_file("students.json")
    # Load into a brand new system object, to prove the file really works.
    new_system = StudentManagement()
    print("Loaded from file:", new_system.load_from_file("students.json"))
    for student in new_system.list_students():
        print(student)

    print("\n--- Removing student S002 ---")
    print("Removed:", system.remove_student("S002"))
    for student in system.list_students():
        print(student)


if __name__ == "__main__":
    main()
