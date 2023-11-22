# 4. Append dictionary keys and values (in order), all keys before all values.
# Sample Input: {1: "Jan", 2: "Feb", 3: "Mar"}
# Output: [1, 2, 3, 'Jan', 'Feb', 'Mar']

di = {
      1 : 'Jan',
      2 : 'Feb',
      3 : 'Mar'
      }

d = [x for x in di.keys()]

for i in di.values():
    d.append(i)

print(d)