myStr = "hahahaha"
l1 = []
substr = "haha"
c = 0
for i in range(len(myStr)):
    if myStr[i:i+len(substr)] == substr:
        c += 1
        
print(f"Count is {c}")