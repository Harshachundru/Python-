print("The program to find the are of circle")

r = float(input("Enter the  radius:"))
import math
r2= r*r
area= math.pi*r2

print ("Area of the circle with radius", r, "is", round(area,3))
circum = 2*math.pi*r
print ("Circumference of the circle with radius", r, "is", round(circum,3))

