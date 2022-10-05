number_of_students = 3      #initializing number of students to 3
number_of_subjects = 3      #initializing number of subjects to 3
gpa_of_each_student = []    #initializing a list to store gpa of each student
#using for loop and intializing 
for student in range(number_of_students):       
    sum_of_marks = 0                            
    for subject in range(number_of_subjects):   
        print("Enter mark for student ", student+1, " in subject ", subject+1)     
        subject_mark = int(input())                                                 
        sum_of_marks += subject_mark                                    #calculating sum of marks by adding sum of marks with the subject mark
    gpa_of_the_student = round(sum_of_marks / number_of_subjects)       #calculating gpa by dividing sum of marks by number of subjects
    gpa_of_each_student.append(gpa_of_the_student)                      #adding the gpa of a student into a list
#using for loop to print the gpa of the students
for gpa in range(number_of_students):                                       
    print("GPA of student ", gpa+1, " is : ", gpa_of_each_student[gpa])     
average_of_the_class = round(sum(gpa_of_each_student) / number_of_students) #calculating average of the class
print("Average of the class is : ", average_of_the_class)                   #printing average of the class



#OUTPUT
Enter mark for student  1  in subject  1
100
Enter mark for student  1  in subject  2
100
Enter mark for student  1  in subject  3
100
Enter mark for student  2  in subject  1
100
Enter mark for student  2  in subject  2
100
Enter mark for student  2  in subject  3
100
Enter mark for student  3  in subject  1
100
Enter mark for student  3  in subject  2
100
Enter mark for student  3  in subject  3
100
GPA of student  1  is :  100
GPA of student  2  is :  100
GPA of student  3  is :  100
Average of the class is :  100
