#mp01
print("MP01 REVERSE ALTERNATE MERGE")
inp1 = input("Input String 1: ")
inp2 = input("Input String 2: ")
result = ""
inp1result = ""
inp2result = ""
for i in range(len(inp1) - 1, -1, -1):#reverseinp1
    inp1result += inp1[i]
for i in range(len(inp2) - 1, -1, -1):#reverseinp2
    inp2result += inp2[i]
for i in range(len(inp1result)):
    result += inp1result[i] + inp2result[i]
print("Output:", result)