# import random
# name = input("Enter your name : ")
# print("Good luck !", name)
# words = ['cat', 'dog', 'hello', 'water', 'night']
# word = random.choice(words)
# turns = 5
# guesses = 0
# while turns > 0:
#     guess = input("Guess A " + str(len(word)) + " letter word:")
#     if len(guess)!=len(word):
#         print("! INVALID INPUT !")
#     index = 0
#     guesses = 0
#     for letter in range(len(guess)):
#         if guess[letter] == word[letter]:
#             print("G")
#             guesses += 1
#         elif guess[letter] in word:
#             print("Y")
#         elif guess[letter] not in word:
#             print("R")
#     if guesses == len(word):
#         print("You won", word)
#         exit()
#     turns -=1
#     print("You have these much ", turns,"turns")
# if guesses != len(word):
#     print("you lose and the word is :",word)
import random
name = input("Enter your name : ")
print("Good luck ", name)
words = ['cat', 'dog', 'anime', 'water', 'night']
turns = 5
level = 1
word = random.choice(words)

while level <= 3:
    length = 3
    while len(word) <= length:
        word = random.choice(words)
    guesses = 0
    index = 1
    while turns > 5:
        guess = input("Guess a character ")
        if guess == word[index]:
            print("G")
            guesses += 1
            index += 1
        elif guess in word:
            print("Y")
        elif guess not in word:
                print("R")
                turns -= 1
        print("You have", turns)
    if guesses == len(word):
        print("You won", word)
        length += 1
        level += 1
    else:
        print("you lose")
