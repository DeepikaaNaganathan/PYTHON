#PROFIT CAKE SHOP PROGRAM
#Calculating the amount which we spent on cake/bread
amt_spent_on_cake = 0
amt_spent_on_bread = 0
tot_sal_of_emp = 2*100
amt_earn_on_cake = 0
amt_earn_on_bread = 0
#initializing value
i = 1
#limiting the value
for i in range(10):
    #Customer's choice whether to buy bread/cake
    cus_buy_item = input("Enter What you bought cake/bread : ")
    if(cus_buy_item == "cake"):
        no_of_cake = int(input("Enter how many cake : "))
        amt_earn_on_cake += no_of_cake * 40
        amt_spent_on_cake += no_of_cake * 20
    if(cus_buy_item == "bread"):
        no_of_bread = int(input("Enter how many bread : "))
        amt_earn_on_bread += no_of_bread * 15
        amt_spent_on_bread += no_of_bread * 10
 #Amount Calculation        
total_amt_earn = amt_earn_on_cake + amt_earn_on_bread
total_amt_spent = amt_spent_on_cake + amt_spent_on_bread + tot_sal_of_emp
profit_of_the_day = total_amt_earn - total_amt_spent
#printing the amount
print("Total amount earn ",total_amt_earn)
print("Total amount spent ",total_amt_spent)
print("Profit of the day is ",profit_of_the_day)





#output
Enter What you bought cake/bread : cake
Enter how many cake : 5
Enter What you bought cake/bread : cake
Enter how many cake : 5
Enter What you bought cake/bread : cake
Enter how many cake : 5
Enter What you bought cake/bread : cake
Enter how many cake : 5
Enter What you bought cake/bread : cake
Enter how many cake : 5
Enter What you bought cake/bread : bread
Enter how many bread : 5
Enter What you bought cake/bread : bread
Enter how many bread : 5
Enter What you bought cake/bread : bread
Enter how many bread : 5
Enter What you bought cake/bread : bread
Enter how many bread : 5
Enter What you bought cake/bread : bread
Enter how many bread : 5
Total amount earn  1375
Total amount spent  950
Profit of the day is  425
