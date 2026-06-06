
students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    grade = input("Enter Student Grade: ")
    students[student_id] = {"Name": name, "Age": age, "Grade": grade}
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
    else:
        for sid, info in students.items():
            print(f"ID: {sid}, Name: {info['Name']}, Age: {info['Age']}, Grade: {info['Grade']}")
        print()

def search_student():
    sid = input("Enter Student ID to search: ")
    if sid in students:
        print(f"Found: {students[sid]}\n")
    else:
        print("Student not found.\n")

def update_student():
    sid = input("Enter Student ID to update: ")
    if sid in students:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        grade = input("Enter new grade: ")
        students[sid] = {"Name": name, "Age": age, "Grade": grade}
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    if sid in students:
        del students[sid]
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
