number_Of_Subjects = int(input("Enter number of subjects : "))
subject_Mark = []
for subject in range(number_Of_Subjects):
    mark = int(input("Enter mark for subject: "))
    subject_Mark.append(mark)

def calculateResult(subject_Mark):
    count_40 = 0
    count_80 = 0
    count_90 = 0
    count_between = 0
    for mark in range(len(subject_Mark)):
        if(subject_Mark[mark] <= 100):
            if(subject_Mark[mark] < 40):
                count_40 += 1
            else:
                if(subject_Mark[mark] > 90):
                    count_90 += 1
                    count_80 += 1
                    count_between += 1
                elif(subject_Mark[mark] > 80):
                    count_80 += 1
                    count_between += 1
                else:
                    count_between += 1
    if(count_90 == number_Of_Subjects):
        return "Distinction"
    elif(count_80 == number_Of_Subjects):
        return "First class"
    elif(count_between == number_Of_Subjects):
        return "Second class"
    elif(count_40 == number_Of_Subjects):
        return "Fail"
    else:
        return "Not eligible"

result = calculateResult(subject_Mark)
print("Result is : ", result)
