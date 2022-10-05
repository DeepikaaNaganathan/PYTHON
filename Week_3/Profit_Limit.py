#SUPPLY OF STOCKS
#Calculating the amount which we spent on cake/bread
amt_spent_on_cake = 0
amt_spent_on_bread = 0
tot_sal_of_emp = 200
amt_earn_on_cake = 0
amt_earn_on_bread = 0
#Limiting the supply of cake/bread
supply_of_cake = int(input("Enter the supply limit of cake: "))
supply_of_bread = int(input("Enter the supply limit of bread : "))
#initializing the value
i=1
#applying while condition because wedoesnt know the users end limit we only know supply limmit
while (supply_of_cake > 0 or supply_of_bread > 0) :
    cus_buy_item = input("Enter What you bought cake/bread : ")
    #using if to check whether the user needs cake/bread
    if(cus_buy_item == "cake"):
        no_of_cake = int(input("Enter how many cake : "))
        if(no_of_cake <= supply_of_cake):
            amt_earn_on_cake += no_of_cake * 40
            amt_spent_on_cake += no_of_cake * 20
            supply_of_cake -= no_of_cake
        else:
            print("Cakes are unavailable")
    
    if(cus_buy_item == "bread"):
        no_of_bread = int(input("Enter how many bread : "))
        if(no_of_bread <= supply_of_bread):
            amt_earn_on_bread += no_of_bread * 15
            amt_spent_on_bread += no_of_bread * 10
            supply_of_bread -= no_of_bread
        else:
            print("Breads are unavailable")
#Amount Calculation
total_amt_earn = amt_earn_on_cake + amt_earn_on_bread
total_amt_spent = amt_spent_on_cake + amt_spent_on_bread + tot_sal_of_emp
amt_of_the_day = total_amt_earn - total_amt_spent
print("Total amount earn ",total_amt_earn)
print("Total amount spent ",total_amt_spent)
print("Avaialbe cakes : ",supply_of_cake)
print("Avaialbe bread : ",supply_of_bread)
if(amt_of_the_day >=0):
    profit_of_the_day = amt_of_the_day
    print("Profit of the day is ",profit_of_the_day)
else:
    loss_of_the_day = amt_of_the_day
    print("Loss of the day ",loss_of_the_day)
    
    
    
    
    
    #output
    Enter the supply limit of cake: 3
Enter the supply limit of bread : 2
Enter What you bought cake/bread : cake
Enter how many cake : 1
Enter What you bought cake/bread : cake
Enter how many cake : 1
Enter What you bought cake/bread : cake
Enter how many cake : 1
Enter What you bought cake/bread : bread
Enter how many bread : 1
Enter What you bought cake/bread : bread
Enter how many bread : 1
Total amount earn  150
Total amount spent  280
Avaialbe cakes :  0
Avaialbe bread :  0
Loss of the day  -130
