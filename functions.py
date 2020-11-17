def say_hello():
    print("Hello Everyone!")
say_hello()    

def mar_in(person):
    print("We invite",person, "to our marriage")
mar_in("Harsha")

def farh(farh):
    celsius = (5*(farh - 32))/9
    return celsius

print("Celsius:", round(farh(200),2))
print("kelvin:",  round((farh(100)+273.5),2))

def per2(person1,person2):
    print("Hello", person1, "and",person2)
per2("harsha", "nandu")


def per2(person1,person2="Nandu"):
    print("Hello", person1, "and",person2)
per2("harsha")




    



