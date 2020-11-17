print("The list of programs for while loop")

x=0
people=[]
while x< 5:
    person= input("enter the name:")
    people.append(person)
    x+=1
print(people)

print("The list of programs for while loop without index variable")
people=[]
while len(people) < 5:
    person = input("Enter the name:")
    people.append(person)
print(people)

print("The program for guessing number")

number = 5
guess = int(input("Guess the number:"))
while True:
    if number == guess:
        break
    else:
        guess = int(input("Again Guess the number:"))
print("Your are right, The number is ", number)


print("The program for guessing number with random  number")

import random
number = random.randint(1,10)
guess = int(input("Guess the number:"))
while True:
    if number == guess:
        break
    else:
        guess = int(input("Again Guess the number:"))
print("Your are right, The number is ", number)




        

