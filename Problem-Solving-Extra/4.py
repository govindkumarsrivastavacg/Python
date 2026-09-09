# Smallest of Three Numbers
# Take three numbers and find the smallest number.

# Constraint
# Do not use:

# min()
# Lists
# Sorting

a,b,c=map(int,input("Enter the numbers: ").split())
if(a<b and a<c):
    print(f"{a} is the smallest")
if(b<a and b<c):
    print(f"{b} is the smallest")
elif(c<a and c<b):
    print(f"{c} is the smallest")
else:
    print("Atleast two values are the smallest and equal")