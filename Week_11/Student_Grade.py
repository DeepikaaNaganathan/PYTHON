"""
 Write an app to calculate Grades for students in each subject.
Mark > 90 is A, > 80 is B, > 70 is C, > 60 is D. anything less than 60 is fail.
Write a function that returns the grade for one subject for all the students in the class.
Also, print the class avg grade.

"""

#Getting Scores in array 
Scores = []
#creating a variable named total_student to sore the no of students in class
total_student = int(input(" Enter the total students in a class : "))
#creating for loop for reading the no of students mark:
for score in range (0,total_student):
    #Appending scores and  to read the value in 
    Scores.append(int(input(" Enter The Mark : ")))
#Assigning a meaningful value to a variable  
mark = 0
total_marks = 0
#creating a function called grade
def grade (mark):
    #According to the given conditon we are assigning values to the if,elif condition
    # Mark > 90 is A, > 80 is B, > 70 is C, > 60 is D. anything less than 60 is fail.
    if(mark > 90):
        print('Grade A')
    elif(mark > 80):
        print('Grade B')
    elif(mark > 70):
        print('Grade C ')
    elif(mark >=60):
        print('Grade D')
    elif(mark < 60):
        print('Fail')
#creating another loop for assigning grade for the corresponding marks
for index in range(0,len(Scores)):
    mark = Scores[index]
    grade(mark)
    total_marks += mark
#finding average grade of a class 
mark = total_marks / len(Scores)
#printing the class average grade with mark
print("Class Average grade is : " ,mark)
grade(mark)

""""
OUTPUT
TEST CASE 1
Enter the total students in a class : 5
 Enter The Mark : 100
 Enter The Mark : 100
 Enter The Mark : 100
 Enter The Mark : 100
 Enter The Mark : 100
Grade A
Grade A
Grade A
Grade A
Grade A
Class Average grade is :  100.0
Grade A
_____________________________________________________
TEST CASE 2
Enter the total students in a class : 5
 Enter The Mark : 79
 Enter The Mark : 85
 Enter The Mark : 87
 Enter The Mark : 53
 Enter The Mark : 56
Grade C 
Grade B
Grade B
Fail
Fail
Class Average grade is :  72.0
Grade C
_____________________________________________________
TEST CASE 3
Enter the total students in a class : 10
 Enter The Mark : 100
 Enter The Mark : 90
 Enter The Mark : 80
 Enter The Mark : 70
 Enter The Mark : 60
 Enter The Mark : 100
 Enter The Mark : 80
 Enter The Mark : 90
 Enter The Mark : 70
 Enter The Mark : 100
Grade A
Grade B
Grade C
Grade D
Grade A
Grade C
Grade B
Grade D
Grade A
Class Average grade is :  84.0
Grade B
_____________________________________________________
TEST CASE 4
Enter the total students in a class : 5
 Enter The Mark : 60
 Enter The Mark : 61
 Enter The Mark : 60
 Enter The Mark : 61
 Enter The Mark : 60
Grade D
Grade D
Grade D
Grade D
Grade D
Class Average grade is :  60.4
Grade D
_____________________________________________________
TEST CASE 5
Enter the total students in a class : 3
 Enter The Mark : 97
 Enter The Mark : 63
 Enter The Mark : 71
Grade A
Grade D
Grade C
Class Average grade is :  77.0
Grade C
_____________________________________________________
"""
