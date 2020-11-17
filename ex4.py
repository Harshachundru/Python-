print("The program for printing birthday month")

month = ("JAN","FEB","MAR","APR","MAY","JUNE","JULY","AUG","SEP","OCT","NOV","DEC")
birthday = input("Enter the DOB in the order of DD-MM-YYYY")

index= int(birthday[3:5])-1

bd_month = month[index]

print("The birthday month is ", bd_month)


print("The program for adding new name")

friends= ["Harsha", "Sandeep","Pochu","Balu","Bulli"]
new_name =input("Enter your name:")
friends.append(new_name)

print("the new list is :", friends)
 
