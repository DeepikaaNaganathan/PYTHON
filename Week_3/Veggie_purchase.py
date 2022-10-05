#Calculating how many kilograms of onion and tomato we can buy
budget=float(input("enter your amount:"))#getting their amount
if(budget>=0):#for checking their budget amount
    onionrate=20
    tomatorate=10.5
    kgofonion=budget/onionrate#calculating how many kgs we can buy
    kgoftomato=budget/tomatorate
else:
    print("please enter a valid amount , this is insufficient ")
    #going to print the results
print(kgofonion,"kg of onion you can buy")
print("and also you can buy")
print(kgoftomato,"kg of tomato you can buy")







#output
enter your amount:100.80
5.04 kg of onion you can buy
and also you can buy
9.6 kg of tomato you can buy
