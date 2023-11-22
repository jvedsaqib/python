marks = float(input("Enter marks - "))

if marks > 100 or marks < 0 :
    print("INVALID INPUT")
    
elif marks > 89 and marks <= 100 :
    print("GRADE A")
    
elif marks > 79 :
    print("GRADE B")
    
elif marks > 69 :
    print("GRADE C")
    
elif marks < 69 and marks >= 50 :
    print("GRADE D")
    
else :
    print("FAIL")