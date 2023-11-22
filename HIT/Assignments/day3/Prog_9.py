# 9) Given a dictionary, which contains group names with the list of users 
# (Users can belong to multiple groups),
# create a dictionary with the users as keys and a list of their groups as values.

# Input: {"local": ["admin", "Ananya"],"public": ["admin", "Zahir"], "administrator”: ["admin"] }

# Output: {'admin': ['local', 'public', 'administrator'], 'Ananya': ['local'], 'Zahir':['public']}

di =  {"local": ["admin", "Ananya"],
       "public": ["admin", "Zahir"],
       "administrator" : ["admin"] }

s = []

for key, val in di.items():
    for i in val:
      s.append(i)
      
s = set(s)
# print(s)


li2 = []

for x in s:
    li = []
    for key, val in di.items():
        for i in val:
            if x == i:
              li.append(key)
    print(x, li)
    li2.append((x, li))
    
print(dict(li2))