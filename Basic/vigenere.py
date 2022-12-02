# WAP to implement Vigenere substitution cipher

pt = input("Enter Text: ")
pt = pt.upper()
c = ''
d = ''
key = input("Enter Key: ")
key = key.upper()

for i in range(len(pt)):
    if (pt[i] != " "):
        ppt = ord(pt[i]) - 65
        pk = ord(key[i % len(key)]) - ord('A')
        x = ((ppt + pk) % 26) + 65
        c = c + chr(x)
    else:
        c = c + " "

print(c)


for i in range(len(pt)):
    if (c[i] != " "):
        ppt = ord(c[i]) - 65
        pk = ord(key[i % len(key)]) - ord('A')
        x = ((ppt - pk) % 26) + 65
        d = d + chr(x)
    else:
        d = d + " "

print(d)
