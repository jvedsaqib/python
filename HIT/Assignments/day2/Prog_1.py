s1 = input("Enter a string : ")
s1 = "".join(s1.split()).upper()

if s1 == s1[::-1]:
    print("Palindrome")
else:
    print("Not")