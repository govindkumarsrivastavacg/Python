# 1.
# Write a program to print "Hello" five times using a for loop.

for i in range(1,6):
    print("Hello")


# 2.
# Print the numbers:

# 0 1 2 3 4 5 6 7 8 9
# using range().

for i in range(0,10):
    print(i)


# 3.
# Print the numbers from 1 to 10.

for i in range(1,11):
    print(i)


# 4.
# Print the numbers from 10 to 1 in reverse order.
for i in range(10,0,-1):
    print(i)


# 5.
# Print the numbers from 5 to 50, increasing by 5.

for i in range(5,51,5):
    print(i)


# 6.
# Print all even numbers from 2 to 20 using range().

for i in range(2,21,2):
    print(i)


# 7.
# Print all odd numbers from 1 to 19 using range().
for i in range(1,20,2):
    print(i)


# 8.
# Print the numbers:

# 3 6 9 12 15 18

for i in range(3,19,3):
    print(i,end="")


# 9.
# Print the numbers from 20 down to 2, decreasing by 2.

for i in range(20,0,-2):
    print(i)


# 10.
# Take a positive integer n from the user and print all numbers from 1 to n

n=int(input("enter a number:"))
for i in range(0,n+1):
    print(i)


# 11.
# Take n from the user and print only the even numbers from 1 to n.

n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%2==0):
        print(i)

# 12.
# Take n from the user and print only the odd numbers from 1 to n

n=int(input("Enter a number: "))
for i in range(1,n+1,2):
    print(i)


# 13.
# Take n from the user and print all numbers from 1 to n that are divisible by 3.

n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%3==0):
        print(i)

# 14.
# Take n from the user and print all numbers from 1 to n that are divisible by both 2 and 3.

n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%3==0 and i%2==0):
        print(i)

# 15.
# Take n from the user and count how many numbers from 1 to n are even.

n=int(input("Enter a number: "))
cnt=0
for i in range(1,n+1):
    if(i%2==0):
        cnt=cnt+1
print(cnt)
# 16.
# Take n from the user and calculate:

# 1 + 2 + 3 + ... + n
# using a for loop.

sum=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
    sum=sum+i
print(f"sum is {sum}")


# 17.
# Take n from the user and calculate the sum of all even numbers from 1 to n.

sum=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%2==0):
        sum=sum+i
print(f"sum is {sum}")

# 18.
# Take n from the user and calculate the sum of all odd numbers from 1 to n.

sum=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%2!=0):
        sum=sum+i
print(f"sum is {sum}")

# 19.
# Take a number from the user and print its multiplication table from 1 to 10.
n=int(input("Enter a number: "))
mul=1
for i in range(1,11):
    mul=mul*i
    print(f"{n}*{i}={mul}")

# 20.
# Take a number n and calculate:

# 1 × 2 × 3 × ... × n
# using a for loop.

n=int(input("Enter a number: "))
mul=1
for i in range(1,n+1):
    mul=mul*i
print(f"result is:{mul}")


# 21.
# Take a string from the user and print each character on a separate line.

a=input("Enter a string: ")
for i in a:
    print(i)

# 22.
# Take a string from the user and print all its characters on the same line using end="".

a=input("Enter a string: ")
for i in a:
    print(i,end="")


# 23.
# Take a string from the user and count the number of characters in it using a for loop.

a=input("Enter a string: ")
ctr=0
for i in a:
    ctr=ctr+1
print(f"Count is{ctr}")

# 24.
# Take a string from the user and count how many times the character "a" appears.

s=input("Enter a string")
ctr=0
for i in s:
    if (i=="a"):
        ctr+=1
print(f"a appears{ctr}times")


# 25.
# Take a string from the user and count how many characters are uppercase letters.

s=input("Enter a string: ")
ctr=0
for i in s:
    if(i.isupper):
        ctr+=1
print(f"There are {ctr} uppercase characters")


# 26.
# Use nested loops to print:

# ****
# ****
# ****

for row in range(1,4):
    for col in range(1,5):
        print("*",end="")
    print()



# 27.
# Use nested loops to print:

# *****
# *****
# *****
# *****

for row in range(1,5):
    for col in range(1,6):
        print("*",end="")
    print()




# 28.
# Print the following pattern:

# *
# **
# ***
# ****
# *****

for row in range(1,6):
    for col in range(row):
        print("*",end="")
    print()



# 29.
# Print the following pattern:

# 1
# 12
# 123
# 1234
# 12345


for row in range(1,6):
    n=1
    for col in range(row):
        print(n,end="")
        n+=1
    print()


# 30.
# Create a multiplication-table grid using nested for loops.

# For example, for numbers 1 to 5, produce rows showing their multiplication results.

for row in range(1,6):
    for col in range(1,6):
        print(row*col,end="\t")
    print()


# Final Practice Challenge
# Try to solve the following without copying an earlier example.

# Challenge
# Take a number n from the user and print:

# 1
# 12
# 123
# 1234
# ...
# until the last row contains n numbers.

# For example, if:

# n = 5
# output:

# 1
# 12
# 123
# 1234
# 12345


num=int(input("Enter the number of elements the last row should contain: "))
for row in range(1,num+1):
    n=1
    for col in range(row):
        print(n,end="")
        n+=1
    print()