def printAvailableSourceAndDestination(source_available):
    print("Please choose source and destination from the below list:")
    for i in range (len(source_available)):
        print(i ,".  " ,source_available[i])

def printBookedTicketDetail(all_booked_ticket):
    for booked_ticket in all_booked_ticket:
        print("Hey" ,booked_ticket["first_name"] ,"Below is your ticket detail:")

        for key in booked_ticket.keys():
            print(key, ": " ,booked_ticket[key])