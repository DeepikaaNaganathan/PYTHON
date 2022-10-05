"""
Write a function that displays a square box with '*'. Input is the width of the sqaure.
"""
# Hollow square star pattern in Python
# creating a function called square_side
def pattern(square_side):
   for row in range(square_side):
      for column in range(square_side):
         # printing stars if row's/column's value is  0 we are printing the "*", 
         # and to get the hallow square we are subtracting 1 from square side of row's/column's,
         # and that shouldbe equal to the column's value
         if (row == 0 )or (row == square_side-1) or (column == 0 )or (column == square_side-1):
            #printing "*" and giving space
            print("*", end=" ")
            #else printing space
         else:
            print(" ", end=" ")
      print("\r")
 
# taking input from user
width = int(input('Enter the number of rows: '))

# calling the function
pattern(width)

"""
OUTPUT
TEST CASE 1
Enter the number of rows: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
____________________________________
TEST CASE 2
Enter the number of rows: 10
* * * * * * * * * * 
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * *
______________________________________
TEST CASE 3
Enter the number of rows: 8
* * * * * * * * 
*             *
*             *
*             *
*             *
*             *
*             *
* * * * * * * *
________________________________________
TEST CASE 4
Enter the number of rows: 3
* * * 
*   *
* * *
_________________________________________
"""
