# 7. Use a dictionary to count the frequency of words in an input string. Only words should be counted,
#   not blank spaces, numbers, or punctuation. Upper case should be considered the same as lowercase.
# Sample Input: Fear leads to anger; Anger leads to hatred; Hatred leads to conflict; Conflict
# leads to suffering.
# Output: {'fear': 1, 'leads': 4, 'to': 4, 'anger': 2, 'hatred': 2, 'conflict': 2, 'suffering': 1}

s = "this is a string and a, simple string".lower().strip()

li = s.split()

li2 = []

for i in li:
    li2.append(i.strip(' ,.;'))
    
print(li2)

newli = []

for i in li2:
    newli.append((i, li2.count(i)))
    
print(dict(set(newli)))
