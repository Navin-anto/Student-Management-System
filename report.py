from database import get_connection
from mysql.connector import Error

def student_mark_report(register_no):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = " SELECT S.NAME,SUB.SNAME, M.IMARK, M.EMARK,M.TMARK FROM STUDENT S JOIN MARK M ON S.REGISTER_NO = M.REGISTER_NO JOIN SUBJECT SUB ON M.SCODE = SUB.SCODE WHERE S.REGISTER_NO = %s"
        cursor.execute(query,(register_no,))
        result = cursor.fetchall()
        if result:
            print("Register No. :",register_no)
            print("Name :",result[0][0])
            print("-----------------------------------------------------------------")
            print("  Subject        |     Internal     |     Exam       |     Total")
            print("-----------------------------------------------------------------")
            for r in result:
                print(r[1],"   ",r[2],"         ",r[3],"        ",r[4])
        else:
            print("Student or marks not found...")
    except Error:
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def class_performance_report():
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = " SELECT S.REGISTER_NO,S.NAME,AVG(M.TMARK) FROM STUDENT S JOIN MARK M ON S.REGISTER_NO = M.REGISTER_NO GROUP BY S.REGISTER_NO,S.NAME ORDER BY AVG(M.TMARK) DESC"
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print("-----------------------------------------------------")
            print("  Register No.   |       Name     |    Average")
            print("-----------------------------------------------------")
            for r in result:
                print(r[0],"    ",r[1],"        ",round(r[2],2))
        else:
            print("There are no students in the class")
    except Error:
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def subject_performance_report():
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "SELECT SUB.SCODE,SUB.SNAME,AVG(M.TMARK) FROM SUBJECT SUB JOIN MARK M ON SUB.SCODE = M.SCODE GROUP BY SUB.SCODE,SUB.SNAME ORDER BY AVG(M.TMARK) DESC"
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print("-----------------------------------------------------------")
            print("  Subject Code  |        Subject Name       |     Average") 
            print("-----------------------------------------------------------")
            for r in result:
                print(r[0],"    ",r[1],"        ",round(r[2],2))
        else:
            print("There are no subjects")
    except Error:
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def top_performers(no):
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()
        query = "SELECT S.REGISTER_NO,S.NAME,AVG(M.TMARK) FROM STUDENT S JOIN MARK M ON S.REGISTER_NO = M.REGISTER_NO GROUP BY S.REGISTER_NO,S.NAME ORDER BY AVG(M.TMARK) DESC LIMIT %s"
        cursor.execute(query,(no,))
        result = cursor.fetchall()
        if result:
            print("----------------------------------------------------------")
            print("Rank |    Register No.   |     Name     |    Average")
            print("----------------------------------------------------------")
            for i,r in enumerate(result,start=1):
                print(i,"      ",r[0],"   ",r[1],"      ",r[2])
        else:
            print("Student or marks not found...")
    except Error:
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()