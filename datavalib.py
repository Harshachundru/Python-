data_valid = False

while data_valid == False:
    grade1 = input("type the grade of the first test:")
    try:
        grade1 = float(grade1)
        print("The entered grade is :", grade1)
    except:
        print("Invalid number")
        continue
        
    if grade1 < 0 or grade1 > 10:
        print("Invalid number and grade1 should be in between 0 and 10")
        continue
    else:
        data_valid = True
        
    
data_valid = False

while data_valid == False:
    grade2 = input("type the grade of the second test:")
    try:
        grade2 = float(grade2)
        print("The entered number is :", grade2)
    except:
        print("Invalid number")
        continue
    if grade2 < 0 or grade2 > 10:
        print("Invalid number and grade2 should be in between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    total_classes = int(input("Type the total of number of classes:"))
    if total_classes <= 0 or total_classes >30: 
        print("Invalid number and total grade should be in between 0 to 30")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = int(input("type the number of absences:"))
    if absences <=0 or absences > total_classes:
        print("Invalid number and grade1 should less than total classes and not less than equal to 0")
        continue
    else:
        data_valid = True

avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absences)/total_classes

print("Average grade:", round(avg_grade,2))
print("Attendance rate:", str(round((attendance *100),2))+'%')

if (avg_grade >= 6 and attendance >= 0.8):
    print("the student has been approved.")
elif(avg_grade < 6 and attendance < 0.8):
    print("the student has failed due to an average grade lower than 6 and lower attendance")
elif(attendance >= 0.8):
    print("the student has failed due to a lower grade")
else:
    print("the student has failed due to an lower attendance rate")
               
