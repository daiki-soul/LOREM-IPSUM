name = input("enter string: ").lower()
storage = {}
vresult = ""
for i in name:
    if i in "aeiou":
        vresult += i
        if i in storage:
            storage[i] += 1
        else:
            storage[i] = 1
for i in storage:
    print(i, storage[i])