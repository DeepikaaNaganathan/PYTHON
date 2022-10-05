#initializing The Values
count_for_onlineclass_from_female = 0               
count_for_responses = 0                          
min_number_of_students = 10                         
#using for loop to get input and printing selection menu
for student in range(min_number_of_students):       
    print("Select\n1.Male\n2.Female")              
    gender = input()                                
    print("Which one do you like?\n1.Online class\n2.In person class\n3.Mixed\nTo end, enter 'No Comment'")     
    answer = input()                                
    count_for_responses += 1 
    #using if condition and break statement
    if(answer == "No Comment"):                     
        break                                      
    if(gender == "Female" and answer == "Online class"):    
        count_for_onlineclass_from_female +=1               
 #calculating the percentage of response of female students whose answer was online class
percentage = count_for_onlineclass_from_female * 100 / count_for_responses    
print(percentage, "percentage of female students like online class")  


#OUTPUT
Select
1.Male
2.Female
Female
Which one do you like?
1.Online class
2.In person class
3.Mixed
To end, enter 'No Comment'
Online class
Select
1.Male
2.Female
Female
Which one do you like?
1.Online class
2.In person class
3.Mixed
To end, enter 'No Comment'
No Comment
50.0 percentage of female students like online class
