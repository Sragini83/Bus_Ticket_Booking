import json
def SaveDataToJson(data):
	ticket_json_object = json.dumps(data, indent=4)
 
	with open("booked_ticket.json", "w") as outfile:
	    outfile.write(ticket_json_object)
    
