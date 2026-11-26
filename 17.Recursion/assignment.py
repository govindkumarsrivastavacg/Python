# 5. Count down (4 marks)
# Write countdown(n) that prints every integer from n down to 1, then prints "Done!".

# Constraint: n is a non-negative integer.

# Examples:

# countdown(3)
# Output:

# 3
# 2
# 1
# Done!
# Edge case: countdown(0) should print only Done!.



# n=int(input("Enter the number: "))
# def countdown(n):
#     if n==0:
#         print("Done!")
#         return
#     print(n)
#     countdown(n-1)
# countdown(n)



# 6. Count up (4 marks)
# Write count_up(n) that prints numbers from 1 through n in ascending order.

# Example:

# count_up(4)
# Output:

# 1
# 2
# 3
# 4
# Edge case: count_up(0) should print nothing.


# n=int(input("Enter the number: "))
# def countdown(n):
#     if n==0:
#         return
#     countdown(n-1)
#     print(n)
# countdown(n)


# 7. Sum from 1 to n (4 marks)
# Write sum_to(n) that returns the sum of all integers from 1 through n.

# Examples:

# print(sum_to(5))  # 15
# print(sum_to(0))  # 0
# Constraint: n is a non-negative integer.


# n=int(input("Enter the number: "))
# def sum(n):
#     if(n==0):
#         return 0
#     return n+sum(n-1)
# total=sum(n)
# print(total)



# 8. Factorial (4 marks)
# Write factorial(n) that returns n!.

# Examples:

# print(factorial(4))  # 24
# print(factorial(0))  # 1
# Constraint: n is a non-negative integer.

# n=int(input("Enter the number: "))
# def fac(n):
#     if n==0:
#         return 1
#     return n*fac(n-1)
# print(fac(n))



# 9. Sum of digits (4 marks)
# Write digit_sum(n) that returns the sum of the digits of a non-negative integer.

# Examples:

# print(digit_sum(583))  # 16
# print(digit_sum(7))    # 7
# print(digit_sum(0))    # 0
# Hint: % 10 gets the last digit; // 10 removes the last digit.

# n=int(input("enter the number: "))
# def sum(n):
#     if n==0:
#         return 0
#     return n%10+sum(n//10)
# print(sum(n))


# 10. Power (5 marks)
# Write power(base, exponent) that returns base raised to exponent.

# Examples:

# print(power(2, 5))  # 32
# print(power(9, 0))  # 1
# print(power(3, 1))  # 3
# Constraint: exponent is a non-negative integer. Do not use ** in your function.



# x=int(input("Enter the number: "))
# y=int(input("Enter the power: "))
# def power(x,y):
#     if(y==0):
#         return 1
#     return x*power(x,y-1)
# print(power(x,y))




# 11. Count digits (5 marks)
# Write count_digits(n) that returns the number of digits in a non-negative integer.

# Examples:

# print(count_digits(5382))  # 4
# print(count_digits(6))     # 1
# print(count_digits(0))     # 1
# Hint: Each recursive call removes the last digit using // 10. Be careful with 0.

# a=0
# n=int(input("Enter the number: "))
# def count_digits(n):
#     if n==0:
#         return 1
#     global a
#     a+=1
#     count_digits(n//10)
#     return a
# print(count_digits(n))




# 12. Reverse a number as a string (5 marks)
# Write reverse_text(text) that returns the characters of a string in reverse order using recursion.

# Examples:

# print(reverse_text("cat"))  # "tac"
# print(reverse_text("a"))    # "a"
# print(reverse_text(""))     # ""
# Hint: Take the last character and combine it with the reverse of the remaining string, or take the first character and place it after the reversed remainder.

# S=""
# Str=input("Enter a string: ")
# a=1
# def reverse_text(Str):
#     global S
#     global a
#     if len(S)==len(Str):
#         return S
#     S+=Str[len(Str)-a]
#     a+=1
#     return reverse_text(Str)
    
# print(reverse_text(Str))



# 13. Fibonacci number (5 marks)
# Write fibonacci(n) that returns the nth Fibonacci number using these definitions:

# fibonacci(0) = 0
# fibonacci(1) = 1
# Otherwise, fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
# Examples:

# print(fibonacci(0))  # 0
# print(fibonacci(1))  # 1
# print(fibonacci(6))  # 8
# Constraint: n is a non-negative integer. Test only small values because this basic recursive method repeats calculations.


# n=int(input("Enter a number: "))
# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(n))





# 14. Find the maximum digit (5 marks)
# Write max_digit(n) that returns the largest digit in a non-negative integer.

# Examples:

# print(max_digit(4729))  # 9
# print(max_digit(555))   # 5
# print(max_digit(0))     # 0
# Constraint: Do not use max(), loops, or convert the number to a string.

# Hint: Compare the last digit (n % 10) with the maximum digit in the remaining number (n // 10). Design the base case carefully.

# n=int(input("Enter the number: "))

# def max_digit(n,m):
#     if n==0:
#         return m
#     if m<n%10:
#         m=n%10
#     return max_digit(n//10,m)
# print(max_digit(n,0))

# x=-10
# total=0
# def sum(x,total):
#     total+=x
#     if x==10:
#         return total
#     return sum(x+1,total)
    
# print(sum(x,total))




# Trace the return values (5 marks)
# Without running the code, write the value returned by mystery(4) and show the return calculation.
# def mystery(n):
# if n <= 1:
# return n
# return mystery(n - 1) + mystery(n - 2)
# Also state the values returned by mystery(0), mystery(1), and mystery(2).




# Section D — Edge Cases and Debugging (10 marks)
# 16.Fix the factorial (3 marks)
# This function gives the wrong result for factorial(0). Fix the base case.
# def factorial(n):
# if n == 0:
# return 0
# return n * factorial(n - 1)
# def factorial(n):
# if n == 1:
# return 1
# return n * factorial(n - 1)
# print(factorial(10))




# 17.Make progress (3 marks)
# The function below never changes n. Rewrite it so it counts down to 0 and stops.
# def stop_at_zero(n):
# if n == 0:
# return
# stop_at_zero(n)
# def stop_at_zero(n):
# if n == 0:
# return 0
# print(n)
# return stop_at_zero(n-1)
# print(stop_at_zero(9))

