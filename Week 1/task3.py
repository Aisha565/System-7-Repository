
import json
import os

FILE_NAME = "students.json"


def load_students():
    # Load existing records from the file
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the records file.")
        return []


def save_students(students):
    # Save all student records to the file
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    # Collect and validate student details
    roll_no = input("Enter roll number: ").strip()

    if any(student["roll_no"] == roll_no for student in students):
        print("This roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return

    students.append({
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("Student added successfully!")


def view_students(students):
    # Display all saved student records
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(
            f"Roll No: {student['roll_no']} | "
            f"Name: {student['name']} | "
            f"Marks: {student['marks']}"
        )


def search_student(students):
    # Search for a student using roll number
    roll_no = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student found:", student)
            return

    print("Student not found.")


def delete_student(students):
    # Delete a student using roll number
    roll_no = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Records saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
