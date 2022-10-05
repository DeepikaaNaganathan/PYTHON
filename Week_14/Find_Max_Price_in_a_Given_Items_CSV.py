file = open(r"C:\Users\Deepikaa Naganathan\Desktop\SAYUR\Python\Week_14\input.csv", "r")  
Price_of_Index = 1                    
Item_index = 0                     
Maximum_Price_of_an_Item = 1                

next(file)                       
for item in file:                 
    Split_variable = item.split(",")       
    Price_Of_Each_Item = int(Split_variable[Price_of_Index]) 
    if(Maximum_Price_of_an_Item <= Price_Of_Each_Item):             
        Maximum_Price_of_an_Item = Price_Of_Each_Item              
        Items_Name = Split_variable[Item_index]

print("Maximum price in the list of items : ", Maximum_Price_of_an_Item, " and the product is : ", Items_Name)     

file.close()


"""
OUTPUT:

Maximum price in the list of items  :  65  and the product is :  Donut

"""
