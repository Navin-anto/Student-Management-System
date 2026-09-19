from database import get_connection
from mysql.connector import Error

def add_student(name,register_no,dept,year):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        check_query = "SELECT * FROM STUDENT WHERE REGISTER_NO = %s"
        cursor.execute(check_query,(register_no,))
        if cursor.fetchone():
            print("Student already exists...")
        else:
            query = "INSERT INTO STUDENT (NAME,REGISTER_NO,DEPT,YEAR) VALUES (%s,%s,%s,%s)"
            values = (name,register_no,dept,year)
            cursor.execute(query,values)
            db.commit()
            print("Student Details Added Successfully...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def view_students():
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM STUDENT"
        cursor.execute(query)
        result = cursor.fetchall()
        for r in result:
            print(r)
    except Error:
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def search_student(register_no):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM STUDENT WHERE REGISTER_NO = %s"
        cursor.execute(query,(register_no,))
        result = cursor.fetchone()
        if result:
            print("Student Details Found Successfully...")
            print(result)
        else:
            print("Student Details Not Found...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def update_student(name,register_no,dept,year):
    db = None 
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "UPDATE STUDENT SET NAME = %s, DEPT = %s, YEAR = %s WHERE REGISTER_NO = %s"
        values = (name,dept,year,register_no)
        cursor.execute(query,values)
        db.commit()
        if cursor.rowcount > 0:
            print("Student Details Updated Successfully...")
        else:
            print("Student Details Not Found...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()    

def delete_student(register_no):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "DELETE FROM STUDENT WHERE REGISTER_NO = %s"
        cursor.execute(query,(register_no,))
        db.commit()
        if cursor.rowcount > 0:
            print("Student Details Deleted Successfully...")
        else:
            print("Student Details Not Found...")
    except Error:
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()