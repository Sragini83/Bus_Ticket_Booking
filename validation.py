import re
def isPhoneNumberValid(mobile_no):

    # condition to validate mobile number
    # 1. 10 digit / 11 digit with 0/ 12 digit with 91
    # first digit should [6-9]/rest 9 digit [0-9]

    pattern = re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")

    if pattern.match(mobile_no):
        print(f"{mobile_no} is valid mobile number")
        return True
    else:
        print(f"{mobile_no} is not valid mobile number")
        return False

def isEmailidValid(email_id):

    # userid@domailname.ext
    # /w-for alphanumeric character
    # start in letter use ^
    # end with string $

    pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    if re.search(pattern, email_id):
        print(f"{email_id} is valid email id")
        return True
    else:
        print(f"{email_id} is not valid email id")
        return False