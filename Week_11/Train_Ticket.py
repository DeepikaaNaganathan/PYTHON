def getAge():
    for person in range(numberOfTickets):
        age = int(input("Enter your age to check for seniority : "))
        ageOfPassengers.append(age)
    return ageOfPassengers

def calculateFare():
    for age in range(len(ageOfPassengers)):
        if ageOfPassengers[age] >= 60:
            ticketFareOfPassengers.append(ticketFare / 2)
        else:
            ticketFareOfPassengers.append(ticketFare)
    totalFare = sum(ticketFareOfPassengers)
    if numberOfReturnTicket != 0:
        totalReturnTicketFare = numberOfReturnTicket * (returnTicketFare + ticketFare)
        totalFare += totalReturnTicketFare
    if numberOfTickets >=4:
        applyDiscount = 20 / 100
        totalFare -= (totalFare * applyDiscount)
    return totalFare

print("Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. \nBooking a return ticket costs extra Rs.750 \nFamily of 4 or above gets 20% off \nSenior citizens can get 50% off")
numberOfTickets = int(input("Enter total number of tickets : "))
numberOfReturnTicket = int(input("Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : "))
ticketFare = 1000
returnTicketFare = 750
ageOfPassengers = []
ticketFareOfPassengers = []

ageOfPassengers = getAge()
totalTicketCost = calculateFare()
print("Total cost of tickets : Rs.", totalTicketCost)
