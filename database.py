import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Apna MySQL password daalein
        database="student_management"
    )
    return conn
