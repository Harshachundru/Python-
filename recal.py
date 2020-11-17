print("-------------------------------------------")
colors = ["red","green","yellow","blue","orange","white"]
import random
index = random.randint(0,5)

while True:
    color = colors[index]
    guess = input("Guess the color:").lower()
    while True:
        if(guess == color):
            print("You guessed it")
            break
        else:
            guess = input("Guess the color again!:").lower()
            
    key = input("wana play again type 'no' to quit").lower()
    if(key == 'no'):
        break
print("Thanks for playing")    



print("-------------------------------------------")
people=[]
import random
number = random.randint(0,5)
for x in range(0,5):
   person = input("Enter the name of person:")
   people.append(person)
ranperson = people[number]
print(ranperson)
        
print("-------------------------------------------")
import random
ranint = random.randint(0,5)
people=[]
while len(people) <=5:
    key = input("Enter the name of person:")
    people.append(key)
person = people[ranint]
print("The random name is:",person)    
    
    


print("-------------------------------------------")


print("-------------------------------------------")
print("THE PROHRAME TO CALCULATE THE BMI")
height= float(input("enter your height in meters'example:1.9999':"))
weight= float(input("enter your weight in kgs'example:75':"))
bmi= weight/(height*height)
print(bmi) 
if(bmi <= 18.5):
    classification= "underweight"
elif(bmi > 18.5 and bmi <=24.9):
   classification ="Normal"
elif(bmi >24.9 and bmi <= 29.9):
    classification ="Overweight"
else:
    classification="Obesity"
print(classification)    
    
    
                    
                    

