actualWord = list("hello")
guessedWord = list("llllo")

for i in range(0, len(actualWord)):
    if guessedWord[i] == actualWord[i]:
        print("Green ")
    elif guessedWord[i] in actualWord:
        if guessedWord.count(guessedWord[i]) == actualWord.count(guessedWord[i]):
            print("Yellow ")
        else:
            guessedWord[i] = "?"
            print("red ")
    else:
        print("red")




"""
H e l m o  - ComputerWord
     

    l l a o o  - UserWord
    0 1 2 3 4

    H l l m A  - userWord
    G R G
    
   AnswerWord - [Y-l,R-l,  ]  (GYRGy) - is to keep track of R,Y, G
 Keep track of color, position and letter in one DS                                


   First Condition-- (For checking Green)
      If the letter in userWord  is in the same index of the computerword
   
Second condition  (Checking for yellow)
      If the letter in userword is anywhere in the ComputerWord"""
