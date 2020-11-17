print("---------------------------------------------------------------")
print("PROGRAM TO CREATE A DICTONARY")
dic={"name":"harsha", "age":23, "nationality":"Indian","studies":"Msc","univ":"UCD","phn":"899459687"}
key = input('enter the key to know the informatiom you wanted(example:"name"):').lower()
print(dic.get(key,"invalid key"))
key = input('enter the key to know the informatiom you wanted(example:"name"):').lower()
print(dic.get(key,"invalid key"))
key = input('enter the key to know the informatiom you wanted(example:"name"):').lower()
print(dic.get(key,"invalid key"))




print("---------------------------------------------------------------")
print("PROGRAM TO CREATE LIST AND ADD NEW ITEM")
names =['john', 'mark','Don','damn','jap']
new_name = str(input("enter your name:") )
names.append(new_name)
print("The new list is:",names)

print("---------------------------------------------------------------")
print("THE PROGRAME TO CREATE A LIST & TUPLE")
dob = input("Enter your DOB in the format DD-MM-YYYY :")
month= ['Jan', 'Feb','Mar','Apr','May','June','Jul','Aug','sep','Oct','Nov','Dec']
dob_month = int(dob[3:5])-1
born_month = month[int(dob_month)]
print("You are born in:",born_month)

