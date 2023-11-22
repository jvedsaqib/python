s1 = input("Enter a string : ")

l1 = []
for i in range(len(s1)):
    for j in range(i+1, len(s1)):
        if s1[i] == s1[j]:
            l1.append(s1[i])
            
print(l1)