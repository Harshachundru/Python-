print("The program to ask user for his names")

firstname= input("Enter your First name :")
middlename= input("Enter your Middle name :")
lastname= input("Enter your Last name :")

print("Your initials are", firstname[0], middlename[0], lastname[0])


print("The program to seperate the batch number of the company")

lotnumber= "O37-OO9O1-OOO27" 

countrycode= lotnumber[0:3]
print("The Country code is :" ,countrycode)

productcode= lotnumber[4:9]
print("The Product code is :" ,productcode)

batchnumber= lotnumber[10:]
print("The Batch number is :" ,batchnumber)


