# 1. Print a Message N Times
# Write a recursive function that accepts a message and a positive integer n. Print the message exactly n times.

# Example:

# Input: message = "Hello", n = 3
# Output:
# Hello
# Hello
# Hello


# n=int(input("Enter how many times you want to print hello: "))
# def hello(n):
#     if n==0:
#         return
#     print("Hello")
#     hello(n-1)
# hello(n)


# 2. Print Even Numbers from 2 to N
# Write a recursive function that accepts a positive integer n and prints all even numbers from 2 up to n.

# Example:

# Input: n = 10
# Output: 2 4 6 8 10
# x=2
# n=int(input("Enter the number: "))
# def even(n,x):
#     if(x<=n):
#         print(x)
#     if x>=n:
#         return
#     even(n,x+2)
# even(n,x)



# 3. Find the Sum of Odd Numbers from 1 to N
# Write a recursive function that accepts a positive integer n and returns the sum of all odd numbers from 1 to n.

# Example:

# Input: n = 7
# Output: 16


# x=1
# sum=0
# n=int(input("Enter the number: "))
# def odd(n,x,sum):
#     if(x<=n):
#         sum+=x
#     if x>=n:
#         return sum
#     return odd(n,x+2,sum)
# print(odd(n,x,sum))


# 4. Count How Many Times a Digit Appears
# Write a recursive function that accepts a non-negative integer number and a digit target. Return how many times the target digit appears in the number.

# Do not convert the number into a string.

# Example:

# Input: number = 52525, target = 5
# Output: 3


# n=int(input("Enter a number: "))
# target=int(input("Enter the target: "))
# count=0
# def digit(n,count,target):
#     if n==0:
#         return count
#     if target==n%10:
#         count+=1
#     return digit(n//10,count,target)
# print(digit(n,count,target))




# 5. Find the Product of Digits
# Write a recursive function that accepts a non-negative integer and returns the product of its digits.

# Example:

# Input: 234
# Output: 24


# product=1
# n=int(input("Enter a number: "))
# def mul(n,product):
#     if n==0:
#         return product
#     product*=n%10
#     return mul(n//10,product)
# print(mul(n,product))


# 6. Find the First Digit of a Number
# Write a recursive function that accepts a non-negative integer and returns its first (leftmost) digit.

# Do not convert the number into a string.

# Example:

# Input: 5837
# Output: 5



# n=int(input("Enter the number: "))
# x=""
# def first(n,x):
#     if n==0:
#         return x
#     x=n%10
#     return first(n//10,x)
# print(first(n,x))


# 7. Check Whether a Number Contains a Digit
# Write a recursive function that accepts a non-negative integer number and a digit target. Return True if the target digit appears in the number. Otherwise, return False.

# Do not convert the number into a string.

# Example:

# Input: number = 4826, target = 8
# Output: True

# n=int(input("Enter a number: "))
# target=int(input("Enter a digit: "))
# flag=False
# def check(n,target,flag):
#     if flag:
#         return "True"
#     elif flag==False and n==0:
#         return "False"
#     if target==n%10:
#         flag=True
#     return check(n//10,target,flag)
# print(check(n,target,flag))


# 8. Find the Length of a String
# Write a recursive function that accepts a string and returns the number of characters in it.

# Do not use len(), loops, or slicing.

# Example:

# Input: "coding"
# Output: 6

# x=""
# count=0
# S=input("Enter a string: ")
# def length(S,x,count):
#     if x==S:
#         return count
#     x+=S[count]
#     return length(S,x,count+1)
# print(length(S,x,count))



# 9. Count Vowels in a String
# Write a recursive function that accepts a string and returns the total number of vowels (a, e, i, o, u).

# Assume the input contains lowercase English letters only.

# Do not use loops or slicing.

# Example:

# Input: "education"
# Output: 5

# i=0
# S=input("Enter a string: ")
# count=0
# def vowel(S,i,count):
#     if i==len(S)-1:
#         return count
#     if S[i] in "aeiou":
#         count+=1
#     return vowel(S,i+1,count)
# print(vowel(S,i,count))


# 10. Check Whether a String Is a Palindrome
# Write a recursive function that accepts a string and returns True if it reads the same forward and backward. Otherwise, return False.

# Do not use loops or slicing. The first function call should accept only the word. You may create an inner helper function to compare characters.

# Example:

# Input: "level"
# Output: True


# S=input("Enter a string: ")
# flag=False
# i=0
# x=""
# def pal(S,flag,x,i):
#     if flag:
#         return "False"
#     if len(x)==len(S) and flag==False:
#         return "True"
#     x+=S[len(S)-1-i]
#     if S[i]!=x[i]:
#         flag=True
#     return pal(S,flag,x,i+1)

    
# print(pal(S,flag,x,i))