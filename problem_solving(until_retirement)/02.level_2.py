# # Level 2 – Loops and basic calculations




# Q11. Print 1 to 10
# Print numbers from 1 to 10.

# Output: 1 2 3 4 5 6 7 8 9 10
# (No input, or you can just assume no parameter.)


# for i in range(1,11):
#     print(i)


# Q12. Print 1 to N
# Given N, print numbers from 1 to N.

# Input: N = 5 → Output: 1 2 3 4 5
# Input: N = 1 → Output: 1
# Input: N = 3 → Output: 1 2 3


# N=int(input("Enter the range: "))
# for i in range(1,N+1):
#     print(i)



# Q13. Even Numbers 1 to N
# Print all even numbers from 1 to N.

# Input: N = 10 → Output: 2 4 6 8 10
# Input: N = 7 → Output: 2 4 6
# Input: N = 2 → Output: 2



# N=int(input("Enter the range: "))
# for i in range(1,N+1):
#     if(i%2==0):
#         print(i)




# Q14. Odd Numbers 1 to N
# Print all odd numbers from 1 to N.

# Input: N = 10 → Output: 1 3 5 7 9
# Input: N = 5 → Output: 1 3 5
# Input: N = 1 → Output: 1


# N=int(input("Enter the range: "))
# for i in range(1,N+1):
#     if(i%2!=0):
#         print(i)


# Q15. Sum 1 to N
# Given N, find sum of numbers from 1 to N.

# Input: N = 5 → Output: 15 (1+2+3+4+5)
# Input: N = 1 → Output: 1
# Input: N = 10 → Output: 55

# sum =0
# N=int(input("Enter the range: "))
# for i in range(1,N+1):
#     sum=sum+i
# print(f"The sum is{sum}")


# Q16. Product 1 to N
# Given N, find product of numbers from 1 to N.

# Input: N = 4 → Output: 24 (1×2×3×4)
# Input: N = 1 → Output: 1
# Input: N = 5 → Output: 120

mul =1
N=int(input("Enter the range: "))
for i in range(1,N+1):
    mul=mul*i
print(f"The product is{mul}")



# Q17. Multiplication Table of a Number
# Print multiplication table of a given number up to 10.

# Input: n = 5 → Output: 5 10 15 20 25 30 35 40 45 50
# Input: n = 2 → Output: 2 4 6 8 10 12 14 16 18 20
# Input: n = 7 → Output: 7 14 21 28 35 42 49 56 63 70



N=int(input("Enter a number: "))
for i in range(1,11):
    print(N*i,end=" ")



# Q18. Count Numbers Divisible by 3 (1 to N)
# Count how many numbers between 1 and N are divisible by 3.

# Input: N = 10 → Numbers: 3, 6, 9 → Output: 3
# Input: N = 7 → Numbers: 3, 6 → Output: 2
# Input: N = 2 → No numbers → Output: 0

ct=0
N=int(input("Enter the range: "))
for i in range(1,N+1):
    if(i%3==0):
        ct+=1
print(f"{ct} numbers are divisible by 3")


# Q19. Factorial (Iterative)
# Compute N! using a loop.

# Input: N = 5 → Output: 120
# Input: N = 0 → Output: 1 (by definition)
# Input: N = 3 → Output: 6

num=int(input("Enter the number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"The factorial is: {fact}")

# Q20. First N Multiples of 7
# Print first N multiples of 7.

# Input: N = 3 → Output: 7 14 21
# Input: N = 5 → Output: 7 14 21 28 35
# Input: N = 1 → Output: 7

N=int(input("Enter the range of multiples: "))
for i in range(1,N+1):
    print(7*i,end=" ")
