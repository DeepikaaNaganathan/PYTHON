#importing random function 
import random
#Reading the input value
input_number = (int(input("Enter the number:")))
#Assigning a null value to variable named random_number 
random_number = 0
#creating a function called random_num()
def random_num():
    #using for loop for checking in the range between 1 to 1000 and defaultly incremented by +1
    for i in range(1,100):
        #Assining meaningful values in variable
        #Here we are using random.randint,since a selected element from the the specified range
        random_number = random.randint(1,100)
        #using if to check whether,inpremainder of my input number and my random number is 0 ,
        if(random_number % input_number ==0):
            #if it is 0 printing the relevant random numbers
            print(random_number , end = " , ")
        
#Calling the function
random_num()

"""
OUTPUT
TEST CASE 1
Enter the number:2
50 , 50 , 82 , 62 , 18 , 18 , 2 , 16 , 88 , 40 , 2 , 62 , 64 , 50 , 52 , 78 , 58 , 
56 , 20 , 60 , 14 , 36 , 56 , 28 , 60 , 32 , 88 , 86 , 2 , 52 , 2 ,
56 , 48 , 74 , 28 , 12 , 66 , 80 , 78 , 52 , 80 , 56 , 86 , 60 , 24 , 94 , 
_______________________________________________________________________
TEST CASE 2
Enter the number:50
50 , 50 , 100 , 
_______________________________________________________________________
TEST CASE 3
Enter the number:5
30 , 10 , 55 , 25 , 25 , 85 , 60 , 95 , 90 , 35 ,
60 , 45 , 15 , 55 , 80 , 15 , 25 , 75 , 30 , 45 , 40 , 
_______________________________________________________________________
TEST CASE 4
Enter the number:40
80 , 40 ,
_______________________________________________________________________

"""
