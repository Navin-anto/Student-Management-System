from database import get_connection
from mysql.connector import Error

def calculate_performance(register_no):
    db = None
    cursor = None
    try :
        db = get_connection()
        cursor = db.cursor()
        check_query = "SELECT * FROM STUDENT WHERE REGISTER_NO = %s"
        cursor.execute(check_query,(register_no,))
        if not cursor.fetchone():
            print("Student doesn't exist...")
            return
    
        query = "SELECT SUM(TMARK), AVG(TMARK), MAX(TMARK), MIN(TMARK) FROM MARK WHERE REGISTER_NO = %s"
        cursor.execute(query,(register_no,))
        result = cursor.fetchone()
        if result[0] is not None:
            print("Register Number :",register_no)
            print("Total Marks :",result[0])
            print("Average Marks :",result[1])
            print("Highest Mark :",result[2])
            print("Lowest Mark :",result[3])
            pass_query = "SELECT COUNT(*) FROM MARK WHERE REGISTER_NO = %s AND TMARK < 50"
            cursor.execute(pass_query,(register_no,))
            pass_result = cursor.fetchone()
            if pass_result[0] > 0:
                print("Result = FAIL")
                print("Grade = F")
            else:
                print("Result = PASS")
                if result[1] >= 90:
                    print("Grade = A+")
                elif result[1] >= 80:
                    print("Grade = A")
                elif result[1] >= 70:
                    print("Grade = B")
                elif result[1] >= 60:
                    print("Grade = C")
                else:
                    print("Grade = D")        
        else:
            print("Student exists, but no marks found...")
    except Error:
        print("Database error...")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()