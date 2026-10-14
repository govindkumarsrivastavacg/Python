

# ## Part A — Intermediate Problems

# ### Q1. Valid Marks

# Ask the user to enter marks between `0` and `100`, inclusive. Keep asking until valid marks are entered. Finally, display the accepted marks.

# **Answer:**


# marks = int(input("Enter marks (0-100): "))

# while marks < 0 or marks > 100:
#     print("Invalid marks!")
#     marks = int(input("Enter marks (0-100): "))

# print("Accepted marks:", marks)


# ### Q2. Positive Integer

# Keep asking the user to enter an integer until they enter a number greater than `0`. Display the accepted number.

# **Answer:**

# n = int(input("Enter a positive integer: "))

# while n <= 0:
#     print("Invalid number!")
#     n = int(input("Enter a positive integer: "))

# print("Accepted number:", n)


# ### Q3. Age Validation

# Accept ages from `0` through `120`. If the age is outside this range, display an error message and ask again.

# **Answer:**

# age = int(input("Enter your age: "))

# while age < 0 or age > 120:
#     print("Invalid age!")
#     age = int(input("Enter your age: "))

# print("Accepted age:", age)


# ### Q4. Menu Choice

# Display the menu repeatedly until the user enters `1`, `2`, `3`, or `4`. Display the selected option after valid input.

# **Answer:**


# print("1. View profile")
# print("2. Edit profile")
# print("3. Settings")
# print("4. Exit")

# choice = int(input("Enter your choice: "))

# while choice < 1 or choice > 4:
#     print("Invalid choice!")
#     choice = int(input("Enter your choice: "))

# print("Selected option:", choice)


# ### Q5. Password Length

# Keep asking for a password until it contains at least eight characters. Leading and trailing spaces should not count toward the password length.

# **Answer:**

# ```python
# password = input("Enter password: ").strip()

# while len(password) < 8:
#     print("Password must contain at least 8 characters!")
#     password = input("Enter password: ").strip()

# print("Password accepted!")


# ### Q6. Temperature Range

# Accept a temperature between `-20` and `45`, inclusive. Repeat until the input is valid.

# **Answer:**

# temp = float(input("Enter temperature: "))

# while temp < -20 or temp > 45:
#     print("Invalid temperature!")
#     temp = float(input("Enter temperature: "))

# print("Accepted temperature:", temp)


# ### Q7. Withdrawal Validation

# Start with a balance of ₹5,000. Reject withdrawals that are zero, negative, or greater than the available balance.

# **Answer:**


# balance = 5000

# amount = float(input("Enter withdrawal amount: "))

# while amount <= 0 or amount > balance:
#     print("Invalid withdrawal amount!")
#     amount = float(input("Enter withdrawal amount: "))

# balance -= amount

# print("Withdrawal successful!")
# print("Remaining balance:", balance)


# ### Q8. Username Validation

# The username must contain at least five characters after trimming outer spaces and must not contain internal spaces.

# **Answer:**

# username = input("Enter username: ").strip()

# while len(username) < 5 or " " in username:
#     print("Invalid username!")
#     username = input("Enter username: ").strip()

# print("Accepted username:", username)


# ### Q9. Divisible Number

# Accept a positive integer divisible by both `3` and `5`.

# **Answer:**

# n = int(input("Enter a positive integer: "))

# while n <= 0 or n % 3 != 0 or n % 5 != 0:
#     print("Invalid number!")
#     n = int(input("Enter a positive integer: "))

# print("Accepted number:", n)


# Q10. Limited PIN Attempts

# The secret PIN is `2468`. Allow up to three attempts. Stop immediately when the PIN is correct.

# **Answer:**


# pin = 2468
# attempts = 0

# while attempts < 3:
#     entered_pin = int(input("Enter PIN: "))
#     attempts += 1

#     if entered_pin == pin:
#         print("Access granted!")
#         break
#     else:
#         print("Incorrect PIN!")

# if attempts == 3 and entered_pin != pin:
#     print("Access denied!")

# ### Q11. Number Within a Range

# Accept an integer between `10` and `50`, inclusive. Print whether it is even or odd.

# **Answer:**


# n = int(input("Enter an integer (10-50): "))

# while n < 10 or n > 50:
#     print("Invalid number!")
#     n = int(input("Enter an integer (10-50): "))

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# ### Q12. Deposit Validation

# Start with a balance of ₹2,000. Accept only positive deposits and display the updated balance.

# **Answer:**


# balance = 2000

# amount = float(input("Enter deposit amount: "))

# while amount <= 0:
#     print("Invalid deposit amount!")
#     amount = float(input("Enter deposit amount: "))

# balance += amount

# print("Updated balance:", balance)


# ## Part B — Challenging Problems

# ### Q13. Integer Between 1 and 100

# Keep asking until an integer between `1` and `100`, inclusive, is entered.

# **Answer:**


# n = int(input("Enter an integer (1-100): "))

# while n < 1 or n > 100:
#     print("Invalid number!")
#     n = int(input("Enter an integer (1-100): "))

# print("Accepted number:", n)


# ### Q14. Marks and Result

# Accept marks between `0` and `100`. Display the appropriate result after validation.

# **Answer:**

# marks = int(input("Enter marks (0-100): "))

# while marks < 0 or marks > 100:
#     print("Invalid marks!")
#     marks = int(input("Enter marks (0-100): "))

# if marks >= 75:
#     print("Distinction")
# elif marks >= 60:
#     print("First Class")
# elif marks >= 35:
#     print("Pass")
# else:
#     print("Fail")
# ### Q15. Username and Password Validation

# The username must have at least five characters after trimming outer spaces and contain no internal spaces. The password must have at least eight non-whitespace characters and cannot consist only of spaces.

# **Answer:**

# while True:
#     username = input("Enter username: ").strip()
#     password = input("Enter password: ")

#     if (len(username) >= 5 and " " not in username
#             and len(password.strip()) >= 8):
#         break

#     print("Invalid username or password! Try again.")

# print("Login details accepted!")

# ### Q16. Calculator Input Validation

# Ask for two numbers and an operator (`+`, `-`, `*`, or `/`). Re-prompt for an invalid operator or a zero divisor.

# **Answer:**

# a = float(input("Enter first number: "))

# operator = input("Enter operator (+, -, *, /): ")

# while operator not in ["+", "-", "*", "/"]:
#     print("Invalid operator!")
#     operator = input("Enter operator (+, -, *, /): ")

# b = float(input("Enter second number: "))

# while operator == "/" and b == 0:
#     print("Division by zero is not allowed!")
#     b = float(input("Enter second number: "))

# if operator == "+":
#     result = a + b
# elif operator == "-":
#     result = a - b
# elif operator == "*":
#     result = a * b
# else:
#     result = a / b

# print("Result:", result)

# ### Q17. Banking Menu

# Start with ₹10,000. Allow the user to check balance, deposit money, withdraw money, or exit. Validate transactions before updating the balance.

# **Answer:**

# balance = 10000

# choice = 0

# while choice != 4:
#     print("\n1. Check balance")
#     print("2. Deposit money")
#     print("3. Withdraw money")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     while choice < 1 or choice > 4:
#         print("Invalid choice!")
#         choice = int(input("Enter choice: "))

#     if choice == 1:
#         print("Balance:", balance)

#     elif choice == 2:
#         amount = float(input("Enter deposit amount: "))

#         while amount <= 0:
#             print("Invalid amount!")
#             amount = float(input("Enter deposit amount: "))

#         balance += amount
#         print("Updated balance:", balance)

#     elif choice == 3:
#         amount = float(input("Enter withdrawal amount: "))

#         while amount <= 0 or amount > balance:
#             print("Invalid amount!")
#             amount = float(input("Enter withdrawal amount: "))

#         balance -= amount
#         print("Updated balance:", balance)

# print("Thank you!")

# ### Q18. Validate Month and Day

# Accept a month from `1` to `12` and a day from `1` to `31`. Repeat until both values are within their individual ranges.

# **Answer:**

# month = int(input("Enter month (1-12): "))
# day = int(input("Enter day (1-31): "))

# while (month < 1 or month > 12
#        or day < 1 or day > 31):
#     print("Invalid month or day!")

#     month = int(input("Enter month (1-12): "))
#     day = int(input("Enter day (1-31): "))

# print("Accepted month:", month)
# print("Accepted day:", day)

# ### Q19. Product Quantity and Price

# Quantity must be a positive integer. Unit price must be greater than zero. Repeat only the invalid field's prompt.

# **Answer:**

# quantity = int(input("Enter quantity: "))

# while quantity <= 0:
#     print("Quantity must be positive!")
#     quantity = int(input("Enter quantity: "))

# price = float(input("Enter unit price: "))

# while price <= 0:
#     print("Price must be positive!")
#     price = float(input("Enter unit price: "))

# total = quantity * price

# print("Total cost:", total)

# ### Q20. Safe Average Calculator

# Accept a count from `1` to `20`, then read that many numeric values and calculate the average.

# **Answer:**

# count = int(input("How many numbers? "))

# while count < 1 or count > 20:
#     print("Count must be between 1 and 20!")
#     count = int(input("How many numbers? "))

# total = 0

# for i in range(count):
#     n = float(input("Enter number: "))
#     total += n

# average = total / count

# print("Average:", average)


# ### Q21. Stronger Password Rules

# Require at least eight characters, an uppercase letter, a lowercase letter, a digit, and no whitespace. Display the unsatisfied rules after each invalid attempt.

# **Answer:**


# while True:
#     password = input("Enter password: ")

#     upper = any(ch.isupper() for ch in password)
#     lower = any(ch.islower() for ch in password)
#     digit = any(ch.isdigit() for ch in password)
#     no_space = not any(ch.isspace() for ch in password)

#     valid = (
#         len(password) >= 8
#         and upper
#         and lower
#         and digit
#         and no_space
#     )

#     if valid:
#         print("Password accepted!")
#         break

#     print("Password requirements not satisfied:")

#     if len(password) < 8:
#         print("- At least 8 characters")

#     if not upper:
#         print("- At least one uppercase letter")

#     if not lower:
#         print("- At least one lowercase letter")

#     if not digit:
#         print("- At least one digit")

#     if not no_space:
#         print("- No whitespace characters")


# ### Q22. Input Validation Without `break`

# Accept an integer from `1` to `10` without using `break`.

# **Answer:**


# n = int(input("Enter an integer (1-10): "))

# while n < 1 or n > 10:
#     print("Invalid number!")
#     n = int(input("Enter an integer (1-10): "))

# print("Accepted number:", n)

# # Q23. Three Valid Scores

# Accept three scores from `0` to `100`, inclusive. Repeat only the invalid score prompt, then display the total and average.

# **Answer:**


# score1 = int(input("Enter score 1: "))

# while score1 < 0 or score1 > 100:
#     print("Invalid score!")
#     score1 = int(input("Enter score 1: "))

# score2 = int(input("Enter score 2: "))

# while score2 < 0 or score2 > 100:
#     print("Invalid score!")
#     score2 = int(input("Enter score 2: "))

# score3 = int(input("Enter score 3: "))

# while score3 < 0 or score3 > 100:
#     print("Invalid score!")
#     score3 = int(input("Enter score 3: "))

# total = score1 + score2 + score3
# average = total / 3

# print("Total:", total)
# print("Average:", average)

# # Q24. ATM Withdrawal With Denomination Rules

# Start with ₹10,000. The withdrawal must be positive, must not exceed the balance, and must be a multiple of ₹100.

# **Answer:**

# balance = 10000

# amount = int(input("Enter withdrawal amount: "))

# while (amount <= 0
#        or amount > balance
#        or amount % 100 != 0):
#     print("Invalid withdrawal amount!")
#     amount = int(input("Enter withdrawal amount: "))

# balance -= amount

# print("Withdrawn amount:", amount)
# print("Remaining balance:", balance)
