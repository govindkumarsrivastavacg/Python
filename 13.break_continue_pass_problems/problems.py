# Practice Problems: break


# Problem 1
# Print numbers from 1 to 10, but stop when the number becomes 6.

# Expected output:

# 1
# 2
# 3
# 4
# 5


# for i in range(1,11):
#     if(i==6):
#         break
#     else:
#         print(i)


# Problem 2
# Given:

# numbers = [10, 20, 30, 40, 50]
# Search for 30.

# Once found, print:

# Found
# and stop the loop.

# l=[10,20,30,40,50]
# for i in l:
#     if(i==30):
#         print("Found")
#         break
# else:
#     print("Not found")


# Problem 3
# Take numbers from the user continuously.

# Stop when the user enters 0.

# while(True):
#     num=int(input("Enter a number: "))
#     if(num==0):
#         break


# Problem 4
# Print numbers from 1 to 100, but stop when you reach the first number divisible by 17.

# for i in range(1,101):
#     if(i%17==0):
#         break
#     else:
#         print(i)



# Practice Problems: continue


# Problem 1
# Print numbers from 1 to 20, but skip all even numbers.

# Expected output:

# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

# for i in range(1,21):
#     if(i%2==0):
#         continue
#     else:
#         print(i)


# Problem 2
# Given:

# numbers = [10, -2, 30, -5, 40, -8]
# Print only positive numbers using continue.

# Expected output:

# 10
# 30
# 40

# num=[10,-2,30,-5,40,-8]
# for i in num:
#     if(i<0):
#         continue
#     else:
#         print(i)


# Problem 3
# Print numbers from 1 to 20.

# Skip numbers divisible by 3.

# for i in range(1,21):
#     if(i%3==0):
#         continue
#     else:
#         print(i)


# Problem 4
# Given:

# numbers = [5, 12, 8, 21, 30, 7]
# Print only numbers greater than 10.

# Use continue.

# num=[5,12,8,21,30,7]
# for i in num:
#     if(i<=10):
#         continue
#     else:
#         print(i)


# Problem 5
# Write a program that checks whether a number is positive.

# For now, leave the positive case empty using pass.

# num=int(input("Enter a number: "))
# if(num>=0):
#     pass
# else:
#     print("Negative")



# Challenge 1
# Write a program that keeps asking the user for numbers.

# Rules:

# Positive number → print it.
# Negative number → skip it using continue.
# 0 → stop using break.


# while(True):
#     num=int(input("Enter a number: "))
#     if(num>0):
#         print(num)
#     elif(num<0):
#         continue
#     else:
#         break


# Challenge 2
# Given:

# numbers = [12, 5, -4, 18, 0, 25, 30]
# Process the list using these rules:

# Negative number → skip.
# 0 → stop.
# Positive number → print.
# Expected output:

# 12
# 5
# 18


# num=[12,5,-4,18,0,25,30]
# for i in num:
#     if(i>0):
#         print(i)
#     elif(i<0):
#         continue
#     else:
#         break


# Challenge 3
# Write a program that searches for a number in a list.

# If found:

# Number found
# If the loop finishes without finding it:

# Number not found

# Hint: Use break and loop else.


# x=int(input("Enter how many numbers you want: "))
# l=[]
# for i in range(x):
#     Num=int(input("Enter a number: "))
#     l.append(Num)
# search=int(input("Enter the nnumber you want to search"))
# for i in range(len(l)):
#     if(i==search):
#         print("Found")
#         break
# else:
#     print("Number not found")