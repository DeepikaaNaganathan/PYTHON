#CALCULATING VEGGIES AND EXCLUDING PETROL EXPENSES
budget = float(input("Enter the amount : "))#getting their amount
city = input("Enter the city : ")#getting thier cities
tomato_price = 10.5
fbud =budget - 3/budget*100#calculating expenses
print(fbud,"this is the petrol expenses")
if(fbud==0):
   print("NOT ENOUGH BUDGET")
elif(city=="chennai"):#calculating onion price in different cities
    priceofonionchn=30.0
    kgofonionchn=fbud/priceofonionchn
    print(kgofonionchn,"Kg of onion you can buy in",city)
elif(city=="madurai"):
    priceofonionmdu=34
    kgofonionmdu=fbud/priceofonionmdu
    print(kgofonionmdu,"Kg of onion you can buy in",city)
elif(city=="trichy"):
    priceofoniontry=27
    kgofoniontry=fbud/priceofoniontry
    print(kgofoniontry,"Kg of oinion you can buy in",city)
#calculating tomato price
kgoftomato = fbud/tomato_price
print(kgoftomato," Kg of tomato you can buy")



#output
Enter the amount : 100
Enter the city : chennai
97.0 this is the petrol expenses
3.2333333333333334 Kg of onion you can buy in chennai
9.238095238095237  Kg of tomato you can buy
