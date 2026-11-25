# Q21. Count Digits in a Number
# Given a number, count how many digits it has. (Ignore sign.)

# Input: n = 0 → Output: 1
# Input: n = 1234 → Output: 4
# Input: n = -98 → Output: 2


# n=input("Enter a number: ")
# if("-" not in n):
#     ct=len(n)
# else:
#     ct=len(n)-1

# print(ct)


# Q22. Sum of Digits
# Given a number, find sum of its digits.

# Input: n = 123 → Output: 6 (1+2+3)
# Input: n = 505 → Output: 10 (5+0+5)
# Input: n = 9 → Output: 9

# sum=0
# n=int(input("Enter the number: "))
# while(n>0):
#     i=n%10
#     n=n//10
#     sum+=i
# print(f"The sum of the digits is {sum}")




# Q23. Product of Digits
# Given a number, find product of its digits.

# Input: n = 123 → Output: 6 (1×2×3)
# Input: n = 505 → Output: 0 (5×0×5)
# Input: n = 46 → Output: 24 (4×6

# mul=1
# n=input("Enter a number: ")
# for i in n:
#     if(i=='-'):
#         continue
#     mul*=int(i)
#     if(mul==0):
#         break
# print(mul)


# Q24. Reverse a Number
# Given a number, print its reverse.

# Input: n = 1234 → Output: 4321
# Input: n = 100 → Output: 1 (leading zeros dropped)
# Input: n = -321 → Output: -123 (if you handle sign)


# n = input("Enter a number: ").strip()

# rev = ""
# j = 0

# if n[0] == "-":
#     rev = "-"
#     j = 1

# for i in range(len(n) - 1, j - 1, -1):
#     rev += n[i]

# print(int(rev))


# Q25. Palindrome Number
# Check if a number reads same forwards and backwards.

# Input: n = 121 → Output: true (or "palindrome")
# Input: n = 123 → Output: false
# Input: n = 0 → Output: true


# flag_pal=False
# while(flag_pal==False):
#     i=0
#     flag_pal=True
#     Str=input("Enter The number: ").strip()
#     while(i<(len(Str)//2)):
#         if(Str[i]!=Str[len(Str)-i-1]):
#             flag_pal=False
#             break
#         i+=1
#     if(flag_pal):
#         print("The number is palindrome")
#     else:
#         print("The number is not Palindrome")
#         print("Try Again!")



# Q26. Prime Number (Simple Check)
# Given a number, check if it is prime.

# Input: n = 2 → Output: true
# Input: n = 17 → Output: true
# Input: n = 15 → Output: false


num=int(input("Enter a number: "))
if num<2:
    print("Neither prime nor composite")
else:
    i=2
    while(i*i<=num):
        if(num%i==0):
            print("Not a prime number")
            break
        i+=1
    else:
        print("Prime Number")