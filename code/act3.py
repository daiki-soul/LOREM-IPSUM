input1 = input("string1: ")
input2 = input("string2: ")
result = ""
for i in range(len(input1)):
    result += input1[i] + input2[i]
print(result)
