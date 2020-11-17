print("The program for 'for loop'")

blog_post= ["The python skills","Data types in python", "Conditional statements in python", "For loop in python", "Machine learning in python"]

for post in blog_post:
    print(post)

print("---------------------------------------------------------")

blog_post= ["","The python skills","Data types in python", "","Conditional statements in python", "For loop in python", "Machine learning in python"]

for post in blog_post:
    if post == "":
        continue
    print(post)
    
print("---------------------------------------------------------")

my_string = ("Harsha Venkata Sai Chudru")

for char in my_string:
    print(char)
    
print("---------------------------------------------------------")

for x in range(1,10):
    print(x)
    
print("---------------------------------------------------------")

person1 = {"Name":"Harsha", "Age":"23", "Course":"MSc", "Study":"Information systems", "Uni":"UCD"}
for key in person1:
    print(key,":",person1[key])

print("---------------------------------------------------------")

blog_post= { "python":["The python skills","Data types in python", "Conditional statements in python", "For loop in python", "Machine learning in python"], "PHP":["The Introductions","The loops","Conditional statements", "Fuction","Constructres"]}

for category in blog_post:
    print("The posts in ", category)
    for post in blog_post[category]:
        print(post)
