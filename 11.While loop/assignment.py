# # 1.
# # Write a program to print "Hello" five times using a for loop.

# i=0
# while(i<5):
#     print("Hello")
#     i+=1


# # 2.
# # Print the numbers:

# # 0 1 2 3 4 5 6 7 8 9


# i=0
# while(i<10):
#     print(i)
#     i+=1



# # 3.
# # Print the numbers from 1 to 10.


# i=1
# while(i<11):
#     print(i)
#     i+=1


# # 4.
# # Print the numbers from 10 to 1 in reverse order.


# i=10
# while(i>0):
#     print(i)
#     i-=1



# # 5.
# # Print the numbers from 5 to 50, increasing by 5.

# i=5
# while(i<51):
#     print(i)
#     i+=5



# # 6.
# # Print all even numbers from 2 to 20


# i=2
# while(i<=20):
#     print(i)
#     i+=2


# # 7.
# # Print all odd numbers from 1 to 19


# i=1
# while(i<20):
#     print(i)
#     i+=2


# # 8.
# # Print the numbers:

# # 3 6 9 12 15 18


# i=3
# while(i<19):
#     print(i)
#     i+=3


# # 9.
# # Print the numbers from 20 down to 2, decreasing by 2.


# i=20
# while(i>1):
#     print(i)
#     i-=2




# # 10.
# # Take a positive integer n from the user and print all numbers from 1 to n.

# i=1
# n=int(input("Enter a number: "))
# while(i<=n):
#     print(i)
#     i+=1



# # 11.
# # Take n from the user and print only the even numbers from 1 to n.


# i=2
# n=int(input("Enter a number: "))
# while(i<=n):
#     print(i)
#     i+=2



# # 12.
# # Take n from the user and print only the odd numbers from 1 to n


# i=1
# n=int(input("Enter a number: "))
# while(i<=n):
#     print(i)
#     i+=2



# # 13.
# # Take n from the user and print all numbers from 1 to n that are divisible by 3.

# i=1
# n=int(input("Enter a number: "))
# while(i<=n):
#     if(i%3==0):
#         print(i)
#     i+=1


# # 14.
# # Take n from the user and print all numbers from 1 to n that are divisible by both 2 and 3.
    

# i=1
# n=int(input("Enter a number: "))
# while(i<=n):
#     if(i%3==0 and i%2==0):
#         print(i)
#     i+=1



# # 15.
# # Take n from the user and count how many numbers from 1 to n are even.

# count=0
# i=1
# n=int(input("Enter a number: "))
# while(i<=n):
#     if(i%2==0):
#         count+=1
#     i+=1



# # 16.
# # Take n from the user and calculate:

# # 1 + 2 + 3 + ... + n


# i=1
# sum=0
# n=int(input("Enter a number: "))
# while(i<=n):
#     sum=sum+1
#     i+=1
# print(f"The sum is {sum}")


# # 17.
# # Take n from the user and calculate the sum of all even numbers from 1 to n.

# i=1
# sum=0
# n=int(input("Enter a number: "))
# while(i<=n):
#     if(i%2==0):
#         sum=sum+1
#     i+=1
# print(f"The sum is {sum}")



# # 18.
# # Take n from the user and calculate the sum of all odd numbers from 1 to n.


# i=1
# sum=0
# n=int(input("Enter a number: "))
# while(i<=n):
#     if(i%2!=0):
#         sum=sum+1
#     i+=1
# print(f"The sum is {sum}")



# # 19.
# # Take a number from the user and print its multiplication table from 1 to 10.

# i=1
# n=int(input("Enter a number: "))
# while(i<=n):
#     print(n*i)
#     i+=1


# # 20.
# # Take a number n and calculate:

# # 1 × 2 × 3 × ... × n



# i=1
# mul=1
# n=int(input("Enter a number: "))
# while(i<=n):
#     mul=mul*i
#     i+=1
# print(f"The result is {mul}")



# # 21.
# # Take a string from the user and print each character on a separate line.

# Str=input("Enter a string: ")
# i=0
# while(i<len(Str)):
#     print(Str[i])
#     i+=1


# # 22.
# # Take a string from the user and print all its characters on the same line using end="".

# Str=input("Enter a string: ")
# i=0
# while(i<len(Str)):
#     print(Str[i],end="")
#     i+=1


# # 23.
# # Take a string from the user and count the number of characters in it using a for loop.

# count=0
# Str=input("Enter a string: ")
# i=0
# while(i<len(Str)):
#     count+=1
#     i+=1

# print("The number of characters in string are: ",count)



# # 24.
# # Take a string from the user and count how many times the character "a" appears.

# count=0
# i=0
# Str=input("Enter a string: ")
# while(i < len(Str)):
#     if(Str[i]=="a"):
#         count+=1
#     i+=1
# print(f"'a' appears {count} times in the string.")



# 25.
# Take a string from the user and count how many characters are uppercase letters


# count=0
# i=0
# Str=input("Enter a string: ")
# while(i < len(Str)):
#     if(Str[i]>='A' and Str[i]<='Z'):
#         count+=1
#     i+=1
# print(f" Number of uppercase letters are: {count}")



# 26.
# Use nested loops to print:

# ****
# ****
# ****


# i=0
# while(i<3):
#     j=0
#     while(j<4):
#         print("*",end="")
#         j+=1
#     print()
#     i+=1


# 27.
# Use nested loops to print:

# *****
# *****
# *****
# *****


# i=0
# while(i<4):
#     j=0
#     while(j<5):
#         print("*",end="")
#         j+=1
#     print()
#     i+=1



# 28.
# Print the following pattern:

# *
# **
# ***
# ****
# *****

# i=1
# while(i<=5):
#     j=0
#     while(j<i):
#         print("*",end="")
#         j+=1
#     print()
#     i+=1


# 29.
# Print the following pattern:

# 1
# 12
# 123
# 1234
# 12345

# i=1
# while(i<=5):
#     j=0
#     num=1
#     while(j<i):
#         print(num,end="")
#         num+=1
#         j+=1
#     print()
#     i+=1


# 30.
# Create a multiplication-table grid using nested for loops.

# For example, for numbers 1 to 5, produce rows showing their multiplication results.


i=1
while(i<6):
    j=1
    while(j<=10):
        print(f"{i} * {j} = {i*j}")
        j+=1
    print()
    i+=1