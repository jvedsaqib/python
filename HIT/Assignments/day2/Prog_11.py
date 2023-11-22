s1 = input("Enter string : ")
l1 = []
for i in range(1,len(s1)+1):
    l1.append(s1[:i])

print(l1)