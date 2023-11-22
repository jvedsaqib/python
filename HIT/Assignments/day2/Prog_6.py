s1 = input("Enter comma seperated 4 - digit binary number : ").split(",")
k = 0
for i in s1 :
    s1[k] = "0b" + i
    k += 1

for i in s1:
    if int(i, 2) % 0b0011 == 0:
        print(i, end=",")