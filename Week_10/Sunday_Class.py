#Today's class discussion: Fruit Shop Problem


fruits_in_shop = ["Apple","Banana","Orange","Mango","Cherry"]
inventory_count = [10,20,20,20,10]
min_of_inventory = [5,10,8,5,8]
reorder_inventory = [5,10,4,5,4]
fruits_name = ""
end = None

def fruit_index(fruits_name):
    for i in range (0,len(fruits_in_shop)):
        if fruits_name == fruits_in_shop[i]:
            return i

def maintain_inventory(index,sales_count):
    if(sales_count > inventory_count[index]):
        print("Not enough inventory")
        reorderAmount = sales_count - inventory_count[index] + min_of_inventory[index]
        print("You need to reorder", fruits_in_shop[index], reorderAmount)
        inventory_count[index] = inventory_count[index] - sales_count + reorderAmount
        print(inventory_count[index])
    else:
        inventory_count[index] -= sales_count

def reorder_inventory_function(index):
    if(inventory_count[index]<min_of_inventory[index]):
        print("You need to reorder",fruits_in_shop[index],reorder_inventory[index])
        inventory_count[index]+=reorder_inventory[index]


while (fruits_name!="done"):
    fruits_name = input("Enter your fruit and enter done when complete: ")
    if (fruits_name == "done"):
        break
    sales_count = int(input("Enter how many do you want: "))
    index = fruit_index(fruits_name)
    maintain_inventory(index,sales_count)
    reorder_inventory_function(index)
