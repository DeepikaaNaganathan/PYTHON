# CAFE PROGRAM
# assigning menu in the cafe and price of items,supplies
cafe_items = [" 1.classic coffee"," 2.classic Tea"," 3.cappuccino","4.chocoshake","5.sandwich","6.cake"]
price_of_items = [55, 50, 60, 100, 100,130]
cafe_supplies = [10, 10, 10, 10, 10,10]
# assigning the maximum of transtitions
max_trans = 10  
sales = [0,0,0,0,0,0]
inp= 0
#printing the menu
print(cafe_items[0:])
inp = int(input("Enter your option : "))
print(cafe_items[inp-1])
#using for loop for checking the option and
#  if to check the cafe items's in the index position and option are equal or not
for i in range(len(cafe_items)):
    #using index command to avoid the error 
    #since it is in integer (inp-1) to avoid type error ,using index command
            if(inp-1 == cafe_items.index(cafe_items[i])):
                print("--------EXCELLENT YOUR PRODUCT WAS THERE TAKE AND ENJOY IT----------")
#printing the quantity needed by the user
inpqut = int(input("Enter the Quantity :"))
#using for loop for supply
for j in range(len(cafe_supplies)):
    #if input is less than or equal to suppy then we are calculating cafe supplies and 
    # input quantities and storing it in cafe supplies and calculating amount earned
        if(inpqut <= cafe_supplies[j]):
                cafe_supplies[inp-1] -= inpqut
                amount_earned = inpqut * price_of_items[inp-1]
#printing the sales amount in the cafe 
sales[inp-1] += amount_earned
print("Sales in cafe is :",sales)

# TEST CASE 1
# [' 1.classic coffee', ' 2.classic Tea', ' 3.cappuccino', '4.chocoshake', '5.sandwich', '6.cake']
# Enter your option : 1
#  1.classic coffee
# --------EXCELLENT YOUR PRODUCT WAS THERE TAKE AND ENJOY IT----------
# Enter the Quantity :3
# Sales in cafe is : [165, 0, 0, 0, 0, 0]
#TEST CASE 2
# [' 1.classic coffee', ' 2.classic Tea', ' 3.cappuccino', '4.chocoshake', '5.sandwich', '6.cake']
# Enter your option : 4
# 4.chocoshake
# --------EXCELLENT YOUR PRODUCT WAS THERE TAKE AND ENJOY IT----------
# Enter the Quantity :7
# Sales in cafe is : [0, 0, 0, 700, 0, 0]
#TESE CASE 3
# [' 1.classic coffee', ' 2.classic Tea', ' 3.cappuccino', '4.chocoshake', '5.sandwich', '6.cake']
# Enter your option : 6
# 6.cake
# --------EXCELLENT YOUR PRODUCT WAS THERE TAKE AND ENJOY IT----------
# Enter the Quantity :10
# Sales in cafe is : [0, 0, 0, 0, 0, 1300]
