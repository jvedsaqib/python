li = [1,2,3,4,5,6,7,8,9]
temp = 0

for i in range(len(li)//2):
    print(li[i],"+",li[len(li) - i - 1])
    temp += li[i] + li[len(li) - i - 1]
print(li[(len(li)//2)])
temp += li[(len(li)//2)]

print(temp)
