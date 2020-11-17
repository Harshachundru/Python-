print("The program to calculate for BMS and tells the persons body health")

weight= float(input("Enter weight in kilos:"))
height= float(input("Enter height in meters:"))

BMI= float(weight/(height*height))
print("BMI:" ,round(BMI,2))
if( BMI <= 18.5):
    print("You are underweight, so put on weight")
elif(BMI > 18.5 and BMI<= 24.9):
    print("you are FIT")
elif(BMI > 24.9 and   BMI<= 29.9):
    print("You are Overweighted , so be on deit")
else:
    print("You are in obesity state, so reduce your weight")
 
    

    

