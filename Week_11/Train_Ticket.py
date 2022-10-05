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

