#creating two lists to store numeric values of numbers and numbers in word
number_in_numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number_in_words = ["Zero", "One", "Two", "Three", "Four","Five", "Six", "Seven", "Eight", "Nine"]
#reading input values from  user
number = str(input("Enter a number : "))
#using for loop for reading numeric values and numbers in word
for num1 in range(0, len(number)):
    for num2 in range(len(number_in_numeric)):
        #using if we are checking whether the numeric value and numbers in word is equal so that the
        #  output will be as for eg:123 one two three
        #we are using end=' ' statement for printing in a line
        if number[num1] == number_in_numeric[num2]:
            print(number_in_words[num2], end = ' ')
            break
            
            
OUTPUT
# test case 1
# Enter a number : 1213
# One Two One Three
# test case 2
# Enter a number : 1122334455
# One One Two Two Three Three Four Four Five Five
# test case 3
#  Enter a number : 01203040
# Zero One Two Zero Three Zero Four Zero 
