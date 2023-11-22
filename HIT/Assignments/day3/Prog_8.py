# 8) Given a dictionary, which contains domain names as keys, 
# and a list of users as values, generate a list
# that contains complete email addresses.

# Input: {"gmail.com": ["paul.buchheit", "sanjeev.singh", "kevin.fox"], "yahoo.com":
# ["jerry.yang", "david.filo"], "hotmail.com": ["sabeer.bhatia"]}

# Output: ['paul.buchheit@gmail.com', 'sanjeev.singh@gmail.com', 'kevin.fox@gmail.com',
# 'jerry.yang@yahoo.com', 'david.filo@yahoo.com', 'sabeer.bhatia@hotmail.com']

di = {
      "gmail.com": ["paul.buchheit", "sanjeev.singh", "kevin.fox"],
      "yahoo.com": ["jerry.yang", "david.filo"],
      "hotmail.com": ["sabeer.bhatia"]
      }

newli = []

for key, val in di.items():
    for i in val:
        newli.append("@".join((i,key)))
        
print(newli)