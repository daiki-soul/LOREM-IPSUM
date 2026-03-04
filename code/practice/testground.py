inp = input("enter string:  ")
result = ""

for i in range(len(inp) - 1, -1, -1):
        result += inp[i]

print(result)