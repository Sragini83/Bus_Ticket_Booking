
from datetime import datetime
from journey_detail import *
from booked_ticket import *
from print_detail import *
from validation import *
def isSourceAndDestinationValid(destination, source):
    if (source not in source_available) or (source == desti):
        print("we dont provide service from this source")
        return False
    else:
        if (desti not in desti_available) or (source == desti):
            print("we dont provide service from this desninatiom")
            return False
        else:
            print("Source and Destination are valid, you can book the ticket")
            return True

def takePersonDetail():
    first_name = input("Please enter the first_name:\t")
    last_name  = input("Please enter the last_name:\t")
    email_id   = input("Please enter the email-id:\t")
    mobile_no  = input("Please enter the mobile number:\t")

    person_detail = {"first_name" :first_name,
                     "last_name" :last_name,
                     "email_id" :email_id,
                     "mobile_no" :mobile_no}
    return person_detail
print("******Welcome to Online Bus Reversation Portal*******\n")
all_booked_ticket = []
restart = "Yes"
while (restart == "Yes"):
    printAvailableSourceAndDestination(source_available)
    source = input("enter the source:\t")
    desti = input("enter the destination:\t")
    if (isSourceAndDestinationValid(desti, source)):
        person_detail = takePersonDetail()

        mobile_no = person_detail["mobile_no"]
        is_mobile_number_valid = isPhoneNumberValid(mobile_no)
        while (not is_mobile_number_valid):            # ! means return false
            print("please re-enter the mobile number:\t ")
            mobile_no  = input("Please enter the mobile number:\t")
            is_mobile_number_valid = isPhoneNumberValid(mobile_no)
        person_detail["mobile_no"] = mobile_no
        email_id = person_detail["email_id"]
        is_email_id_valid = isEmailidValid(email_id)
        while (not is_email_id_valid):
            print("please re-enter the email id:\t")
            email_id   = input("Please enter the email-id:\t")
            is_email_id_valid = isEmailidValid(email_id)
        person_detail["email_id"] = email_id

        booked_ticket = bookTicket(source, desti, person_detail, fare, distance)

        all_booked_ticket.append(booked_ticket)

    restart = str(input("\nplease enter Yes to  book another ticket:\t"))

print("********Thanks for using our services***********")

printBookedTicketDetail(all_booked_ticket)


