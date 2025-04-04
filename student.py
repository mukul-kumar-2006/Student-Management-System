import mysql.connector
from database import connect

# Create operation (Add student)
def add_student(name, age, course):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    conn.commit()
    print("Student added successfully!")
    conn.close()

# Read operation (View students)
def view_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)
    conn.close()

# Update operation (Update student details)
def update_student(student_id, name, age, course):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE students SET name=%s, age=%s, course=%s WHERE student_id=%s"
    values = (name, age, course, student_id)
    cursor.execute(query, values)
    conn.commit()
    print("Student updated successfully!")
    conn.close()

# Delete operation (Delete student)
def delete_student(student_id):
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM students WHERE student_id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print("Student deleted successfully!")
    conn.close()
