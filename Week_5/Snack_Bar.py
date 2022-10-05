#SNACK BAR
#intializing prices 
price_of_coffee=100
price_of_vadai=100
price_of_sandwich=200
price_of_coke=60
#printing the proces to the customer
print(" 1. Coffee - Rs.100 \n 2. Vadai - Rs. 100 \n 3. Sandwich - Rs.200 \n 4. Coke - Rs.60")
#Asking the customers what they need to buy 
total_no_of_coffee=int(input("Enter The No of Coffee You Need:"))
total_no_of_vadai=int(input("Enter The No of vadai You Need:"))
total_no_of_sandwich=int(input("Enter The No of sandwich You Need:"))
total_no_of_coke=int(input("Enter The No of Coke You Need:"))
#calculatng the prices
price_of_coffee*=total_no_of_coffee
price_of_vadai*=total_no_of_vadai
price_of_sandwich*=total_no_of_sandwich
price_of_coke*=total_no_of_coke
total_price=price_of_coffee+price_of_vadai+price_of_sandwich+price_of_coke
discount=0
#yet to do this condition:
#if((sandwich>1)or(vadai>2)):
    #price_of_one_coffee=50
#using if to check if the customer has bought atleast one or more number of items in each
if((total_no_of_coffee>=1)and(total_no_of_vadai>=1)and(total_no_of_sandwich>=1)and(total_no_of_coke>=1)):
    total_price=(price_of_coffee+price_of_vadai+price_of_sandwich+price_of_coke)
#initializing discount amount
    discount = 20 
    total_price = total_price - (total_price * discount / 100)
#here we are checcking if total price >1000 then there is a discount 
elif(total_price > 1000):
    discount = 20   
    total_price = total_price - (total_price * discount / 100) 
print("Total cost of items : Rs.", total_price)



#output
1. Coffee - Rs.100 
 2. Vadai - Rs. 100 
 3. Sandwich - Rs.200 
 4. Coke - Rs.60
Enter The No of Coffee You Need:5
Enter The No of vadai You Need:5
Enter The No of sandwich You Need:5
Enter The No of Coke You Need:5
Total cost of items : Rs. 1840.0
