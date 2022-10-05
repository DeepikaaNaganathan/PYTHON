number = int(input("Enter a number (to end, enter 0): "))    #gettinginput from user
total_numbers = 0                           #initializing total numbers to 0
sum_of_numbers = 0                          #initializing sum of all numbers to 0

while(number != 0):              #using while to continue reading numbers till the user enters 0 
    total_numbers += 1           #increasing total numbers by 1
    sum_of_numbers += number     #calculating sum of numbers by adding it with the input number
    number = int(input("Enter a number (to end, enter 0): "))       #getting next input from the user

if(sum_of_numbers==0):              #if statement that checks whether the sum of number is 0
    print("Average is null")        #printing that there is no average
else:                               #using else to print the average
    average_of_numbers = sum_of_numbers/total_numbers       #calculating average by dividing sum of numbers by total numbers
    print("Average of the given numbers is : ", average_of_numbers)     #printing the average of input numbers
    
    
    
    
    
#OUTPUT
Enter a number (to end, enter 0): 2
Enter a number (to end, enter 0): 3
Enter a number (to end, enter 0): 4
Enter a number (to end, enter 0): 5
Enter a number (to end, enter 0): 6
Enter a number (to end, enter 0): 0
Average of the given numbers is :  4.0
