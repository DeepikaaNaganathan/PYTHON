import random                           #importing random to roll dice
import numpy as np                      #importing numpy to create a matrix

start_Number = 1                       #start number for rolling dice starting from 1                                     
End_Number = 6                           #end number for rolling dice till 6 only
Player_One_Point = 0                      #initializing player 1's point as 0
Player_Two_Point = 0                      #initializing player 1's point as 0
Play_Turn = 1                            #initializing the player's play as 1 to start with
# userWins = False                        #initializing user winning as false since the game has just started

def createBoard():                      #function to create a 6x6 board
    global board                        #declaring board as global to access it in the program
    board = np.array([["A1","A2", "A3", "A4", "A5", "A6"],
                    ["B1", "B2", "B3", "B4", "B5", "B6"],
                    ["C1", "C2", "C3", "C4", "C5", "C6"],
                    ["D1", "D2", "D3", "D4", "D5", "D6"],
                    ["E1", "E2", "E3", "E4", "E5", "E6"],
                    ["F1", "F2", "F3", "F4", "F5", "F6"],])        #creating a board as matrix

def rollDice():                         #function to roll dice
    Dice_Roll_Row = random.randint(start_Number, End_Number)            #getting a random number as row
    Dice_Roll_Column = random.randint(start_Number, End_Number)         #getting a random number as column
    return [Dice_Roll_Row,Dice_Roll_Column]
                            
