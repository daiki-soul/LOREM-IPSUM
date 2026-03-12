#Joshua A. Reyes CC3 - Lab Exercises //MARCH 7 2026
#WMA-1C

inp = input("enter string: ")
bank = {}
for i in inp.lower():
    if i == " ":
        continue
    if i in bank:
        bank[i] += 1
    else:
        bank[i] = 1
for i in bank:
    print(i, "=", bank[i])