l1 = ["a.out", "b.cpp", "cpp.c", "d.cpp", "e.h"]
l2=[]


for i in l1:
    l2.append(i.replace(".cpp", ".h"))
    
print(l1)
print(l2)