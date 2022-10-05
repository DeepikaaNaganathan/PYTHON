#Sample Program_04/09/2022
#Creating a list
my_list = [11,12,12,12,12,12]
#defining function as max_list and passing mylist as an argument
def max_list(My_List):
    max = My_List[0]
    #calculating the length of mylist and finding the greatest between the list
    for i in range(1, len(My_List)):
        if max <= My_List[i]:
            max = My_List[i]
    #Returning the maximum of a my list's value
    return max
#Assigning result as a variable for storing maximum of a list
result = max_list(my_list)
#printing the result
print("The Maximum of numbers in a list is " , result)


"""
OUTPUT:
TEST CASE 1
myList = [10,20,30,40,10]
The Maximum of numbers in a list is  40
TEST CASE 2
myList = [11,12,12,12,12,12]
The Maximum of numbers in a list is  12
 """
