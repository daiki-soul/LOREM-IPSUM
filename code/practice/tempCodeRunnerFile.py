num1 = int(input("Enter the 1st number: ") )
num2 = int(input("Enter the 2nd number: ") )
try:
    print(num1 / num2)
except ZeroDivisionError:
    print("There is an Error!")
else:
    print("No Error Found") 