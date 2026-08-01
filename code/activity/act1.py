inp = input("enter string:")
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
print(vresult)
print(cresult)
print(sresult)