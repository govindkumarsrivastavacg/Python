# 1. Sum of Digits at Even Positions
# Write a recursive function that accepts a positive integer and returns the sum of the digits at even positions, counting positions from the rightmost digit as position 1.

# Example:
# Input: 583246
# Output: 12


# total=0
# x=-1
# n=input("enter a number")
# l=-1*len(n)

# def sum(n,l,x):
#     global total
#     if x==l:
#         if x%2==0:
#             total+=int(n[x])
#         return
#     if x%2==0:
#         total+=int(n[x])
#     sum(n,l,x-1)
#     return total
# print(sum(n,l,x))



# 2. Reverse a Number Without Converting It to a String
# Write a recursive function that accepts a positive integer and returns the number with its digits in reverse order. Do not convert the number into a string.

# Example:
# Input: 4827
# Output: 7284


# x=""
# n=int(input("Enter the number: "))
# def rev(n,x):
#     if n==0:
#         return x
#     x += str(n%10)
#     return rev(n//10,x)
    
# print(int(rev(n,x)))


# 3. Check Whether a String Is a Palindrome
# Write a recursive function that accepts a string and returns whether it reads the same forward and backward. The function must compare characters recursively without using loops or slicing.

# Example:
# Input: level
# Output: True


# i=-1
# rev=""
# Str=input("Enter a string: ").lower()
# def pal(Str,rev,i):
#     if len(Str)==len(rev):
#         if Str==rev:
#             return "True"
#         else:
#             return "False"
#     rev+=Str[i]
#     return pal(Str,rev,i-1)
# print(pal(Str,rev,i))




# 4. Count a Character in a String
# Write a recursive function that accepts a string and a character. Return how many times that character appears in the string. Treat uppercase and lowercase characters as different.

# Example:
# Input: programming, m
# Output: 2


# Str=input("Enter the string: ")
# c=input("Enter the character you wish to count: ")
# x=0
# y=0
# def counter(Str,c,x,y):
#     if y==len(Str)-1:
#         return x
#     if Str[y]==c:
#         x+=1
#     return counter(Str,c,x,y+1)
# print(counter(Str,c,x,y))


# 5. Find the Greatest Common Divisor
# Write a recursive function that accepts two positive integers and returns their greatest common divisor (GCD). Do not use built-in GCD functions.

# Example:
# Input: 48, 18
# Output: 6

# n1=int(input("Enter the first number: "))
# n2=int(input("Enter the second number: "))
# small=n1
# if n2<n1:
#     small=n2
# def gcd(n1,n2,small):
#     if n1%small==0 and n2%small==0:
#         return small
#     return gcd(n1,n2,small-1)
# print(gcd(n1,n2,small))



# 6. Check Whether a Number Is a Prime Number
# Write a recursive function that accepts an integer greater than 1 and checks whether it is prime. Use recursion to test possible divisors. Do not use loops.

# Example:
# Input: 29
# Output: True

# flag=False
# x=2
# n=int(input("Enter a number: "))
# def prime(n,flag,x):
#     if n%x==0:
#         flag=True
#     if flag==True or n==2:
#         return "Not a prime number"
#     elif flag==False and x==n-1:
#         return "It is a prime number"
#     return prime(n,flag,x+1)
# print(prime(n,flag,x))


# 7. Remove All Occurrences of a Character
# Write a recursive function that accepts a string and a character. Return a new string with every occurrence of that character removed. Do not use the built-in replace() method.

# Example:
# Input: mississippi, s
# Output: miippi

# x=0
# new=""
# old=input("Enter the old string: ")
# c=input("Enter a character present inside the old string: ")
# if c not in old:
#     print("You do have eyes right?")

# else:
#     l=len(old)
#     def replace_string(old,new,l,x,c):
#         if x==l-1:
#            if old[x]!=c:
#                 new+=old[x] 
#                 return new
#         if old[x]!=c:
#             new+=old[x]
#         return replace_string(old,new,l,x+1,c)

#     print(replace_string(old,new,l,x,c))



# 8. Convert a Decimal Number to Binary
# Write a recursive function that accepts a non-negative decimal integer and returns its binary representation as a string. Do not use bin().

# Example:
# Input: 13
# Output: 1101

# n=int(input("Enter the number: "))
# s=""
# def binary(n,s):
#     if n==0:
#         return s[::-1]
#     s=s+str(n%2)
#     return binary(n//2,s)
# print(binary(n,s))


# 9. Check Whether a String Contains Only Digits
# Write a recursive function that accepts a non-empty string and checks whether every character is a digit from 0 to 9. Do not use loops or the built-in isdigit() method.

# Example:
# Input: 50291
# Output: True

# flag=False
# S=input("Enter a string:")
# l=len(S)

# def isdigit(S,l,flag):
#     if S[l-1] not in "`1234567890":
#             flag=True
#     if flag:
#         return "It does not contain only digits"
#     if flag==False and l==0 and S[0] in "1234567890":
#          return "It does contain only digits"
#     return isdigit(S,l-1,flag)
         
    
# print(isdigit(S,l,flag))




# 10. Find the Digital Root
# Write a recursive function that accepts a positive integer and repeatedly adds its digits until only one digit remains. Return that final digit.

# Example:
# Input: 9875
# Output: 2
# (First: 9 + 8 + 7 + 5 = 29; then: 2 + 9 = 11; then: 1 + 1 = 2.)

# x=0
# sum=0
# y=0
# N=int(input("Enter a number: "))
# n=str(N)

# def root(n,sum,x,y):
#     sum+=int(n[x])

#     if x==len(n)-1:
#         if len(str(sum))==1:
#             return sum
#         else:
#             n=str(sum)
#             sum=0
#             x=0
#             y+=1
#             return root(n,sum,x,y)

#     return root(n,sum,x+1,y)

# print(root(n,sum,x,y))