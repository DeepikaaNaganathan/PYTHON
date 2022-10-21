Items_Data = {
    "Sandwich" : {
        "Price" : 40,
        "Supply" : 100,
        "Sales" : 0
    },
    "Donut" : {
        "Price" : 50,
        "Supply" : 100,
        "Sales" : 0
    },
    "Coke" : {
        "Price" : 30,
        "Supply" : 100,
        "Sales" : 0
    }
}
Max_Transaction = 10
Open_To_Order = 'yes'

for item in Items_Data.keys():
    print(item, " - Rs.", Items_Data[item]["Price"])
while Max_Transaction > 0 and Open_To_Order == "yes":
    for item in Items_Data.keys():
        No_Of_Item = int(input("How much " + item + " do you want? "))
        if No_Of_Item <= Items_Data[item]["Supply"]:
            Items_Data[item]["Supply"] -= No_Of_Item
            Items_Data[item]["Sales"] += No_Of_Item * Items_Data[item]["Price"]
        else:
            print("Out of stock")
    Max_Transaction -= 1
    Open_To_Order = input("Open to receive orders (yes / no) : ")

for item in Items_Data.keys():
    print("Sales in ", item, " - ", Items_Data[item]["Sales"])



"""OUTPUT
TEST CASE 1:
Sandwich  - Rs. 40
Donut  - Rs. 50
Coke  - Rs. 30
How much Sandwich do you want? 2
How much Donut do you want? 3
How much Coke do you want? 4
Open to receive orders (yes / no) : yes
How much Sandwich do you want? 3
How much Donut do you want? 4
How much Coke do you want? 5
Open to receive orders (yes / no) : no
Sales in  Sandwich  -  200
Sales in  Donut  -  350
Sales in  Coke  -  270
________________________________________________________
TEST CASE 2 :
Sandwich  - Rs. 40
Donut  - Rs. 50
Coke  - Rs. 30
How much Sandwich do you want? 10
How much Donut do you want? 11
How much Coke do you want? 12
Open to receive orders (yes / no) : NO
Sales in  Sandwich  -  400
Sales in  Donut  -  550
Sales in  Coke  -  360
________________________________________________________
"""
