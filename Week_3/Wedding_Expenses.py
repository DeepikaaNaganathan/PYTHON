#WEDDING EXPENSES PROGRAM

cost_for_lunch_per_person = int(input("Enter your amount : "))#Getting cost for lunch per person
cost_for_breakfast_per_person = cost_for_lunch_per_person / 2#calculating cost for breakfast per person
cost_for_hall_per_person = cost_for_lunch_per_person / 3#calculating cost for hall per person
dec_cost = cost_for_hall_per_person / 2 #calculating cost for decoration
parking_cost_per_person  = (cost_for_hall_per_person *10) /100#calculating parking cost
tot_exp_in_wedding = cost_for_lunch_per_person + cost_for_breakfast_per_person + cost_for_hall_per_person + dec_cost + parking_cost_per_person#calculating total cost
no_of_persons = int(input("Enter the persons : "))#getting the total no of guest 
tot_exp_in_wedding *= no_of_persons#total expenses for the wedding

print("This is the total expenses of wedding",tot_exp_in_wedding)#printing the output



#output
Enter your amount : 2000
Enter the persons : 160
This is the total expenses of wedding 650666.6666666666
