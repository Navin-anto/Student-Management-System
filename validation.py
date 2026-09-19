def validate_register_no(register_no):
    if register_no == "":
        print("Field can't be empty...")
        return False
    elif not register_no.isdigit():
        print("Register number should be in digits...")
        return False
    elif len(register_no) != 12:
        print("Register number should contain exactly 12 digits...")
        return False
    else:
        return True

def validate_subject_code(scode):
    if scode == "":
        print("Field can't be empty...")
        return False
    elif not scode.isalnum():
        print("Please enter a valid subject code...")
        return False
    elif len(scode) != 7:
        print("Subject code should contain exactly 7 characters...")
        return False
    else:
        return True

def validate_mark(imark,emark):
    if 0 <= imark <= 100 and 0 <= emark <= 100:
        return True
    else:
        print("Marks must be between 0 and 100...")
        return False

def validate_year(year):
    if 1 <= year <= 4:
        return True
    else:
        print("Years must be between 1 and 4...")
        return False