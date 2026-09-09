# 17. Simple Calculator
# Take:

# First number
# Second number
# Operator
# Supported operators:

# +
# -
# *
# /
# Perform the appropriate calculation.

# Extra Condition
# If the operator is /, do not allow division by zero.

operator=int(input("Enter the operation you want to perform:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Floor division\n:"))
if(operator==1 or operator==2 or operator==3 or operator==4):
    num1=int(input("Enter first number:"))
    num2=int(input("enter second number:"))
    if(operator==1):
        sum=num1+num2
        print("Sum: ",sum)
    elif(operator==2):
        sub=num1-num2
        print(f"The subtraction is: {sub}")
    elif(operator==3):
        mul=num1*num2
        print(f"The result is: {mul}")
    elif(operator==4):
        if(num2==0):
            print("Cannot divide by zero")
        else:
            div=num1/num2
            print(f"The result is: {div}")
else:
    print("Enter a valid number")