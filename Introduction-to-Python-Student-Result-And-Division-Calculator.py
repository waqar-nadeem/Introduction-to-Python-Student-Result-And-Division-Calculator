mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))

if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    average = (mark1 + mark2 + mark3) / 3
    print("Result: Pass")
    
    if average >= 60:
        print("Division: First Division")
    elif average >= 50:
        print("Division: Second Division")
    else:
        print("Division: Third Division")
else:
    print("Result: Fail")
