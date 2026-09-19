import student as stu
import subject as sub
import marks as m
import performance as p
import report as r
import validation as v

while True:
    print("===============================================")
    print("\t STUDENT MANAGEMENT SYSTEM")
    print("===============================================\n")
    print("1. Student Management")
    print("2. Subject Management")
    print("3. Marks Management")
    print("4. Performance Analysis")
    print("5. Reports")
    print("6. Exit")
    try:
        ch = int(input("Enter your choice : "))

    # Student Management
        if ch == 1:
            while True:
                print("------------------------------")
                print("  Student Management")
                print("------------------------------")
                print("1. Add Student")
                print("2. View all Students")
                print("3. Search Student")
                print("4. Update Student")
                print("5. Delete Student")
                print("6. Exit")
                try:
                    c = int(input("Enter your choice : "))
                    if c == 1:
                        while True:
                            name = input("Enter the Student Name : ").strip()
                            register_no = input("Enter the Register Number : ").strip()
                            dept = input("Enter the Department : ").strip()
                            if name == "" or dept == "":
                                print("Field can't be empty...")
                            elif v.validate_register_no(register_no):
                                break
                        while True:
                            try:
                                year = int(input("Enter the year : "))
                                if v.validate_year(year):
                                    break
                            except ValueError:
                                print("Please enter in numbers...")
                        stu.add_student(name,register_no,dept,year)
                    elif c == 2:
                        stu.view_students()
                    elif c == 3:
                        while True:
                            register_no = input("Enter the Student Register No. to be Found : ").strip()
                            if v.validate_register_no(register_no):
                                break
                        stu.search_student(register_no)
                    elif c == 4:
                        while True:
                            register_no = input("Enter the Register Number to be Updated : ").strip()
                            name = input("Enter the Updated Student Name : ").strip()
                            dept = input("Enter the Updated Department : ").strip()
                            if name == "" or dept == "":
                                print("Field can't be empty...")
                            elif v.validate_register_no(register_no):
                                break
                        while True:
                            try:
                                year = int(input("Enter the Updated year : "))
                                if v.validate_year(year):
                                    break
                            except ValueError:
                                print("Please enter in numbers...")
                        stu.update_student(name,register_no,dept,year)
                    elif c == 5:
                        while True:
                            register_no = input("Enter the Student Register No. to be Deleted : ").strip()
                            if v.validate_register_no(register_no):
                                break
                        stu.delete_student(register_no)
                    elif c == 6:
                        break
                    else:
                        print("Invalid Choice Try Again...")
                except ValueError:
                    print("Please enter the choice in digit...")       

    # Subject Management
        elif ch == 2:
            while True:
                print("------------------------------")
                print("   Subject Management")
                print("------------------------------")
                print("1. Add Subject")
                print("2. View Subject")
                print("3. Update Subject")
                print("4. Delete Subject")
                print("5. Exit")
                try:
                    c = int(input("Enter your choice : "))
                    if c == 1:
                        while True:
                            sname = input("Enter Subject Name : ").strip()
                            scode = input("Enter Subject Code : ").strip()
                            if sname == "":
                                print("Fields can't be empty...")
                            elif v.validate_subject_code(scode):
                                break
                        sub.add_subject(sname,scode)
                    elif c == 2:
                        sub.view_subject()
                    elif c == 3:
                        while True:
                            scode = input("Enter Subject Code to be Updated : ").strip()
                            sname = input("Enter Updated Subject Name : ").strip()
                            if sname == "":
                                print("Fields can't be empty...")
                            elif v.validate_subject_code(scode):
                                break
                        sub.update_subject(sname,scode)
                    elif c == 4:
                        while True:
                            scode = input("Enter the Subject Code to be Deleted : ").strip()
                            if v.validate_subject_code(scode):
                                break
                        sub.delete_subject(scode)
                    elif c == 5:
                        break
                    else:
                        print("Invalid Choice Try Again...")
                except ValueError:
                    print("Please enter the choice in digit...")

    # Mark Management
        elif ch == 3:
            while True:
                print("------------------------------")
                print("   Marks Management")
                print("------------------------------")
                print("1. Enter Mark")
                print("2. View Mark")
                print("3. Update Mark")
                print("4. Delete Mark")
                print("5. Exit")
                try:
                    c = int(input("Enter your choice : "))
                    if c == 1:
                        while True:
                            register_no = input("Enter the register number : ").strip()
                            if v.validate_register_no(register_no):
                                break
                        while True:
                            scode = input("Enter the subject code : ").strip()
                            if v.validate_subject_code(scode):
                                break
                        while True:
                            try:
                                imark = int(input("Enter the internal mark : "))
                                emark = int(input("Enter the exam mark : "))
                                if v.validate_mark(imark,emark):
                                    break
                            except ValueError:
                                print("Please enter a number...")
                        tmark = ((imark*40)/100)+((emark*60)/100)
                        m.enter_marks(register_no,scode,imark,emark,tmark)
                    elif c == 2:
                        m.view_marks()
                    elif c == 3:
                        while True:
                            register_no = input("Enter the register number to be Updated : ").strip()
                            if v.validate_register_no(register_no):
                                break
                        while True:
                            scode = input("Enter the subject code : ").strip()
                            if v.validate_subject_code(scode):
                                break
                        while True:
                            try:
                                imark = int(input("Enter the internal mark : "))
                                emark = int(input("Enter the exam mark : "))
                                if v.validate_mark(imark,emark):
                                    break
                            except ValueError:
                                print("Please enter a number...")
                        tmark = ((imark*40)/100)+((emark*60)/100)
                        m.update_marks(register_no,scode,imark,emark,tmark)
                    elif c == 4:
                        while True:
                            register_no = input("Enter the register number to be Deleted : ").strip()
                            if v.validate_register_no(register_no):
                                break
                        while True:
                            scode = input("Enter the subject code to be Deleted : ").strip()
                            if v.validate_subject_code(scode):
                                break
                        m.delete_marks(register_no,scode)
                    elif c == 5:
                        break
                    else:
                        print("Invalid Choice Try Again...") 
                except ValueError:
                    print("Please enter the choice in digit...")

    # Performance Analysis
        elif ch == 4:
            while True:
                print("------------------------------")
                print("  Performance Analysis")
                print("------------------------------")
                print("1. Student Performance")
                print("2. Exit")
                try:
                    c = int(input("Enter your choice : "))
                    if c == 1:
                        register_no = input("Enter the register number of the student : ")
                        p.calculate_performance(register_no)
                    elif c == 2:
                        break
                    else:
                        print("Invalid Choice Try Again...")
                except ValueError:
                    print("Please enter the choice in digit...")
                    
    # Reports           
        elif ch == 5:
            while True:
                print("------------------------------")
                print("  Report")
                print("------------------------------")
                print("1. Student Mark Report")
                print("2. Class Performance Report")
                print("3. Subject Performance Report")
                print("4. Top Performers")
                print("5. Exit")
                try:
                    c = int(input("Enter your choice : "))
                    if c == 1:
                        register_no = input("Enter the register number of the student : ")
                        r.student_mark_report(register_no)
                    elif c == 2:
                        r.class_performance_report()
                    elif c == 3:
                        r.subject_performance_report()
                    elif c == 4:
                        while True:
                            try:
                                no = int(input("Enter the no. of top performers : "))
                                if no > 0:
                                    break
                                else:
                                    print("Number of top performers must be greater than zero...")
                            except ValueError:
                                print("Please enter number of top performers in digits...")
                        r.top_performers(no)
                    elif c == 5:
                        break
                    else:
                        print("Invalid Choice Try Again...")
                except ValueError:
                    print("Please enter the choice in digit...")

    # Exit
        elif ch == 6:
            print("Thanks for using...")
            break

        else:
            print("Invalid Choice ! Please Choose Other Choice")

    except ValueError:
        print("Please enter the choice in digit...")