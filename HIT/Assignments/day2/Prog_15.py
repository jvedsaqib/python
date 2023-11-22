l1 = ["A Prasad Sen", "Ananth B Chand", "Heera Juhuri", "Tapasi Das", "Gambhir Mudi"]

l2 = []

for i in l1:
    l2.append(i.split()[-1])
    
print(l1)
print(l2)