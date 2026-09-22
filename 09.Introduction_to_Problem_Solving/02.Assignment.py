# Problem 1
# Take two numbers and print their sum.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
print(f"The sum of the two numbers is:: {sum}")

# IPO

#INPUT
#     num1
#     num2
# PROCESSING
#     Add the two numbers
# OUTPUT
#     sum

# ALGORITHM

# 1.start
# 2.read first number
# 3.read second number
# 4.add first number with the second
# 5.store result
# 6.print result
# 7.stop


# DRY RUN

# 1. INPUT 2,3
#     Result 5

# 2. INPUT -1,5
#     Result 4

# Problem 2
# Take a number and print whether it is even or odd.
num=int(input("Enter number: "))
if(num%2==0):
    print("Number is odd")
else:
    print("Number is even")



# INPUT
#     Number

# PROCESSING
#     Check number % 2
#     If remainder is 0 → Even
#     Otherwise → Odd

# OUTPUT
#     Even or Odd


# ALGORITHM
# 1.Start
# 2.read number
# 3.If number%2==0:
#     Print Even
# 4.Otherwise:
#     Print Odd
# 5.Stop

# DRY RUN

# 1.Input 5
#   Condition otherwise
#   result Odd

# 2.Input 8
#   Condition 8%2==0
#   result Even


# Problem 3
# Take three numbers and print the largest number.

n1,n2,n3=map(int,input("Enter the numbers: ").split())
if(n1>n2 and n1>n3):
    print(f"{n1} is the largest of the three")
elif(n2>n1 and n2>n3):
    print(f"{n2} is the largest of the three")
elif(n3>n1 and n3>n2):
    print(f"{n3} is the largest of the three")
else:
    print("Atleast 2 values are equal and largest")

# IPO


# INPUT
#   n1
    # n2
    # n3    
# PROCESSING
#     Check n1>n2 and n3
#     If True Print-> n1 is the largest
#     check n2>n3 and n1
#     If True Print-> n2 is the largest
#     Otherwise → n3 is the largest

# OUTPUT
#     N1 or N2 or N3

# Algorithm
# 1.Start
# 2.Read first number
# 3.Read second number
# 4.Read third number
# 5.If first number is greater than second number and third number:
#        Print first number
# 6.If second number is greater than first number and third number:
#        Print first number
# 7.If third number is greater than second number and first number:
#        Print first number
# 8.Stop


# DRY Run

# 1.  Input:4,5,6
#     condition:6>4 and 6>5
#     result 6
# 2.  Input:-9,0,-10
#     condition:0>-9 and 0>-10
#     result 0

# Problem 4
# Take a person's age and print whether they are eligible to vote. Assume the minimum age is 18.

age=int(input("Enter the age: "))
if(age>=18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# IPO


# INPUT
    # age  
# PROCESSING
#     Check age>=18
#     If True->Eligible to vote
    #   Otherwise->Not eligible to vote
# OUTPUT
#     Eligible to vote or Not eligible to vote


# Problem 5
# Take the price of an item. Give a 20% discount when the price is greater than or equal to 2000. Print the final price.

price=int(input("Enter price: "))
dis=price*(20/100)
if(price>=2000):
    print(f"The total price is: {price-dis}")
else:
    print(f"The total price is: {price}")


# Problem 6
# Take three subject marks and calculate the average. Print Pass if the average is at least 40; otherwise print Fail.

m1,m2,m3=map(int,input("Enter the marks:").split())
avg=(m1+m2+m3)/3
if(avg>=40):
    print("Pass")
else:
    print("Fail")
    