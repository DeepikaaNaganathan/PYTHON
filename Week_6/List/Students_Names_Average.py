#reading students names in list
Students_name=[]
#reading the total no of students who are in the class
Total_no_of_students=int(input("Enter The No Of Students :"))
#using for loop for reasing students name
for students in range(0,Total_no_of_students):
    students=str(input( "ENTER YOUR NAME :" ))
    Students_name.append(students)
 #printing students name   
print(*Students_name)
#Reversing students name in the list 
for Students in reversed(Students_name):
    #printing the reversed list
    print(Students)
    
    #error
    
    
#     name=input(str (Students_name [Students]) + "How Many Marks Do You Score ? : ")
#     mark=int(input("Enter" + str(Students_name[Students]) + "'s Mark :"))
#     sum_of_marks+=mark
# Average_of_the_class = sum_of_marks / total_no_of_students
# print("Average of the class")


#OUTPUT
# Enter The No Of Students :3
# ENTER YOUR NAME :sakthi
# ENTER YOUR NAME :sube
# ENTER YOUR NAME :deepi
# sakthi sube deepi
# deepi
# Traceback (most recent call last):
#   File "<string>", line 10, in <module>
# TypeError: list indices must be integers or slices, not str
