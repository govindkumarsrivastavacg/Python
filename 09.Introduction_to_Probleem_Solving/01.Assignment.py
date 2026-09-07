# Problem 1
# Take two numbers and print the larger number.

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if(num1>num2):
    print("First number is larger")
elif(num1<num2):
    print("Second number is larger")
else:
    print(" Both numbers are equal")


# Problem 2
# Take a student's marks. Print:

# A if marks are 90 or above
# B if marks are 75–89
# C if marks are 50–74
# Fail if marks are below 50

marks=int(input("Enter your marks"))
if(marks>=90):
    print("A")
elif(marks>=75):
    print("B")
elif(marks>=50):

    print("C")
else:

    print("Fail")


# Problem 3
# Take the length and width of a rectangle and calculate:

# area
# perimeter

length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))
area = length*breadth
peri=2*(length+breadth)
print("Area of the rectangle is: ",area)
print("Perimeter of the rectangle is: ",peri)



# Problem 4
# Take a number and print whether it is:

# positive
# negative
# zero

num=int(input("Enter a number: "))
if(num>0):
    print("Number is positive")
elif(num<0):
    print("Number is negative")
else:
    print("Number is zero")



# Problem 5
# Take the price of an item. If the price is at least 1000, give a 10% discount. Print the final price.

price=float(input("Enter the price: "))
if(price>=1000):
        Total=price-(price/10)
else:
    Total=price
print("Total price is: ",Total)