cafe_items = ["classic coffee","classic Tea","cappuccino","chocoshake","sandwich","cake"]
price_of_items = [55, 50, 60, 100, 100,130]
supply = [100, 100, 100, 100, 100, 100]                                       

inp= 0

def cafe_shop():
    sales = [0,0,0,0,0,0]
    print(cafe_items[0:])
    for order in range(len(cafe_items)):
        percent = supply[order] /100*20
        inp = int(input("How much " + cafe_items[order] + " do you want to purchase? \n"))
        if(inp <= supply[order]):
            supply[order] -= inp
            sales[order] += inp * price_of_items[order]
            print("**********HAPPY ORDER**************")
            if(supply[order] <= percent):
                supply[order] = [100, 100, 100, 100, 100, 100]
                print("Stocks restored \n",supply[order])
        else:
            print("Out of stock")
            if(supply[order] >= supply[order]):
                supply[order] += 50
                print("Stocks restored \n",supply[order])

    print(sales)

cafe_shop();

"""
OUTPUT
TEST CASE 1
['classic coffee', 'classic Tea', 'cappuccino', 'chocoshake', 'sandwich', 'cake']
How much classic coffee do you want to purchase? 
100
**********HAPPY ORDER**************
Stocks restored
 [100, 100, 100, 100, 100, 100]
5500
How much classic Tea do you want to purchase?
100
**********HAPPY ORDER**************
Stocks restored
 [100, 100, 100, 100, 100, 100]
5000
How much cappuccino do you want to purchase?
100
**********HAPPY ORDER**************
Stocks restored
 [100, 100, 100, 100, 100, 100]
6000
How much chocoshake do you want to purchase?
100
**********HAPPY ORDER**************
Stocks restored
 [100, 100, 100, 100, 100, 100]
10000
How much sandwich do you want to purchase?
100
**********HAPPY ORDER**************
Stocks restored
 [100, 100, 100, 100, 100, 100]
10000
How much cake do you want to purchase?
100
**********HAPPY ORDER**************
Stocks restored
 [100, 100, 100, 100, 100, 100]
13000
_________________________________________________
TEST CASE 2
['classic coffee', 'classic Tea', 'cappuccino', 'chocoshake', 'sandwich', 'cake']
How much classic coffee do you want to purchase? 
2
**********HAPPY ORDER**************
110
How much classic Tea do you want to purchase? 
2
**********HAPPY ORDER**************
100
How much cappuccino do you want to purchase?
2
**********HAPPY ORDER**************
120
How much chocoshake do you want to purchase?
2
**********HAPPY ORDER**************
200
How much sandwich do you want to purchase?
2
**********HAPPY ORDER**************
200
How much cake do you want to purchase?
2
**********HAPPY ORDER**************
260
______________________________________________________
"""
