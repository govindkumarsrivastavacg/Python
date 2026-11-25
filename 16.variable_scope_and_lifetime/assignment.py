# Create a function with a local variable city and print it.

# def sum():
#     a="hello"
#     print(a)

# Create a global variable school. Read it inside a function.

# a=10
# def sum():
#     print(a)



# Assign a variable inside an if block and print it outside the block.
# a=10
# if(a>5):
#     a=8
# print(a)

# Use a for loop to assign a loop variable. Print it after the loop.

# for i in range(1):
#     x=5
# print(x)

# Explain the difference between scope and lifetime in your own words.


# scope defines where we can use a variable while lifetime refers to how long a variable is binded to an object




# Predict the output:

# value = 100
# def test():
#     value = 200
#     print(value)
# test()
# print(value)
# 200
# 100



# Fix this code so it increments the global variable:

# clicks = 0
# def click():
#     clicks += 1




# clicks = 0
# def click():
#     global clicks
#     clicks += 1
# click()




# Explain why this code raises an error:
# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()


# because name is not able to access the value of name yet



# Write a nested function that reads a variable from its enclosing function.


# def outer():
#     x=10
#     def inner():
#         print(x)
#     inner()
# outer()


# Write a function that returns a list. Show that the returned list can be changed by the caller.


# def sum():
#     l=[1,2,3,4,5]
#     return l
# x=sum()
# x.append(6)
# print(x)


# Use nonlocal to create a counter that returns 1, 2, 3 across three calls.



# def outer():
#     x=1
#     def inner():
#         nonlocal x
#         print(x)
#         x+=1
#     return inner
# counter=outer()
# counter()
# counter()
# counter()





# Predict the output: python     x = 1     def outer():         x = 2         def inner():             x = 3      
#        print(x)         inner()         print(x)     outer()     print(x)


# 3
# 2
# 1


# Explain why the loop variable in a normal for loop can remain available after the loop, but a list-comprehension
#  variable in Python 3 does not overwrite an outer variable.

# normal for loop does not create its own block while the list comprehension does



# Create a function that returns another function. Explain which variable remains available and why.


# def outer():
#     x=1
#     def inner():
#         nonlocal x
#         print(x)
#         x+=1
#     return inner
# counter=outer()
# counter()





# Explain why variable names such as list, str, and sum should usually be avoided.


# because they will lead to error if we use them as in built functions later on