#reading users input
word = input("Enter a word : ")
#assigning some meaningful values to a variable
first_index = -1
last_index = -1
#using for loop checking the index of the word , first and last index of the word is being stored through tracking it by a variable
for letter in range(len(word)):
    if(word[letter] == "A" or word[letter] == "a" and first_index == -1):
        first_index = letter
    elif(word[letter] == "A" or word[letter] == "a"):
        last_index = letter
        break
#if the first_index position is not valid or incorrect or it is not having any such input then will block will return,and last_index is not having any N/a in it then elif block will return
if(first_index == -1):
    print("There is no A or a")
elif(last_index == -1):
    print("There is only one A or a")
# or else it checks any letters in between first A/a and first N/a if not it returns if block
else:
    if(first_index + 1 == last_index):
        print("There is no letter between first and last A/a")
    else:
        #if letters are there then it checks and print those letters by another for loop it checks the position and print it of
        print("Letters between first A/a and last A/a")
        for letter1 in range(first_index + 1, last_index):
            print(word[letter1])          
            
            
            
#             OUTPUT
#             TEST CASE 1
#             Enter a word : Aaaaaa
# There is no letter between first and last A/a
#             TEST CASE 2
#     Enter a word : applea
# Letters between first A/a and last A/a
# p
# p
# l
# e
#             TEST CASE 3
#     Enter a word : AppleA
# There is only one A or a
#             TEST CASE 4
#     Enter a word : Asdfghjklsdfghka
# Letters between first A/a and last A/a
# s
# d
# f
# g
# h
# j
# k
# l
# s
# d
# f
# g
# h
# k
