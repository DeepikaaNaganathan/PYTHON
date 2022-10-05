        #   QUESTION 
#     Input a string. 
#     Print all the chars that are in Odd index - eg intput - abcd, output bd
#     Print all the chars in the even index in reverse order - eg input abcd output ca


#Reading input values from the user
input_string= input("enter the characters:  ")
#printing odd characters
print("odd characters: ")
#using for loop and initializing range according to our condition
for index in range(1,len(input_string),2):
    #printing the odd index's characters
        print(input_string[index])
#printing even characters
print("even characters: ")
#if length of the input string's index position value is divided by 2 and the remainder is 0 then it is in the even index 
if (len(input_string)%2==0):
    #using for loop and initializing range according to our condition
    for index in range(len(input_string)-2,-1,-2):
            print(input_string[index])
else:
    for index in range(len(input_string)-1,-1,-2):
             print(input_string[index])

             """ 
             OUTPUT
             TEST CASE 1
             enter the characters:  0a1b2c3d4e5f
odd characters: 
a
b
c
d
e
f
even characters:
5
4
3
2
1
0
             TEST CASE 2
             enter the characters:  1234567890
odd characters: 
2
4
6
8
0
even characters:
9
7
5
3
1
             TEST CASE 3
        enter the characters:  abcde
odd characters: 
b
d
even characters: 
e
c
a     
             TEST CASE 4
        enter the characters:  DEEPIKAA
odd characters: 
E
P
K
A
even characters:
A
I
E
D     
             
             
              """
