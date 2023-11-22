#n = int(input("Rows number - "))
n = 7

print("SQUARE BOX")
for x in range(n):
    for y in range(n):
        print("*", end=" ")
    print()
    
print("PATTERN 1")
for x in range(n):
    for y in range(n):
        if x >= y:
            print("*", end=" ")
        else :
            print(end=" ")
    print()
    
    
print("PATTERN 2")
for x in range(n):
    for y in range(n):
        if x > y:
            print(" ", end=" ")
        else :
            print("*", end=" ")
    print()
    
print("PATTERN 3")
for x in range(n):
    for y in range(n):
        if x + y > n - 1:
            print(" ", end=" ")
        else :
            print("*", end=" ")
    print()
    
print("PATTERN 4")
for x in range(n):
    for y in range(n):
        if x + y < n - 1:
            print(" ", end=" ")
        else :
            print("*", end=" ")
    print()
    
print("PATTERN 5")
for x in range(n):
    for y in range(n):
        if x>=y and x+y<n:
            print("*", end=" ")
    print()
    
print("PATTERN 6")
for x in range(n):
    for y in range(n+1):
        if x<y and x+y>=n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
print("PATTERN 7")
for x in range(n):
    for y in range(n):
        if x<=y and x+y<n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
print("PATTERN 8")
for x in range(n+1):
    for y in range(n):
        if y < x and x + y >= n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
print("PATTERN 9")
n = n // 2
for x in range(2*n+1):
    for y in range(2*n+1):
        if x>=y and x+y<=2*n or x<=y and x+y>=2*n :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    

print("PATTERN 10")
for x in range(2*n+1):
    for y in range(2*n+1):
        if x>=y and x+y >=2*n or x<=y and x+y<=2*n :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("PATTERN 11")
for x in range(2*n+1):
    for y in range(2*n+1):
        if x+y<=2*n and x+y >=2*n and x+y>=2*n and x+y>=2*n :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
