#mp03
print("MP03 INTERLEAVE WITH UPPERCASE RULE")
inp1 = input("Input String 1: ")
inp2 = input("Input String 2: ")
result = ""
for i in range(len(inp1)):
    result += inp1.upper()[i] + inp2.lower()[i]
print("Output:", result)