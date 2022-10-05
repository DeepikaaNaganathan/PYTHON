#WEDDING EXPENSES LOAN PROGRAM

cost_for_lunch_per_person = int(input("Enter your amount : "))#getting cost for lunch per person
cost_for_breakfast_per_person = cost_for_lunch_per_person / 2#calculating cost for breakfast per person
cost_for_hall_per_person = cost_for_lunch_per_person / 3#calculating cost for hall per person
dec_cost = cost_for_hall_per_person / 2 #calculating cost for lunch per person
parking_cost_per_person = (cost_for_hall_per_person*10) /100#calculating cost for parking per person
tot_exp_in_wedding = cost_for_lunch_per_person + cost_for_breakfast_per_person + cost_for_hall_per_person + dec_cost + parking_cost_per_person#calculating total expenses for wedding
no_of_persons = int(input("Enter the persons : "))#getting total no of guest
tot_exp_in_wedding *= no_of_persons#over all wwedding expenses per person

print("This is the total expenses of wedding : ",tot_exp_in_wedding)#printing the total expenses
#Amount spending by groom and bride
amt_spent_in_Bride_Groom = tot_exp_in_wedding/2
amt_save_by_Bride_Groom = 50000
#printing the amount spent by bride and groom
print("The amount spent in Bride and Groom :",amt_spent_in_Bride_Groom)
#calculating bride and groom's spend amount to check whether need for an loan or not
if(amt_spent_in_Bride_Groom>amt_save_by_Bride_Groom):
    loan_amount = amt_spent_in_Bride_Groom - amt_save_by_Bride_Groom
    print("Required loan amount : ",loan_amount)
    print("So you need to take a loan ")
else:
    print("No need to take a loan my friend")
    
    
    
    
    #output
    Enter your amount : 1000
Enter the persons : 80
This is the total expenses of wedding :  162666.66666666666
The amount spent in Bride and Groom : 81333.33333333333
Required loan amount :  31333.33333333333
So you need to take a loan 
