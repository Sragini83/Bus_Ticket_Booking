import datetime
def bookTicket(source, destination, person_deatil, fare, distance):

    calculated_fare = fare[(source ,destination)]
    calculated_distance = distance[(source ,destination)]

    ticket_detail = person_deatil
    current_time = datetime.datetime.now()

    ticket_detail["fare"] = calculated_fare
    ticket_detail["ticket_booking_time"] = current_time
    ticket_detail["total_travel_distance"] = calculated_distance

    return ticket_detail