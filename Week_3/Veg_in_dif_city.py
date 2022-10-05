#buying veggies in differnt cities
budget=float(input("Enter Your Amount:"))#geting their amount
city=str(input("Enter your city:"))#getting their cities
if(budget==0):#checking whether the amount is enough or not
    print("Enter a valid amount,This is insufficient amount")
elif(city=="chennai"):#calculating onion price in different cities
    priceofonionchn=30
    kgofonionchn=budget/priceofonionchn
    print(kgofonionchn,"kg of onion you can buy in ",city)
elif(city=="madurai"):
    priceofonionmdu=34
    kgofonionmdu=budget/priceofonionmdu
    print(kgofonionmdu,"kg of onion you can buy in ",city)
elif(city=="trichy"):
    priceofoniontry=27
    kgofoniontry=budget/priceofoniontry
    print(kgofoniontry,"kg of onion you can buy in ",city)
#calculating how many tomatoes we can buy
priceoftomato=10.5
kgoftomato=budget/priceoftomato
print(kgoftomato,"kg of tomato you can buy")




#output
Enter Your Amount:1000
Enter your city:chennai
33.333333333333336 kg of onion you can buy in  chennai
95.23809523809524 kg of tomato you can buy
