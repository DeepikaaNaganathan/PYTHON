#reading users input
word = input("Enter a word : ")
#assigning some meaningful values to a variable
first_index = -1
last_index = -1
#using for loop checking the index of the word , first and last index of the word is being stored through tracking it by a variable
for letter in range(len(word)):
    if(word[letter] == "A" or word[letter] == "a" and first_index == -1):
        first_index = letter
    elif(word[letter] == "N" or word[letter] == "a"):
        last_index = letter
        break
#if the first_index position is not valid or incorrect or it is not having any such input then will block will return,and last_index is not having any N/a in it then elif block will return
if(first_index == -1):
    print("There is no A or a")
elif(last_index == -1):
        print("There is no N or a to stop printing letters")
# or else it checks any letters in between first A/a and first N/a if not it returns if block       
else:
    if(first_index+1 == last_index):
        print("No letters between first A/a and first N/a")
    else:
        #if letters are there then it checks and print those letters by another for loop it checks the position and print it of
        print("Letter between first A/a and first N/a")
        for letter1 in range(first_index + 1, last_index):
            print(word[letter1])
            
#             OUTPUT
#             TEST CASE 1
#             Enter a word : Adeepikaa
# Letter between first A/a and first N/a
# d
# e
# e
# p
# i
# k
#             TEST CASE 2
#     Enter a word : NasdfghA
# There is no A or a
#             TEST CASE 3
#     Enter a word : Aakipeed
# No letters between first A/a and first N/a
#             TEST CASE 4
#     Enter a word : AdhavA
# Letter between first A/a and first N/a
# d
# h
