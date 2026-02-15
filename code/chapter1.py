#input
gwa = float(input("Enter GWA: "))
units_enrolled = int(input("Enter number of units enrolled: "))

units_failed = int(input("Enter number of failed units: "))
has_diciplinary_case = str(input("Has diciplinary case? (yes/no): "))
print("\n")

#academic standing rule
if gwa <= 1.75 and units_failed == 0:
    print("Academic Standing: Excellent Standing")
elif gwa <= 2.5 and units_failed <= 6:
    print("Academic Standing: Good Standing")
elif gwa <= 3.0 and units_failed <= 6:
    print("Academic Standing: Probation")
else:
    print("Academic Standing: Dismissal")

#diciplinary
if has_diciplinary_case == "yes":
    has_diciplinary_case = "yes"
else:
    has_diciplinary_case = "no"

#eligibility
status = gwa <= 1.75 and units_failed == 0 and units_enrolled >= 18 and has_diciplinary_case == "no"
if status == True:
    print("Academic Standing: Eligible")
else:
    print("Academic Standing: Not Eligible")