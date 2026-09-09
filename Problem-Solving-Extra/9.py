# 9. Grade Calculator
# Take marks from the user.

# Use these rules:

# Marks	Grade
# 90–100	A
# 80–89	B
# 70–79	C
# 60–69	D
# 40–59	E
# Below 40	Fail
# Also handle marks below 0 and above 100 as invalid.

marks=int(input("Enter first number: "))
if(marks<0 or marks>100):
    print("Invalid marks")
elif(marks>=90):
    print("Grade:A")
elif(marks>=80):
    print("Grade:B")
elif(marks>=70):
    print("Grade:C")
elif(marks>=60):
    print("Grade:D")
elif(marks>=40):
    print("Grade:E")
else:
    print("Fail")