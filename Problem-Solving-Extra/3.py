# Largest of Two Numbers
# Take two numbers.

# Print:

# The larger number
# Both are equal if both numbers are the same
# Constraint
# Do not use max().

num1,num2=map(int,input("Enter the number: ").split())
if(num1>num2):
    print("The first number is larger")
elif(num2>num1):
    print("Second number is larger")
else:
    print("Both are equal")

