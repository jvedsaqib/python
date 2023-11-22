# 6. Remove all duplicates words from a givensentence.

s = "Hello I am Saqib Hi Saqib"

print(str(set(s.split())))

s1 = " ".join(set(s.split()))
print(s1)