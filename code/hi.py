inp = input("Enter text: ")
is_digit = False
for i in inp:
    if inp in ("1234567890"):
        is_digit = True
    else:
        is_digit = False
if is_digit == True:
    print("its a digit")
else:
    print("its not a digit")
