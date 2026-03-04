inp = input("enter string: ")
bank = {}
for i in inp:
    if i in bank:
        bank[i] += 1
    else:
        bank[i] = 1
for i in bank:
    print(i, bank[i])