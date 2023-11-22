myStr = "strength".upper()
l1 = []

for i in myStr:
    l1.append(i)
    
max_elem = []
s = ""

for i in l1:
    if i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U':
        #print(i, end=" ")
        s = s + i
    else:
        max_elem.append(s)
        s = ""
else:
    max_elem.append(s)
    s = ""
    
print(sorted(max_elem)[0])