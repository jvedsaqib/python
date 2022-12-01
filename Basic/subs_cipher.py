# WAP to implement substitution cipher

s = input("Enter Text: ")

res = []
result = ''
s = s.upper()
str_list = list(s)
#print(str_list)
base = ord('A')
key = int(input("Enter Key: "))

for i in str_list:
    val = ((ord(i) - base) + key) % 26
    res.append(chr(base + val))

for j in res:
    result += j

print(s)
print(result)

