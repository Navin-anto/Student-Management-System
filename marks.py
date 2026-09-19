from database import get_connection
from mysql.connector import IntegrityError,Error

def enter_marks(register_no,scode,imark,emark,tmark):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        check_query = "SELECT * FROM MARK WHERE REGISTER_NO = %s AND SCODE = %s"
        cursor.execute(check_query,(register_no,scode))
        if cursor.fetchone():
            print("Mark already registered...")
        else:
            try:
                query = "INSERT INTO MARK (REGISTER_NO,SCODE,IMARK,EMARK,TMARK) VALUES (%s,%s,%s,%s,%s)"
                values = (register_no,scode,imark,emark,tmark)
                cursor.execute(query,values)
                db.commit()
                print("Mark Details Added Successfully...") 
            except IntegrityError:
                db.rollback()
                print("Student or Subject doesn't exist...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def view_marks():
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM MARK"
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

def update_marks(register_no,scode,imark,emark,tmark):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "UPDATE MARK SET IMARK = %s,EMARK = %s,TMARK = %s WHERE REGISTER_NO = %s AND SCODE = %s"
        values = (imark,emark,tmark,register_no,scode)
        cursor.execute(query,values)
        db.commit()
        if cursor.rowcount > 0:
            print("Mark Details Updated Successfully...")
        else:
            print("Mark not Found...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
    

def delete_marks(register_no,scode):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "DELETE FROM MARK WHERE REGISTER_NO = %s AND SCODE = %s"
        values = (register_no,scode)
        cursor.execute(query,values)
        db.commit()
        if cursor.rowcount > 0:
            print("Marks Details Deleted Successfully...")
        else:
            print("Mark not Found...")
    except Error:
        if db:
            db.rollback()
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()