l1 = ["MCA1205", "MCA2125", "HUM2210", "MTH2101", "MCA1295"]
l2=[]


for i in l1:
    if i.startswith("MCA"):
        l2.append(i)
    
print(l1)
print(l2)