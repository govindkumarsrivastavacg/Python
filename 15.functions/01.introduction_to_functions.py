# 12. Quick Dry Run Questions-

#OUTPUT Of Q.1 - Start
#OUTPUT Of Q.2 - Hello 
#                Hello
##OUTPUT Of Q.3 - B A B
#OUTPUT Of Q.4 - one inside two inside 
#OUTPUT Of Q.5 - A start middle B
#OUTPUT Of Q.6 - Done
#OUTPUT Of Q.7 - NameError     
#OUTPUT OF Q.8 - C A B

# Addition Function-


# def addition(a=int(input('Enter The Number: ')),b=int(input('Enter The Number: '))):
#     print(a+b)

# addition()

# #Substraction Function-

# def substraction(c=int(input('Enter The Number: ')),d=int(input('Enter The Number: '))):
#     print(c-d)
    
# substraction()

# def multiplication(e=int(input('Enter The Number')),f=int(input('Enter The Number: '))):
#     print(e*f)

# Number To Binary (Code, Function Code)

# num = int(input('Enter The Number You Want To Convert It Into Binary: '))
# # binary = ''
# while num > 0:
 #     binary = str(num%2)+binary
 #     num = num // 2
 # print(binary)

# def numtobinary(n):
#     binary =''
#     while n > 0:
#         binary =str(n%2)+binary
#         n = n // 2
#     return binary
    
# print(numtobinary(num))





## Basic Level

# 1. Define a function named `greet` that prints `Hello, Python!`. Call it once.

# def greet():
#     print('hello python')

# 2. Define a function named `show_name` that prints your name. Call it three times.

# def show_name():
#     print('Nirmal')
# show_name()
# show_name()
# show_name()

# 3. Define a function named `print_line` that prints 20 hyphens. Call it before and after a heading.(
# def print_line():
#     print('-'*20)
    
# print_line()


# 4. Define a function named `show_rules` that prints three classroom rules, one per line.

# def show_rules():
#     print('1.Kuch bhi karo')
#     print('2.Murder Karna Allowed h and it is the best practice')
#     print('3.Sybau')
    
# show_rules()

# 5. Define a function named `show_square` that prints a 4-by-4 square of `*` characters using four `print("****")` statements. Call it once.

# def show_square():
#     for i in range(1,5):
#         print('*'*i)
#         for j in range(1,5):
#             print('*'*j)

# show_square()

# 6. Define a function named `show_menu` that prints three menu options. Call it twice.
# def show_menu():
#     print('---Menu----\n1.A\n2.B\n3.C\n: ')
# show_menu()
# show_menu()



# 7. Define two functions, `morning_message` and `evening_message`. Call them in the reverse order of their definitions.

# def morning_message():
#     print('Good Morning')

# def evening_message():
#     print('Good Evening')
    
# evening_message()
# morning_message()


# 8. Define a function named `show_student_card` that prints a heading, a student name, and a roll number. Call it once.

# def show_student_card():
#     heading = 'CodingGita'
#     student_name = 'Nirmal Kumar'
#     roll_number= 889
#     print(f'{heading}\n{student_name}\n{roll_number}')
    
# show_student_card()
    

# 9. Define a function named `print_numbers` that prints the numbers 1 through 5 using five print statements. Call it twice.

# def print_numbers():
#     print(1)
#     print(2)
#     print(3)
#     print(4)
#     print(5)
    
# print_numbers()

# 10. Define a function named `show_pattern` that prints:
#     ```
#     *
#     **
#     ***
#     ```
#     Call it twice.

# def show_pattern():
#     print('*')
#     print('**')
#     print('***')
    
# show_pattern()
# show_pattern()


# ## Intermediate Level

# 11. Create three functions: `show_header`, `show_body`, and `show_footer`. Call them in the correct order to print a simple report.

# def show_header():
#     print('DPS')
# def show_body():
#     print('text text text text text text text')
# def show_footer():
#     print('Contant Us')
        
# show_header()
# show_body()
# show_footer()
    


# 12. Create a function named `show_separator` that prints `====================`. Use it between sections of a report.

# def show_separator():
#     print('====================')

# 13. Define functions named `step_one`, `step_two`, and `step_three`. Each should print its step name. Call them in the order 3, 1, 2.

# def step_one():
#     print('Step one')
# def step_two():
#     print('Step Two')
# def step_three():
#     print('Step Three')

# step_three()
# step_one()
# step_two()

# 14. Create a function named `show_table_heading` that prints column headings for a student table. Call it before printing two student rows.

# def show_table_heading():
#     print('Name        Marks')
#     print('------------------')

# show_table_heading()
# print('Alice       90')
# print('Bob         85')

# 15. Define a function that prints five stars on one line. Call it four times to create four rows.
# def print_five_stars():
#     print('*****')

# for _ in range(4):
#     print_five_stars()

# 16. Create a function named `show_welcome` that prints a welcome message and course name. Call it at the start of a simple program.
# def show_welcome():
#     print('Welcome to the Python Course')

# show_welcome()

# 17. Define a function named `show_help` that prints instructions for a simple calculator. Call it before printing the calculator menu.
# def show_help():
#     print('Calculator Instructions:')
#     print('1. Enter first number')
#     print('2. Enter operator')
#     print('3. Enter second number')

# show_help()
# print('Calculator Menu:')
# print('1. Add')
# print('2. Subtract')
# print('3. Multiply')
# print('4. Divide')

# 18. Create two functions that print the opening and closing lines of a receipt. Call them around the receipt details.
# def print_receipt_opening():
#     print('=== Receipt ===')

# def print_receipt_closing():
#     print('=== Thank You ===')

# print_receipt_opening()
# print('Notebook   $20')
# print('Pen        $5')
# print_receipt_closing()

# 19. Define a function named `print_box` that prints a fixed three-line text box. Call it twice.
# def print_box():
#     print('+-------------------+')
#     print('|     Welcome!      |')
#     print('+-------------------+')

# print_box()
# print_box()

# 20. Create functions for a program's title, menu, and closing message. Arrange the calls to produce a readable program flow.
# def show_title():
#     print('My Program')

# def show_menu():
#     print('Menu:')
#     print('1. View')
#     print('2. Edit')
#     print('3. Exit')

# def show_closing_message():
#     print('Goodbye!')

# show_title()
# show_menu()
# show_closing_message()

# ## Debugging and Reasoning

# 21. Fix the indentation error:
#     ```python
#     def greet():
#     print("Hello")
#     ```

# def greet():
#     print("Hello")


# 22. Fix the code so it prints `Welcome`:
#     
#     def welcome():
#         print("Welcome")

# def welcome():
#     print("Welcome")

# 23. Explain why this code raises an error, then fix it:
#   
#     show()

#     def show():
#         print("Hello")
# Because Python Runs Code From Top To Bottom and function is being called before the code of function so i cannot access it.

# def show():
#     print("Hello")
# show()




# 24. Find the naming problem and fix it:
# 
#     def print_report():
#         print("Report")

#     Print_Report()
#    

# def print_report():
#     print("Report")

# print_report()
 

# 25. Predict the output and explain why:
#
#     def a():
#         print("A")

#     def b():
#         print("B")

#     a()
#     b()
#     a()

# Output- A B A Why- The Order Of The Function being called



# 26. How many times does the function body run?

#     def message():
#         print("Python")

#     message()
#     message()
#     message()
#     message()
# 4 Times


# 27. Which lines belong to the function body?

#     def example():
#         print("One")
#         print("Two")

#     print("Three")
# one and two are the lines which belongs to the function body


# 28. Rename the following functions using clear `snake_case` names:
#     - `f`
#     - `DoTask`
#     - `studentdetails`
#     - `x1` (assume it displays a menu)
#
#     - 
#     - do_task
#     - student_details
# 29. Write a program with two function definitions but call only one. Predict the output.

# def function_one():
#     print('q')
# def function_two():
#     print('w')
    
# function_two()
# function_one()

# w and q


# 30. Write a program that defines one function, prints a message outside it, calls the function, and prints another message after the call.

# def msg():
#     print('hello')
# msg()
# print('bye')
# print('hello')
