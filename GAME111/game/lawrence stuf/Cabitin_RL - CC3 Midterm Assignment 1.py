#Hello = "New variable"
#try:
#    print(hello)
#except NameError:
#    print("Variable does not exist")
#else:
#    print("Hello")

Hello = "New variable"
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
try:
    print(int(num1) + (int(num2)))
    print(Hello)
    print(5/0)
except TypeError:
    print("type error")
except NameError:
    print("name error")
except ZeroDivisionError:
    print("zero division error")
else: #only prints if no error
    print("no error!")
finally: #will show with error or not, as the last one
    print("goodbye")



#ASSERT imma try doing a program that checks exam answers and if wrong, assert will say answer

#ALL POSSIBLE ERRORS:

#Syntax Error
#Type Error
#Name Error
#Index Error
#Key Error
#Value Error
#Attribute Error
#IO Error
#Zero Division Error
#Import Error