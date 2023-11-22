# 5. Sort the items of a dictionary (i) by keys, (ii) by values

di = {
      2 : 'Feb',
      1 : 'Jan',
      3 : 'Mar'
      }
    
print(dict(sorted(di.items())))

li = sorted(di.values())

newli = []

for i in li:
    for key, val in di.items():
        if i == val:
          newli.append((key, val))
          
print(dict(newli))
    