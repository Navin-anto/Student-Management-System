from mysql import connector as c
from mysql.connector import Error

def get_connection():
    try:
        return c.connect(
            host = "localhost",
            user = "root",
            password = "YOUR_SQL_PASSWORD",
            database = "student_db"
        )
    except Error:
        print("Database connection failed...")