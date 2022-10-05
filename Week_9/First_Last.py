#Printing A statement for user to print it in caps
print("*****KINDLY ENTER YOUR INPUT IN CAPITAL LETTERS*****")
#defining  function as betweenA
def betweenA(word):
    #Assigning value for variable 
    first_A = -1
    last_A = -1
    #using find function for finding "A"
    first_A = word.find("A")
    last_A = word.rfind("A")
    #checking whether the A is there or not and checking 2 "A"'s are there or not
    if(first_A==-1 or first_A == last_A):
        print("There is no first A or last A")
        betweenB(word)
    elif(first_A == last_A-1):
        print("There is no letter between first and last A")
        #Else printining the letters between First A and Last A
    else:
        print("Letters between first and last A")
        for letter in range(first_A+1, last_A):
            print(word[letter], end = " ")
#defining  function as betweenB
def betweenB(word):
    #Assigning value for variable 
    first_B = -1
    last_B = -1
    #using find function for finding "B"
    first_B = word.find("B")
    last_B = word.rfind("B")
    #checking whether the B is there or not and checking 2 "B"'s are there or not
    if(first_B==-1 or first_B == last_B):
        print("There is no first B or last B")
        betweenC(word)
    elif(first_B == last_B-1):
        print("There is no letter between first and last B")
        #Else printining the letters between First B and Last B
    else:
        print("Letters between first and last B")
        for letter in range(first_B+1, last_B):
            print(word[letter], end = " ")
#defining  function as betweenc
def betweenC(word):
    #Assigning value for variable 
    first_C = -1
    last_C = -1
    #using find function for finding "C"
    first_C = word.find("C")
    last_C = word.rfind("C")
    #checking whether the C is there or not and checking 2 "C"'s are there or not
    if(first_C==-1 or first_C == last_C):
        print("There is no first C or last C")
    elif(first_C == last_C-1):
        print("There is no letter between first and last C")
        #Else printining the letters between First C and Last C
    else:
        print("Letters between first and last C")
        for letter in range(first_C+1, last_C):
            print(word[letter], end = " ")

word = input("Enter a word : ")
betweenA(word)

"""
OUTPUT
TEST CASE 1
CATC
There is no first A or last A
There is no first B or last B
Letters between first and last C
A T
TEST CASE 2
Enter a word : BBBBB
There is no first A or last A
Letters between first and last B
B B B
TEST CASE 3 
Enter a word : deepikaa
There is no first A or last A
There is no first B or last B
There is no first C or last C
SINCE I GOT THIS ERROR I HAVE MENTIONED THE PRINT STATEMENT
TEST CASE 4
*****KINDLY ENTER YOUR INPUT IN CAPITAL LETTERS*****
Enter a word : DEEPIKAA
There is no letter between first and last A
"""
