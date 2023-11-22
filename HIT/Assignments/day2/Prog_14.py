l1 = [2182001, 2182023, 2282022, 2282056, 2182049, 2282036, 2182053]
l21=[]
l22=[]


for i in l1:
    if str(i)[0:2] == '22':
        l22.append(i)
    elif str(i)[0:2] == '21':
        l21.append(i)
    
print(l1)
print(l22)
print(l21)
