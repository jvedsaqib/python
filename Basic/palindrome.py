s = input("Enter a text: ")

print(s.split(' '))
list1 = s.split(' ') 

palin = []

for i in list1:
    if(i == i[::-1]):
        palin.append(i)

print(len(palin))
print(palin)
