print("The programe for user dict")
person={"name":"Harsha", "gender":"Male", "age":"23", "address":"Dublin", "phone":12345}

key= input("Enter the details:").lower()
result= person.get(key,"Invalid Entry")
print(result)

