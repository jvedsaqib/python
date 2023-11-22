s1 = input("Enter name : ").split()

if len(s1) > 1:
    k = 0
    for i in s1:
        if i != s1[-1]:
            print(s1[k][0].upper(), end=". ")
            k += 1
        else:
            print(s1[-1].title())
else :
    print(s1[0].title())