l1 = [1,2,3,4,5,6,7,8,9,10]

n = int(input("Enter number of chunks : "))

for i in range(0, len(l1) , n): 
    print(l1[i:i+n]) 