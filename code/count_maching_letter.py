s1 = input("Input 1: ")
s2 = input("Input 2: ")
count = 0
for i in range(len(s1)):
    if s1[i] == s2[i]:
        count += 1
print("Output:")
print(count, "letters match in the same position")