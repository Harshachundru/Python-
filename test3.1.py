print("To publish the results on the basis of average grade and the attendace percentage")

grade1 = float(input("Enter your garde of first test:"))
grade2 = float(input("Enter the grade of second test:"))
absences = int(input("Enter the absenses classes:"))
total_classes = int(input("Enter the total_classes:"))

average_grade= round((grade1 + grade2)/2)
attendance= (total_classes - absences)/total_classes

print("the average grade is:", round(average_grade,2))
print("The attendance percentage is :", str(round(attendance*100, 2))+'%')

if(average_grade >=6.5 and attendance >= 0.8):
    print("The candidate was approved")
elif(average_grade < 6.5 and attendance < 0.8):
        print("The candidate was failed  due to low attendence and low grade")
elif(average_grade >=6.5 and attendance < 0.8):
    print("The candidate was failed due to low attendance")
else:
    print("The candidate was failed due to low grades ") 
    
