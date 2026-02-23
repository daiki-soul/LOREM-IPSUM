name = str(input("input name: "))
vresult = ""
cresult = ""
sc= ""
for i in name.lower():
    if i in "aeiou":
        vresult += i
    elif i in "qwertyuiopasadsfdgfhjklzxzcvbnmn":
        cresult += i
    else:
        sc += i
print(vresult)
print(cresult)
print(sc)
print()