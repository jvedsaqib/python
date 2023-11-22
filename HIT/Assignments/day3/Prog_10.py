student = {
        "roll" : 31,
        "name" : "saqib",
        "marks" : [80, 78, 85]
    }

total = 0
for i in student.get("marks"):
    total += i
    
li = list(student.items())

li.append(("total", total))

print(dict(li))

for i,j in li:
    if i == 'marks':
        j.append(total)
        
print(dict(li))

li.pop(len(li) - 1)
li.pop(len(li) - 1)
li.append(('marks', total))
print(dict(li))