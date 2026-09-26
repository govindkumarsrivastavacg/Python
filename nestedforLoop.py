# 1. Print a 3×3 Star Grid
# Write a Python program to print:

# * * *
# * * *
# * * *


# for i in range(3):
#     for j in range(3):
#         print("*",end="")
#     print()



# 2. Print Numbers in Rows
# Write a Python program to print:

# 1 2 3
# 1 2 3
# 1 2 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end="")
#     print()



# 3. Print Row Numbers
# Write a Python program to print:

# 1 1 1
# 2 2 2
# 3 3 3


# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end="")
#     print()



# 4. Increasing Star Pattern
# Write a Python program to print:

# *
# * *
# * * *
# * * * *
# * * * * *


# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()


# 5. Decreasing Star Pattern
# Write a Python program to print:

# * * * * *
# * * * *
# * * *
# * *
# *


# n=int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()




# 6. Increasing Number Pattern
# Write a Python program to print:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



# 7. Repeated Number Pattern
# Write a Python program to print:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print() 


# for i in range(1,6):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")
#     print()


# 9. Multiplication Grid
# Write a Python program to print:

# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15


# for i in range(1,4):
#     for j in range(1,6):
#         print(f"{i*j}",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(j**2,end=" ")
#     print()


# 11. Alphabet Pattern
# Write a Python program to print:

# A
# A B
# A B C
# A B C D
# A B C D E


# Str="ABCDE"
# for i in range(len(Str)):
#     for j in range(i+1):
#         print(Str[j],end="")
#     print()


# 12. Repeated Alphabet Pattern
# Write a Python program to print:

# A
# B B
# C C C
# D D D D
# E E E E E

# Str="ABCDE"
# for i in range(len(Str)):
#     for j in range(i+1):
#         print(Str[i],end="")
#     print()



# 13. Odd Number Pattern
# Write a Python program to print:

# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9


# for i in range(5):
#     x=1
#     print(x,end=" ")
#     for j in range(1,i+1):
#         print(x+2,end=" ")
#         x+=2
#     print()



# 14. Even Number Pattern
# Write a Python program to print:

# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
        

# for i in range(5):
#     x=2
#     print(x,end=" ")
#     for j in range(1,i+1):
#         print(x+2,end=" ")
#         x+=2
#     print()




# 15. 5×5 Star Square
# Write a Python program to print:

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *



# for i in range(5):
#     for j in range(5):
#         print("* ",end="")
#     print()



# 16. 5×5 Number Square
# Write a Python program to print:

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


# for i in range(5):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()



# 17.. Row-wise Numbers
# Write a Python program to print:

# 1 2 3
# 4 5 6
# 7 8 9



x=1
for i in range(3):
    for j in range(3):
        print(x,end=" ")
        x+=1
    print()




# 18. Print 1 to 20 in 4 Rows
# Write a Python program to print numbers from 1 to 20 in 4 rows, with 5 numbers in each row.

# Expected output:

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20

# x=1
# for i in range(4):
#     for j in range(5):
#         print(x,end=" ")
#         x+=1
#     print()


# 19. Print Coordinate Pairs
# Write a Python program to print:

# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)


# for i in range(1,4):
#     for j in range(1,4):
#         print(f"({i},{j})",end=" ")
#     print()


# 20. Print All Number Combinations
# For numbers from 1 to 3, print every possible pair:

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{i} {j}")



# 22. Repeated Number Pattern
# Write a Python program to print:

# 1
# 22
# 333
# 4444
# 55555


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print() 



# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


    
# 24. Reverse Number Pattern
# Write a Python program to print:

# 54321
# 5432
# 543
# 54
# 5

# for i in range(5,0,-1):
#     for j in range(5,5-i,-1):
#         print(j,end=" ")
#     print()




# 25. Repeated Row Number Pattern
# Write a Python program to print:

# 11111
# 22222
# 33333
# 44444
# 55555

# n=int(input("Enter the number of rows you want: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end="")
#     print()

