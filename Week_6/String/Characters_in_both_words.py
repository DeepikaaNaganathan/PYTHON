#getting input as word from a user
first_word = input("Enter a word : ")
second_word = input("Enter a word : ")
#assigning a list same_char to store the same characters
same_char = []
#using nested for loop for checking the same characters in both words 
for char1 in range(len(first_word)):
    for char2 in range(len(second_word)):
        if first_word[char1] in same_char:
            break
        else:
            if first_word[char1] in second_word:
                same_char.append(first_word[char1])
print(*same_char)

#test case 1
# Enter a word : deepikaa
# Enter a word : lokesh barani
# e i k a
#test case 2
# Enter a word : deepikaa
# Enter a word : lokesh
# e k
# #test case 3
# Enter a word : deepikaa
# Enter a word : sakthi priya
# p i k a
