inp = str(input("input string: ")).lower()
storage = {}
vresult = ""
cresult = ""
specialc = ""
total = vresult + cresult

for i in inp:
    if i in ("aeiou"):#vowels counter
        vresult += i
    elif i.isalpha():#consonant counter
        cresult += i
    else:
        specialc += i
        


for i in inp:#tells when letter appear the most
    if i.isalpha():
        if i in storage:
            storage[i] += 1
        else:
            storage[i] = 1

if storage:
    storagemax = max(storage.values())
    storagemin = min(storage.values())

for i in storage:
    if storage[i] == storagemax:
        print(i, storage[i], "most")

    if storage[i] == storagemin:
        print(i, storage[i], "least")



print(len(inp), "letters.")
print("vowels:", len(vresult))#how many vowels
print("consonant:", len(cresult))#how many consonants


lorem
