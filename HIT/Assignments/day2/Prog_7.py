n = int(input("Enter number of elements - "))
l1 = []
for i in range(n) :
    x = int(input("Enter element - "))
    l1.append(x)
    
    
not_sorted = True

for i in range(len(l1)-1):
    if (l1[i] < l1[i+1]):
        pass
    else:
        break
else:
    not_sorted = False
    print("Sorted in ascending")
    
for i in range(len(l1)-1):
    if(l1[i] > l1[i+1]) and not_sorted:
        pass
    else:
        break
else:
    not_sorted = False
    print("Sorted in descending")
    
if(not_sorted):
    print("Not Sorted")
    
