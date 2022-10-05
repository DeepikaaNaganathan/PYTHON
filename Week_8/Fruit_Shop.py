fruits_List = ["apple", "orange", "banana", "jackfruit", "cherry"]       
quantity_Word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
quantity_Numeric = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

fruits_in_Need = None                
quantity_in_Need = None             
customer = True                 

for fruit in range(len(fruits_List)):            
    print(fruit+1, fruits_List[fruit])


while(customer == True):                        
    print("Vendor: What do you want?")          
    customer_Response = input("Customer: ") 
   
