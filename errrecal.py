print("------------------------------------------------------------")
std_num = input("Enter the student number:")
try:
    std_num = float(std_num)
    print(std_num)
except:
    print("Invalid number")
