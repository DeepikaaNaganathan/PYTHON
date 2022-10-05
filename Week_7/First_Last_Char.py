#  Input a string. Print first and last char, add a comma, then print second and last but first char and so on.
#    eg - input ABCD1234 , output - A4,B3,C2,D1. 
#    Hint - use only one for loop. 


#reading input
word = input("Enter a word : ") 


firstHalf = len(word)          #initializing first half
secondHalf = len(word) - 1          #initializing second half

for letter in range(0, firstHalf):                          #iterating the firsthalf
    print(word[letter], end = "" + word[secondHalf])        #printing firsthalf and secondhalf elements
    if(firstHalf == secondHalf):                            #checking if both the indexes are the same
        break                                               #breaking from the statement
    print(",", end ="")                                     #printing comma
    secondHalf -= 1                                         #decreasing secondhalf index by 1
# OUTPUT
# TEST CASE 1
# Enter a word : deepi12345
# d5,e4,e3,p2,i1,1i,2p,3e,4e,5d,
# TEST CASE 2
# Enter a word : abc123
# a3,b2,c1,1c,2b,3a,
