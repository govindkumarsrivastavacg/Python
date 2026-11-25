# 1.Define a function named welcome that prints Welcome to Python. Call it three times.

def welcome():
    print("Welcome to python")

welcome()
welcome()
welcome()


# 2.Define greet(name) that prints a greeting using the given name.

def greet(name):
    print(f"welcome {name}")
greet("Govind")



# 3.Define show_number(number) that prints the number passed to it.

def number(n):
    print(n)
greet(90)



#  4.Define add(a, b) that returns the sum of two numbers.

def add(a,b):
    return a+b

print(add(67,56))


#  5.Define square(number) that returns the square of a number.

def square(a):
    return a*a

print(square(6))


#  6.Define is_even(number) that returns True if the number is even and False otherwise.


def is_even(a):
    return a%2==0
print(is_even(8))


#  7.Define get_full_name(first_name, last_name) that returns the full name.


def full_name(a,b):
    return a+b
print(full_name("Govind","Srivastava"))



# 8.Define introduce(name, city="Pune") and test it with and without a city argument.

def introduce(name,city="Pune"):
    print(name,city)

introduce("Govind")

# 9.Define subtract(a, b) and show how changing positional argument order changes the result.

def sub(a,b):
    return a-b
print(sub(70,10))



#  10.Define get_min_max(a, b) that returns both the smaller and larger values.


def get_min_max(a,b):
    if(a>b):
        print("A is greater")   
    elif(a<b):
        print("B is greater")
    else:
        print("Both are equal")

get_min_max(7,6)

# Intermediate
# Define calculate(a, b) that returns the sum, difference, product, and quotient. Assume b is not zero.

# def calculate(a,b):
#     sum = a+b
#     difference = a-b
#     product = a*b
#     quotient = a/b
#     return 'addition',sum,'Substraction',difference,'Multiplication',product,'Divison',quotient

# print(calculate(9,2))

# Define count_digits(number) that returns the number of digits in a non-negative integer. For this exercise, treat 0 as having one digit.

# def count_digits(number):
#     count=0
#     for i in str(number):
#         count+=1
#     print(count)
    
# count_digits(8)


# Define classify_number(number) that returns "Positive", "Negative", or "Zero".
# def classify_number(number):
#     if number > 0:
#         print('Positive')
#     elif number < 0:
#         print('Negative')
#     elif number == 0:
#         print('Zero')

# classify_number(0)

# Define calculate_total(price, quantity=1) that returns the total price.

# def calculate_total(price,quantity=1):
#     total = price*quantity
#     return total
# print(calculate_total(12,4))

# Define create_email(username, domain="example.com") that returns an email address.

# def create_email(username,domain="@example.com"):
#     email = username+domain
#     return email

# print(create_email('nirmal'))

# Define format_name(first, last, uppercase=False). If uppercase is True, return the full name in uppercase.

# def format_name(first,last,upparcase=False):
#     full_name=first+' '+last
#     if upparcase==True:
#         print(full_name.upper())
#     else:
#         print(full_name)
        
# format_name("nirmal","kumar",False)
        

# Define percentage(marks, total=100) that returns the percentage. Assume total is not zero.

# def percentage(marks,total=100):
#     result=(marks/total)*100
#     return result
    
# print(percentage(345,500))

# Define convert_minutes(minutes, seconds_per_minute=60) that returns the total seconds.

# def convert_minutes(minutes,seconds_per_minute=60):
#     total_seconds = minutes*seconds_per_minute
#     return total_seconds
# print(convert_minutes(22))


# Define student_details(name, age, city) and call it using keyword arguments in a different order.

# def student_details(name, age, city):
#     print(f'Name-{name}\nAge-{age}\nCity-{city}')

# student_details(age=17,name='Govind',city='Kanpur')

# Define bill(item, quantity=1, price=100) that returns the bill amount. Test positional and keyword calls.

# def bill(item,quantity=1,price=100):
#     total_bill = quantity*price
#     return total_bill
# print(bill('Book',1,600))


# Challenging
# Define analyze_number(number) that returns three values: the absolute value, whether it is even, and the number of digits. Do not use abs(); assume the input is an integer.

# def analyze_number(number):
#     count=0
#     if number % 2==0:
#         print('even')
#     else:
#         print('odd')
#     for i in str(number):
#         count+=1
#     print(count)
    
# analyze_number(9999)
    

# Define calculate_stats(a, b, c) that returns the smallest, largest, and sum of three numbers.

# def calculate_stats(a,b,c):
#     sum = a+b+c
#     print(f'Total Sum of these three numbers are:{sum}')
# #Largest Finder
#     if a > b and a > c:
#         print('Largest',a)
#     elif b > a and b > c:
#         print('Largest',b)
#     elif c > a and c > b:
#         print('Largest',c)
# #Smallest Finder
#     if a < b and a < c:
#         print('Smallest',a)
#     elif b < a and b < c:
#         print('Smallest',b)
#     elif c < a and c < b:
#         print('Smallest',c)
        
# calculate_stats(9,8,7)


# Define make_sentence(subject, verb, object) that returns a sentence. Call it with keyword arguments in a different order.

# def make_sentence(subject,verb,adverb):
#     sentence = subject+' '+verb+' '+adverb
#     print(sentence)
    
# make_sentence('laptop','is','hot')

# Define apply_discount(price, discount=0) that returns the final price after subtracting the discount percentage. Assume discount is between 0 and 100.

# def apply_discount(price,discount=10):
#     discount = price*(discount*0.01)
#     final_price = price-discount
#     print(final_price)
# apply_discount(1000,20)


# Define calculate_pay(hours, rate=200, bonus=0) that returns hours * rate + bonus. Try different combinations of positional and keyword arguments.

# def calculate_pay(hours,rate=200, bonus=0):
#     return hours * rate + bonus 

# print(calculate_pay(2,200,100))


# Define get_coordinates(x=0, y=0) that returns both values. Test default calls and calls with only one keyword argument.

# def get_coodinadinates(x=0,y=0):
#     return x, y

# print(get_coodinadinates(3,8))

# Define compare(a, b) that returns two values: "A is greater", "B is greater", or "Equal" as the first value, and the absolute difference as the second value. Do not use abs().

# def compare(a, b):
#     if a > b:
#         print('A is greater')
#     elif a < b:
#         print('B is greater')
#     elif a == b:
#         print('Equal')

# compare(4,4)

# Define convert_temp(value, scale="C"). If scale is "C", convert Celsius to Fahrenheit; if "F", convert Fahrenheit to Celsius. Return the converted value. Assume the scale is valid.

# def convert_temp(value, scale='C'):
#     if scale =='C':
#         f_to_c =  ((value-32)/1.8)
#         return f_to_c
#     elif scale =='F':
#         c_to_f = ((value*1.8)+32)
#         return c_to_f
    
# print(convert_temp(32,'C'))
    


# Define calculate_result(marks, passing_marks=35) that returns "Pass" if marks meet the passing mark and "Fail" otherwise.

# def calculate_result(marks, passing_marks=35):
#     if marks >=35:
#         print('Pass')
#     else:
#         print('Fail')
        
# calculate_result(34)



# Define order_summary(item, quantity=1, price=100, delivery_fee=40) that returns the total cost. Use keyword arguments to change only the delivery fee.

# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     total_cost = ((quantity*price)+delivery_fee)
#     return item , total_cost

# print(order_summary('Mouse',4))

# Rough Work--------------

# def check_balance(balance):
#     print(balance)
# def credit_balance(balance):
#     print(balance+deposit)
#     return balance
# def withdrawal(balance):
#     print(balance-withdraw)
#     return balance

# balance = 30000
# menu = int(input('1.Check Balance\n2.Credit Balance\n3.Withdraw Balance\n4.Exit\n:'))
# while menu!=4:
#     match menu:
#         case 1:
#             check_balance(balance)
#             break
#         case 2:
#             deposit = int(input('Enter The Amt You Want To Deposit: '))
#             credit_balance(balance)
#             break
#         case 3:
#             withdraw = int(input('Enter The Amount Of Money You Want To Withdraw: '))
#             withdrawal(balance)
#             break
#         case _:
#             print('Enter A Valid Option...')
#             break
# print('Exiting...')

# a=10
# b=20
# c=40
# d=50
# k=10

# def add(a, b):
#     c=a+b
#     return c
# def sub(a,b):
#     return a-b
# def muli(a,b):
#     e=a*b
#     return e
# def fdev(a,b):
#     j=a//b
#     return j

# print(fdev(muli(sub(add(a,b),c),d),k))





# def check_balance(balance):
#     print(balance)

# def withdraw(balance):
#     wit=int(input("Enter the money you want to withdraw: "))
#     balance-=wit
#     return balance
# def deposit(balance):
#     dep=int(input("Enter the amount you want to deposit: "))
#     balance+=dep
#     return balance

# balance=30000
# flag=True
# while(flag):
#     choice=int(input("Enter your choice\n1.Deposit\n2.Withdraw\n3.Check balance\n4.End operation\n:"))
#     print()
#     match choice:
#         case 1:
#             balance=deposit(balance)
#         case 2:
#             balance=withdraw(balance)
#         case 3:
#             check_balance(balance)
#         case 4:
#             flag=False
#         case _:
#             print("Enter a valid operation")
#     print()



# def cal(a,b):
#     def sub(a,b):
#         return a-b
#     def div(a,b):
#         return a/b
#     def fdiv(a,b):
#         return a/b
#     def add(a,b):
#         return a+b
#     return sub(a,b),div(a,b),fdiv(a,b),add(a,b)


# print(cal(25,3))


# def cal(a,b):
#     def sub(a,b):
#         print(a-b)
#         def div(a,b):
#             print(a/b)
#             def fdiv(a,b):
#                 print(a//b)
#                 def add(a,b):
#                     print(a+b)
#                 return add(a,b)
#             return fdiv(a,b)
#         return div(a,b)    
#     return sub(a,b)        
# cal(25,3)        


# def counter_fun(count):
#     count = count + 1
#     if(count==5):
#         return count
#     return counter_fun(count)
# print(counter_fun(0))


# Fact- 4!=1x2x3x4 = 24
# Fact = 1
# num = 3
# i = 1 2 3 4
# i= 1*2*3*4