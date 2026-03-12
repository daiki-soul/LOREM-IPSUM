#Joshua A. Reyes CC3 - Lab Exercises //MARCH 7 2026
#WMA-1C

inp = input("Input String: ")
vresult = ""
cresult = ""
sresult = ""
for i in inp.lower():
    if i in "aeiou":
        vresult += i
    elif i in "qwertyuiopasdfghjklzxcvbnm":
        cresult += i
    else:
        sresult += i
print("Vowel", vresult)
print("Consonants:", cresult)
print("Special Char:", sresult)