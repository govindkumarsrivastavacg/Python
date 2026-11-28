# 1. Add Two Numbers
# Create a lambda function that accepts two numbers and returns their sum.

# Sample values: 10, 20
# Expected output: 30

# sum=lambda  x,y:x+y
# print(sum(5,10))



# 2. Find the Square
# Create a lambda function that accepts one number and returns its square.

# Sample value: 6
# Expected output: 36


# square=lambda a:a*a
# print(square(9))


# 3. Find the Cube
# Create a lambda function that accepts one number and returns its cube.

# Sample value: 3
# Expected output: 27

# cube=lambda a:a**3
# print(cube(3))


# 4. Check Even or Odd
# Create a lambda function that accepts a number and returns "Even" if the number is even, otherwise returns "Odd".

# Sample value: 7
# Expected output: "Odd"


# check=lambda a:"Even" if a%2==0 else "Odd"
# print(check(7))


# 5. Find the Greater Num
# Create a lambda function that accepts two numbers and returns the greater number.

# Sample values: 45, 32
# Expected output: 45


# great=lambda a,b:a if a>b else b
# print(great(45,32))


# 6. Convert Celsius to Fahrenheit
# Create a lambda function that accepts a temperature in Celsius and converts it to Fahrenheit.

# Use this formula:

# Fahrenheit = (Celsius * 9/5) + 32

# Sample value: 25
# Expected output: 77.0


# convert=lambda c:(c*(9/5))+32
# print(convert(25))


# 7. Calculate the Length of a String
# Create a lambda function that accepts a string and returns the number of characters in it.

# Sample value: "Python"
# Expected output: 6


# length=lambda s:len(s)
# print(length("Python"))


# 8. Convert a String to Uppercase
# Create a lambda function that accepts a string and returns the string in uppercase.

# Sample value: "hello world"
# Expected output: "HELLO WORLD"

# to_upper=lambda s:s.upper()
# print(to_upper("hello world"))



# 9. Find the Last Character
# Create a lambda function that accepts a non-empty string and returns its last character.

# Sample value: "Coding"
# Expected output: "g"

# last=lambda s:s[-1]
# print(last("coding"))


# 10. Calculate the Final Price
# Create a lambda function that accepts the original price and discount percentage. Return the final price after applying the discount.

# Formula:

# Final Price = Original Price - (Original Price * Discount / 100)

# Sample values: Original price = 1000, Discount = 10
# Expected output: 900.0


# final=lambda p,d:p-(p*(d/100))
# print(final(1000,10))



# guess=lambda x:"Positive" if x>0 else "Negative" if x<0 else "Zero"
# print(guess(-3))