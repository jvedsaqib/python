l1 = [1, 3, 2, 5, 4]
l2 = []

for i in range(0, len(l1)+1):
    if i < len(l1)-1:
        l2.append(l1[i:i+2])
        
print(l2)