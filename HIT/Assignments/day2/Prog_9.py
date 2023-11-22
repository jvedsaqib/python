l1 = ["BSC", "MSC", "BTECH", "MTECH", "BLIB", "MLIB"]
print(l1)

k = 0

elem = input("Enter element : ")

for i in l1:
    if elem == i:
        l1.append(l1.pop(k))
    k += 1


print(l1)