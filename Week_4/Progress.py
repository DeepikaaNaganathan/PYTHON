#calculaing Wtheter The Student Passes Or Not
sub1=int(input("Enter Marks Of The First Subject:"))#geting their marks as input
sub2=int(input("Enter Marks Of The second Subject:"))
sub3=int(input("Enter Marks Of The Third Subject:"))
sub4=int(input("Enter Marks Of The Fourth Subject:"))
sub5=int(input("Enter Marks Of The Fifth Subject:"))
#calculating Average for each subject
avg1=(sub1/100)*100
avg2=(sub2/100)*100
avg3=(sub3/100)*100
avg4=(sub4/100)*100
avg5=(sub5/100)*100
#checking whether the student passes or fails in the degree
if((sub1>=75)and(sub2>=75)and(sub3>=75)and(sub4>=75)and(sub5>=75)):
    print("he/she passes the degree")
elif((sub1>=50)and(sub2>=50)and(sub3>=50)and(sub4>=50)and(sub5>=50)):
    print("he/she passes the degree")
elif((sub1>=90)and(sub2>=90)and(sub3>=90)and(sub4>=90)and(sub5>=90)):
    print("he/she passes the degree")
elif((sub1>=40)and(sub2>=40)and(sub3>=40)and(sub4>=40)and(sub5>=40)):
    print("he/she passes the degree")
elif((sub1>=60)and(sub2>=60)and(sub3>=60)and(sub4>=60)and(sub>=60)):
    print("he/she passes the degree")
else:
    print("he fails in the degree")
    
    
    
    
    
  
