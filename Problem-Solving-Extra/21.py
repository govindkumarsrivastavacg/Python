# 21. Triangle Type
# Take three side lengths.

# First check whether they form a valid triangle.

# If valid, determine:

# Equilateral
# Isosceles
# Scalene
# Rules
# Equilateral → all three sides equal
# Isosceles   → exactly two sides equal
# Scalene     → all sides different

a,b,c=map(int,input("Enter the sides of the triangle").split())
if(a+b>c and a+c>b and b+c>a):
    print("Valid triangle")
    if(a==b and b==c):
        print("Equilateral Triangle")
    elif(a!=b and b!=c and c!=a):
        print("Scalene triangle")
    elif(a==b or b==c or c==a ):
        print("Isosceles Triangle")
else:
    print("Invalid triangle")