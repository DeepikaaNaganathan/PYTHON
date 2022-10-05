#example program
#getting input from user
yourword=input("Enter your string:")
yourchar1 = input("enter the character 1 you want to find: ")
yourchar2 = input("enter the character 2 you want to find: ")
#assigning values to the variable
char_count = 0
start = -1
end = -1
#printing the word
print(yourword)
#creating a variable called errmsg and kept as a boolean(true/false)
errmsg = True
#creating a variable called strlen to store the length of the variable
strlen= len(yourword)
#using for loop for finding the index position of the given input
for word_index in range (0,strlen):
    if(yourword[word_index] == yourchar1):
        start = word_index
    if(yourword[word_index] == yourchar2):
        end = word_index
#printing the Start and end word_index that is equal to the character the user gives
print(start,end)
#this loop is for counting the character 
if(start != -1) and (end != -1) and (start < end):
    for count in range((start+1),end):
        char_count += 1
    print(char_count)
#if none of it matches the case then else need to be printed 
else:
    print("index not found or not in the correct order")
    
    #OUTPUT
#     TEST CASE 1
#     Enter your string:apple
# enter the character 1 you want to find: p
# enter the character 2 you want to find: e
# apple
# 2 4
# 1
#     TEST CASE 2
#     Enter your string:applee
# enter the character 1 you want to find: p
# enter the character 2 you want to find: e
# applee
# 2 5
# 2
#     TEST CASE 3
#     Enter your string:deepikaa
# enter the character 1 you want to find: d
# enter the character 2 you want to find: a
# deepikaa
# 0 7
# 6
# TEST CASE 4
# Enter your string:deepikaa
# enter the character 1 you want to find: r
# enter the character 2 you want to find: h
# deepikaa
# -1 -1
# index not found or not in the correct order
