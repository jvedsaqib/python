l1 = [272, 45, 11, 272]
l2 = []
temp = sum = 0

for i in l1 :
    while(i > 0):
        sum += i % 10
        i = i // 10
    l2.append(sum)
    sum = 0
    
print(l1)
print(l2)