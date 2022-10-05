# QUESTION
#  Input two strings. Output is both strings merged . Eg - input1 = ABCD, input 2 = 1234. Output = A1B2C3D4 

 #reading first word
first_Word = input("Enter first word : ")
#reading second word
second_Word = input("Enter second word : ")     
#Printing The first and second word before getting merged     
print("The First_Word is :", first_Word ,"and" , "The Second_Word is :",second_Word)
#checking whether the length of the given strings is same
if(len(first_Word) == len(second_Word)):             
    print("The Merged Word is :")
    #if it is same then , iterating through the first input string
    for letter in range(len(first_Word)):            
        print(first_Word[letter],end="")
        print(second_Word[letter],end="")
 #if not same, printing not same
else:                                               
    print("The given strings are of different length")



    """ 
    OUTPUT
    TEST CASE 1
    Enter first word : deepi
Enter second word : 0502
The First_Word is : deepi and The Second_Word is : 0502
The given strings are of different length
    TEST CASE 2
    Enter first word : deepi
Enter second word : 05002
The First_Word is : deepi and The Second_Word is : 05002
The Merged Word is :
d0e5e0p0i2
    TEST CASE 3
    Enter first word : abcde
Enter second word : 12345
The First_Word is : abcde and The Second_Word is : 12345
The Merged Word is :
a1b2c3d4e5
    TEST CASE 4
    Enter first word : ABCDE
Enter second word : abcde
The First_Word is : ABCDE and The Second_Word is : abcde
The Merged Word is :
AaBbCcDdEe
    
     """
