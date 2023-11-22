s1 = input("Enter a string : ").split(" ,")
n = int(input("Enter length : "))

for i in s1:
    if len(i) > n:
        print(i, end=",")