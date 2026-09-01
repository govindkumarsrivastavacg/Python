# Task 1 — Create Strings
# Create variables for:

# Your name
# Your city
# Your favorite programming language
# A short message
# Print all variables.

# Use both single quotes and double quotes in your program.




name='Govind'
city="Kanpur"
favlang="C"
msg="A short message ig"
print( name,city,favlang,"  "  ,msg)


# Task 2 — Empty String
# Create an empty string.

# Print:

# The string
# Its length
# Its data type

emp=""
print(emp)
print(len(emp))
print(type(emp))




# Task 3 — String Information
# Create:

# "Python Programming"
# Display:

# Complete string
# Length
# First character
# Last character
# Third character
# Second-last character


a="Python Programming"
print(a)
print(len(a))
print(a[0])
print(a[-1])
print([2])
print([-2])



# Part 4 — Indexing
# Task 4 — Positive Indexing
# Create:

# "Programming"
# Using indexing, print:

# First character
# Second character
# Fifth character
# Last character
# Do not directly type the characters. Access them using indexes.

b="Programming"
print(b[0])
print(b[1])
print(b[4])
print(b[-1])


# Task 5 — Negative Indexing
# Using the same string, print:

# Last character
# Second-last character
# Third-last character
# First character using a negative index

print(b[-1])
print(b[-2])
print(b[-3])
print(b[-len(b)])


# Task 6 — Indexing Challenge
# Create a string containing your full name.

# Using indexing, print:

# First character
# Last character
# First character of your last name, if applicable

fname="Govind Kumar Srivastava"
print(fname[0])
print(fname[-1])
print(fname[-10])


# Task 7 — Basic Slicing
# Create:

# "Python Programming"
# Using slicing, extract:

# "Python"
# "Programming"
# "Python Programming"
# First 5 characters
# Last 5 characters

print(a[0:6])
print(a[7:])
print(a[0:])
print(a[0:6])
print(a[13:])


# Task 8 — Slicing with Step
# Create:

# "ABCDEFGHIJKL"
# Using slicing:

# Print every second character.
# Print every third character.
# Print characters from index 1 to index 8 with step 2.
# Reverse the string.

c="ABCDEFGHIJKL"
print(c[::2])
print(c[::3])
print(c[1:9:2])
print(c[::-1])


# Task 9 — Slicing with Negative Indexes
# Create:

# "Python Programming"
# Use negative indexes to extract:

# Last 5 characters
# Last 10 characters
# Characters from the end using a negative step

print(a[-5:])
print(a[-10:])
print(a[::-1])


# Task 10 — Slicing Challenge
# Create any string containing at least 10 characters.

# Using only slicing, produce:

# The first 3 characters.
# The last 3 characters.
# Every second character.
# The string in reverse.
# The string without its first and last character.


print(a[0:4])
print(a[-3:])
print(a[::2])
print(a[::-1])
print(a[1:-1])


# Task 11
# Create three strings:

# A short word
# A sentence
# A sentence containing spaces
# Use len() to find the length of each.

# Observe how spaces affect the result.

str1="short"
str2="Asentencewithoutspaces"
str3="A sentence with spaces"
print(len(str1))
print(len(str2))
print(len(str3))


# Task 12
# Create:

# text = "Python Programming"
# Use len() to calculate the last valid positive index.

# Then use that value to access the last character.

text=a
last=len(a)-1
print(text[last])


# Task 13 — Full Name
# Create:

# first_name
# last_name
# Combine them into a full name.

# The output should contain a space between the first and last name.
fname1="Govind"
lname="srivastava"
fulname=fname1+" "+lname
print(fulname)


# Task 14 — Sentence Creation
# Create separate variables for:

# Name
# Age
# City
# Programming language
# Create a sentence using string concatenation.

print(fname+" ""is my name and i am from "+city+" i have recently started studying "+favlang)


# Task 15 — String and Integer
# Try combining a string and an integer using +.

# Observe the error.

# Then solve the problem using str().

# print(fname+6)
# #TypeError


# Task 16
# Create a string containing a symbol or character.

# Repeat it:

# 3 times
# 5 times
# 10 times
# Use the * operator.

x="new@123"
print(x*3)
print(x*5)
print(x*10)


# Task 17 — Pattern
# Use string repetition to create the following output:

# **********
# Do not type all ten * characters manually.

star="*"
print(star*10)


# Task 18
# Create:

# "python programming language"
# Apply:

# upper()
# lower()
# capitalize()
# title()
# swapcase()
# Display every result.


ab="python programming language"
print(ab.upper())
print(ab.lower())
print(ab.capitalize())
print(ab.swapcase())


# Task 19 — Case-Insensitive Comparison
# Create two strings:

# "Python"
# "python"
# Check whether they are equal.

# Then convert both strings to lowercase and compare them again.


a1="Python"
a2="python"
print(a1==a2)
c1=a1.lower()
c2=a2.lower()
print(c1==c2)


# Task 20 — Membership
# Create:

# "Python is a programming language"
# Check whether the following exist in the string:

# "Python"
# "programming"
# "Java"
# "language"
# Use in.


d="Python is a programming language"
print("python" in d)
print("programming" in d)
print("Java" in d)
print("language" in d)



# Task 21 — find()
# Using the same string:

# Find the position of:

# "Python"
# "programming"
# "language"
# "Java"
# Observe what find() returns when the text does not exist.

print(d.index("Python"))
print(d.index("programming"))
print(d.index("language"))
#print(d.index("Java"))   results in value error

# Task 22 — index()
# Repeat the previous task using index().

# Try searching for "Java".

# Observe the difference between find() and index().


#print(d.index("Java"))   results in value error
print(d.find("Java"))  #results in -1 rather than ValueError



# Task 23 — Count Characters
# Create:

# "banana"
# Use count() to find how many times:

# "a"
# "n"
# "b"
# occur.

banana="banana"
print(banana.count("a"))
print(banana.count("n"))
print(banana.count("b"))



# Task 24 — Starts and Ends
# Create:

# filename = "student_notes.pdf"
# Check:

# Whether it starts with "student".
# Whether it ends with ".pdf".
# Whether it ends with ".txt".


filename="student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))


# Task 25 — Replace a Word
# Create:

# text = "I am learning Java"
# Replace "Java" with "Python".

# Display the new string.

text="I am learning Java"
new_text=text.replace("Java","Python")
print(new_text)


# Task 26 — Multiple Replacements
# Create:

# text = "apple apple apple"
# Replace every "apple" with "mango".

text1="apple,apple,apple"
new_text1=text1.replace("apple","mango")
print(new_text1)


# Task 27 — Limited Replacement
# Using the same string, replace only the first "apple".

# Use the third argument of replace().

new_text2=text1.replace("apple","mango",1)
print(new_text2)


# Task 28 — Check Immutability
# Create:

# text = "Python"
# Call:

# text.upper()
# Then print text.

# Observe whether the original string changed.

# Then store the result back into text and print it again.

text2="Python"
text2.upper()
print(text2)
text2=text2.upper()
print(text2)


# Task 29
# Create:

# text = "   Python Programming   "
# Use:

# strip()
# lstrip()
# rstrip()
# Observe the difference between the three methods.

text3="   Python Programming   "
print(text3.strip())
print(text3.lstrip())
print(text3.rstrip())



# Task 30 — User Input
# Take a name from the user using input().

# Assume the user may accidentally enter spaces before or after the name.

# Remove the extra surrounding spaces and display the cleaned name.

inp_name=input("Enter your name:")
inp_name=inp_name.strip()
print(inp_name)



# Task 31 — Split
# Create:

# "Python is easy to learn"
# Use split() to convert it into a list of words.

# Display the resulting list.

new_text3="Python is easy to learn"
print(new_text3.split())



# Task 32 — Split with Separator
# Create:

# "apple,banana,mango,orange"
# Use split() to separate the fruits.


new_text4="apple,banana,mango,orange"
print(new_text4.split("'"))


# Task 33 — Join
# Create a list:

# words = ["Python", "is", "easy"]
# Use join() to create:

# Python is easy

words = ["Python", "is", "easy"]
result = " ".join(words)
print(result)



# Task 34 — Join with Different Separators
# Using a list of words, create:

# Python-is-easy
# Then create:

# Python/is/easy
# Use join().
word1=["Python","is","easy"]
print("-".join(word1))
print("/".join(word1))


# Task 35 — F-String
# Create variables for:

# Name
# Age
# City
# Use an f-string to create a sentence containing all three values.

age=17
print(f"My name is {name} and i am from {city} and my age is {age}")


# Task 36 — Arithmetic Inside F-String
# Create:

# a = 10
# b = 20
# Use an f-string to display:

# The sum is 30
# Do not calculate the result separately.

num1=10
num2=20
print(f"The result is {num1+num2}")


# Task 37
# Run each piece of code separately.

# Identify the error produced by each.

# A
# text = "Python"
# print(text[20])

#index error


# B
# text = "Python"
# text[0] = "J"

#TypeError: 'str' object does not support item assignment


# C
# age = 20
# print("Age: " + age)

#TypeError


# D
# text = "Python"
# print(text.index("Java"))

#ValueError: substring not found

# For each:

# Identify the error.
# Explain why it occurred.
# Write the corrected version where possible.


# Task 38 — Name Processor
# Create a program that takes a user's full name as input.

# Your program should:

# Remove extra spaces from the beginning and end.
# Display the original input.
# Display the cleaned name.
# Display the name in uppercase.
# Display the name in lowercase.
# Display the name in title case.
# Display the length of the name.
# Display the first character.
# Display the last character.
# Check whether the name contains a particular character.


fname1=input("Enter your name")
cleaned_name=fname1.strip()
print(f"Original input:{fname1}")
print(f"cleaned name:{cleaned_name}")
print(f"Uppercase:{cleaned_name.upper()}")
print(f"Lowercase:{cleaned_name.lower()}")
print(f"Title Case:{cleaned_name.title()}")
print(f"Length:{len(cleaned_name)}")
print(f"First Character:{cleaned_name[0]}")
print(f"Last Character:{cleaned_name[-1]}")
print(f"Does the name contain 'a'? {'a' in cleaned_name}")




# Task 39 — Sentence Analyzer
# Take a sentence from the user.

# Your program should display:

# The original sentence.
# Number of characters.
# Number of words.
# First character.
# Last character.
# Sentence in uppercase.
# Sentence in lowercase.
# Sentence in title case.
# Whether "Python" exists in the sentence.
# Number of times a chosen character occurs.

sentence=input("Enter a sentence:")
print(f"Original sentence:{sentence}")
print(f"Number of characters:{len(sentence)}")
print(f"Number of words: {len(sentence.split())}")
print(f"The first Character:{sentence[0]}")
print(f"The last character:{sentence[-1]}")
print(f"Uppercase:{sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Title Case: {sentence.title()}")
print(f"Does the word Python exist in the sentence? { 'Python' in sentence }")
print(f"Number of times 'i' occurs: {sentence.count('i')}")




# Task 40 — Student Information
# Create a program that takes the following information from the user:

# First name
# Last name
# City
# Course
# Age
# The program should:

# Remove unnecessary spaces from text inputs.
# Create the full name.
# Display the full name in title case.
# Display the full name in uppercase.
# Display the full name in lowercase.
# Display the length of the full name.
# Display the first character of the full name.
# Display the last character of the full name.
# Display the city and course.
# Display the age using an f-string.
# Check whether the course contains "Python".
# Replace one word in the course name with another word.
# Display the number of words in the course name.



name1=input("Enter your first name:")
name2=input("Enter your last name:")
city=input("Enter your city:")
course=input("Enter your course:")
age=int(input("Enter your age:"))

name1 = name1.strip()
name2 = name2.strip()
city = city.strip()
course = course.strip()

full_name = f"{name1} {name2}"

print(f"Full Name (Title Case): {full_name.title()}")

print(f"Full Name (Uppercase): {full_name.upper()}")

print(f"Full Name (Lowercase): {full_name.lower()}")

print(f"Length of Full Name: {len(full_name)}")

print(f"First Character of Full Name: {full_name[0]}")

print(f"Last Character of Full Name: {full_name[-1]}")

print(f"City: {city}")
print(f"Course: {course}")

print(f"Age: {age}")

print(f"Does the course contain 'Python'? {'Python' in course}")

course_replaced = course.replace("Java", "Python")
print(f"Course with replaced word: {course_replaced}")

print(f"Number of words in Course Name: {len(course.split())}")