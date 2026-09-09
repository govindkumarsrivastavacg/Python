# 20. Triangle Validator
# Take three side lengths.

# Determine whether the three sides can form a triangle.

# Rule
# For a valid triangle:

# a + b > c
# a + c > b
# b + c > a

a,b,c=map(int,input("Enter the sides of the triangle").split())
if(a+b>c and a+c>b and b+c>a):
    print("Valid triangle")
else:
    print("Invalid triangle")