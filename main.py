from student import add_student, view_students, update_student, delete_student

def menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter student course: ")
        add_student(name, age, course)

    elif choice == '2':
        view_students()

    elif choice == '3':
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")
        update_student(student_id, name, age, course)

    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)

    elif choice == '5':
        print("Exiting...")
        exit()

    else:
        print("Invalid choice, please try again.")
        menu()

if __name__ == "__main__":
    menu()
