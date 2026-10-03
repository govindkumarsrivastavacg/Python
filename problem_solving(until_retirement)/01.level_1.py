# Level 1 – Basics (numbers, variables, if-else)




# Q1. Even or Odd
# Given a number, print whether it is "even" or "odd".

# Input: 4 → Output: "even"
# Input: 7 → Output: "odd"
# Input: 0 → Output: "even"

# n=int(input("Enter a number: "))
# if(n%2==0):
#     print("Even")
# else:
#     print("odd")


# Q2. Maximum of Two Numbers
# Given two numbers, print the larger one.

# Input: a = 5, b = 9 → Output: 9
# Input: a = 12, b = 3 → Output: 12
# Input: a = -4, b = -10 → Output: -4

# a,b=map(int,input("Enter two numbers: ").split())
# if(a>b):
#     print(f"{a} is greater than {b}")
# elif(b>a):
#     print(f"{b} is greater than {a}")
# else:
#     print("Both are equal")


# Q3. Maximum of Three Numbers
# Given three numbers, print the largest.

# Input: a = 3, b = 7, c = 5 → Output: 7
# Input: a = 10, b = 2, c = 10 → Output: 10
# Input: a = -1, b = -5, c = -3 → Output: -1



# a,b,c=map(int,input("Enter the numbers: ").split())
# if(a>b and a>c):
#     print(f"{a} is the greatest")
# elif(b>a and b>c):
#     print(f"{b} is the greatest")
# elif(c>a and c>b):
#     print(f"{c} is the greatest")
# else:
#     print("Atleast two values are equal and highest")



# Q4. Positive, Negative, or Zero
# Given a number, print "positive", "negative", or "zero".

# Input: 8 → Output: "positive"
# Input: -2 → Output: "negative"
# Input: 0 → Output: "zero"


# num=int(input("Enter a number: "))
# if(num>0):
#     print("Number is positive")
# elif(num<0):
#     print("Number is negative")
# else:
#     print("Number is zero")


# Q5. Age Group
# Given an age, print whether the person is "child", "teenager", or "adult" (you can assume: 0–12 child, 13–19 teenager, 20+ adult).

# Input: age = 8 → Output: "child"
# Input: age = 15 → Output: "teenager"
# Input: age = 25 → Output: "adult"

age=int(input("Enter your age: "))
if(age>=0 and age<=12):
    print("You are a child")
elif(age>=13 and age<=19):
    print("You are a teenager")
elif(age>=20):
    print("You are an adult")




# Q6. Grade Calculator
# Given marks 0–100, print grade.

# Example mapping:

# 90–100 → A

# 80–89 → B

# 70–79 → C

# 60–69 → D

# 0–59 → F

# Input: marks = 92 → Output: "A"

# Input: marks = 75 → Output: "C"

# Input: marks = 40 → Output: "F"


# marks2=int(input("Enter your marks: "))
# if(marks2>=90):
#     print("A")
# elif(marks2>=80):
#     print("B")
# elif(marks2>=70):
#     print("C")
# elif(marks2>=60):
#     print("D")
# else:
#     print("F")

# Q7. Divisible by 5
# Given a number, print whether it is divisible by 5.

# Input: 10 → Output: "divisible by 5"
# Input: 11 → Output: "not divisible by 5"
# Input: 0 → Output: "divisible by 5"

# num=int(input("Enter a number: "))
# if(num%5==0):
#     print("Number is divisible by 5")
# else:
#     print("Number is not divisible by 5")


# Q8. Divisible by 3 and 5
# Given a number, print if it is divisible by both 3 and 5.

# Input: 15 → Output: "divisible by 3 and 5"
# Input: 30 → Output: "divisible by 3 and 5"
# Input: 9 → Output: "not divisible by both"



# num=int(input("Enter a number: "))
# if(num%5==0) and num%3==0:
#     print("Number is divisible by 5 and 3")
# else:
#     print("Number is not divisible by 5 and 3")



# Given a year, check if it is a leap year. (Simple version: divisible by 4 → leap; you can refine later.)

# Input: 2020 → Output: "leap year"
# Input: 2021 → Output: "not a leap year"
# Input: 2000 (if using full rule: divisible by 400) → Output: "leap year"

yr=int(input("enter the year: "))
if(yr%400==0):
    print("Leap year")
elif(yr%100!=0 and yr%4==0):
    print("Leap year")
else:
    print("Not a leap year")


# Q10. In Range 10–50
# Given a number, check if it lies between 10 and 50 (inclusive).

# Input: 25 → Output: "in range"
# Input: 10 → Output: "in range"
# Input: 7 → Output: "out of range"


num=int(input("Enter the number: "))
if(num>=10 and num<=50):
    print("In range")
else:
    print("Not in range")