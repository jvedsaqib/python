# 1. Given a non-empty dictionary, create a list of tuples where
# each tuple is a (key, value) pair of the dictionary.

di = {
      'FirstName' : 'Saqib',
      'LastName' : 'Javed',
      'Degree' : 'MCA',
      }

print(di)

t = []


print()

for key,value in di.items():
    t.append((key,value))
    
t = tuple(t)

print(t)