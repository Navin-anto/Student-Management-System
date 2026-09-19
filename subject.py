from database import get_connection
from mysql.connector import Error

def add_subject(sname,scode):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        check_query = "SELECT * FROM SUBJECT WHERE SCODE = %s"
        cursor.execute(check_query,(scode,))
        if cursor.fetchone():
            print("Subject already exists...")
        else:  
            query = "INSERT INTO SUBJECT (SNAME,SCODE) VALUES (%s,%s)"
            values = (sname,scode)
            cursor.execute(query,values)
            db.commit()
            print("Subject Details Added Successfully...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def view_subject():
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM SUBJECT"
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

def update_subject(sname,scode):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "UPDATE SUBJECT SET SNAME = %s WHERE SCODE = %s"
        values = (sname,scode)
        cursor.execute(query,values)
        db.commit()
        if cursor.rowcount > 0:
            print("Subject Details Updated Successfully...")
        else:
            print("Subject not Found...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def delete_subject(scode):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "DELETE FROM SUBJECT WHERE SCODE = %s"
        values = (scode,)
        cursor.execute(query,values)
        db.commit()
        if cursor.rowcount > 0:
            print("Subject Details Deleted Successfully...")
        else:
            print("Subject not Found...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()