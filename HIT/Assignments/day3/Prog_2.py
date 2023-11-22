# 2. Find maximum and minimum k elements in a Tuple.

t = (2,1,3,5,4)

li = list(t)

li = reversed(sorted(li))

t = tuple(li)
print(t)

k = int(input("Enter k : "))

print(t[0:k])
    
print()
    
print(t[len(t):k:-1])