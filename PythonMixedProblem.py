# 1. Digit and Character Analyzer
# Take a string containing letters, digits, spaces, and special characters.

# Using a for loop:

# Count uppercase letters.
# Count lowercase letters.
# Count digits.
# Count spaces.
# Count special characters.
# Print which category has the highest count.
# If two or more categories have the same highest count, print "Tie".

# Str=input("Enter a string: ")
# ct_up=0
# ct_lw=0
# ct_dig=0
# ct_spac=0
# ct_spe=0

# for i in Str:
#     if(i>='A' and i<='Z'):
#         ct_up+=1
#     elif(i>='a' and i<='z'):
#         ct_lw+=1
#     elif(i>='0' and i<='9'):
#         ct_dig+=1
#     elif(i==" "):
#         ct_spac+=1
#     else:
#         ct_spe+=1
# if(ct_up>ct_lw and ct_up>ct_dig and ct_up>ct_spac and ct_up>ct_spe):
#     print("UpperCase characters have the highest count")
# elif(ct_lw>ct_up and ct_lw>ct_dig and ct_lw>ct_spac and ct_lw>ct_spe):
#     print("LowerCase characters have the highest count")
# elif(ct_dig>ct_lw and ct_dig>ct_up and ct_dig>ct_spac and ct_dig>ct_spe):
#     print("digit characters have the highest count")
# elif(ct_spac>ct_lw and ct_spac>ct_up and ct_spac>ct_dig and ct_spac>ct_spe):
#     print("space characters have the highest count")
# elif(ct_spe>ct_lw and ct_spe>ct_up and ct_spe>ct_dig and ct_spe>ct_spac):
#     print("speical characters have the highest count")
# else:
#     print("Tie")




# 2. Student Performance Analyzer
# Take marks of 10 students using a for loop.

# For each student:

# Print "Fail" if marks are below 35.
# Print "Pass" for 35–49.
# Print "Good" for 50–74.
# Print "Excellent" for 75–100.
# At the end, print the number of students in each category.



# ct_pass=0
# ct_good=0
# ct_ex=0
# ct_fail=0
# for i in range(10):
#     marks=int(input("Enter marks: "))
#     if(marks>=75):
#         print("Excellent")
#         ct_ex+=1
#     elif(marks>=50):
#         print("Good")
#         ct_good+=1
#     elif(marks>=35):
#         print("Pass")
#         ct_pass+=1
#     else:
#         print("Fail")
#         ct_fail+=1

# print("Excellent students are:",ct_ex)
# print("Good students are:",ct_good)
# print("Pass students are:",ct_pass)
# print("Fail students are:",ct_fail)



# 3. Word Score Calculator
# Take a sentence.

# For every word:

# Vowel = 2 points.
# Consonant = 1 point.
# Digit = 3 points.
# Special character = 4 points.
# Calculate the score of every word and print the word with the highest score.

# Do not use max().
  

# Str=input("Write a sentence: ").strip().lower().split()
# point=0
# for word in Str[0:1]:
#     for char in word:
#         if(char=='a'or char=='i'or char=='e' or char=='o' or char=='u'):
#             point+=2
#         elif(char>='0' and char<='9'):
#             point+=3
#         elif(char>='a' and char<='z'):
#             point+=1
#         else:
#             point+=4
#     high=point
#     x=Str[0]
        
# i=0
# for word in Str[1:]:
#     point=0
#     for char in word:
#         if(char=='a'or char=='i'or char=='e' or char=='o' or char=='u'):
#             point+=2
#         elif(char>='0' and char<='9'):
#             point+=3
#         elif(char>='a' and char<='z'):
#             point+=1
#         else:
#             point+=4
#     i+=1
#     if(point>high):
#         high=point
#         x=Str[i]
# print("The word with the highest points is :",x)
# print("The points are: ",high)




# 4. Password Batch Validator
# Take passwords for 5 users using a for loop.

# For every password, check:

# Minimum length of 8.
# At least one uppercase letter.
# At least one lowercase letter.
# At least one digit.
# At least one special character.
# Print "Strong", "Medium", or "Weak" based on the number of conditions satisfied.


# for i in range(5):
#     ct_up=0
#     ct_lw=0
#     ct_spe=0
#     ct_dig=0
#     count=0
#     Pass=input("Enter the password: ")
#     if(len(Pass)>=8):
#         count+=1
#     for char in Pass:
#         if(char>='A' and char<='Z'):
#             ct_up+=1
#         elif(char>='a' and char<='z'):
#             ct_lw+=1
#         elif(char>='0' and char<='9'):
#             ct_dig+=1
#         else:
#             ct_spe+=1
#     if(ct_up>0):
#         count+=1
#     if(ct_dig>0):
#         count+=1
#     if(ct_lw>0):
#         count+=1
#     if(ct_spe>0):
#         count+=1
#     if(count==5):
#         print("Password is strong")
#     elif(count>=3):
#         print("Password is medium")
#     else:
#         print("Password is weak")




# 5. Sentence Word Analyzer
# Take a sentence and examine every word.

# For each word:

# Print its length.
# Print "Short" if length ≤ 3.
# Print "Medium" if length is 4–6.
# Print "Long" if length > 6.
# At the end, print the number of short, medium, and long words.


# Sent=input("Enter a sentence: ").strip().split()
# ct_long=0
# ct_med=0
# ct_short=0
# for word in Sent:
#     if(len(word)>6):
#         print("Long")
#         ct_long+=1
#     elif(len(word)>3):
#         print("Medium")
#         ct_med+=1
#     else:
#         print("Short")
#         ct_short+=1
# print(f"The Number of long words are: {ct_long}")
# print(f"The Number of medium words are: {ct_med}")
# print(f"The Number of short words are: {ct_short}")



# 6. Number-String Conversion Challenge
# Take 5 numbers from the user.

# For each number:

# Convert it to a string.
# Examine every digit using a loop.
# Count even and odd digits.
# Print which type occurs more.
# If equal, print "Equal".


# for i in range(5):
#     ct_even=0
#     ct_odd=0
#     Num=int(input("Enter a number: "))
#     Str=str(Num)
#     for char in Str:
#         j=int(char)
#         if(j%2==0):
#             ct_even+=1
#         else:
#             ct_odd+=1
#     if(ct_even>ct_odd):
#         print("Even digits occur more")
#     elif(ct_even<ct_odd):
#         print("Odd digits occur more")
#     else:
#         print("Equal")



# 7. Repeated Character Report
# Take a string.

# For every character, determine how many times it appears in the string without using count().

# Print only characters that appear more than once.

# Also classify them:

# 2 occurrences → "Duplicate"
# 3–4 occurrences → "Repeated"
# More than 4 → "Highly Repeated"


# Str=input("Enter a string: ")
# x=0
# for char in Str:
#     count=0
#     y=0
#     for j in Str:
#         if(char==j ):
#             if(y<x):
#                 break
#             else:
#                 count+=1
#         y+=1
#     if(count>4):
#         print(char)
#         print("Highly repetated")
#     elif(count>2):
#         print(char)
#         print("Repeated")
#     elif(count==2):
#         print(char)
#         print("Duplicate")
#     x+=1





# 8. Shopping Cart Analyzer
# Take prices of 8 products.

# For every price:

# Below 500 → "Budget"
# 500–1999 → "Regular"
# 2000–4999 → "Premium"
# 5000 or more → "Luxury"
# Calculate:

# Total amount.
# Number of products in each category.
# Average product price.


# ct_bud=0
# ct_reg=0
# ct_pre=0
# ct_lux=0
# total=0
# for i in range(8):
#     price=int(input("Enter the price: "))
#     if(price>=5000):
#         ct_lux+=1
#     elif(price>=2000):
#         ct_pre+=1
#     elif(price>=500):
#         ct_reg+=1
#     elif(price>=0):
#         ct_bud+=1
#     total=total+price
# avg_price=total/8
# print(f"The total price is: {total}")
# print(f"The average price is: {avg_price}")
# print(f"The number of luxury products are: {ct_lux}")
# print(f"The number of premium products are: {ct_pre}")
# print(f"The number of regular products are: {ct_reg}")
# print(f"The number of budget products are: {ct_bud}")



# 9. Character Position Challenge
# Take a string.

# For every character, print:

# Character
# Position
# Whether position is even or odd
# Whether character is vowel, consonant, digit, or special character
# At the end, count how many characters fall into each category.

# i=0
# ct_even=0
# ct_odd=0
# ct_vow=0
# ct_cons=0
# ct_dig=0
# ct_spe=0
# Str=input("Enter a string: ").strip().lower()
# for char in Str:
#     print(f"Character is: {char}")
#     print(f"Position is: {i}")
#     if(i%2==0):
#         ct_even+=1
#         print("Position is even")
#     else:
#         ct_odd+=1
#         print("Position is odd")
#     if(char in 'aeiou'):
#         ct_vow+=1
#         print("Character is a vowel")
#     elif(char >='a' and char<='z'):
#         ct_cons+=1
#         print("Character is a consonent")
#     elif(char >='0' and char<='9'):
#         ct_dig+=1
#         print("Character is a digit")
#     else:
#         ct_spe+=1
#         print("Character is a speical character")
#     i+=1
# print(f"Even:{ct_even}")
# print(f"odd:{ct_odd}")
# print(f"vowel:{ct_vow}")
# print(f"consonent:{ct_cons}")
# print(f"digit:{ct_dig}")
# print(f"speical:{ct_spe}")
        
        




# 10. Number Pattern With Conditions
# Take n.

# Print a pattern where each row contains numbers from 1 to the row number.

# Replace:

# Multiples of 3 with X
# Multiples of 5 with Y
# Multiples of both 3 and 5 with Z
# Example for n = 5:

# 1
# 1 2 X
# 1 2 X 4 Y
# 1 2 X 4 Y X 7
# 1 2 X 4 Y X 7 8 X
# Use nested for loops.


# n=int(input("Enter the number of rows: "))
# x=1
# print("1")
# for i in range(1,n+1):
#     for j in range (1,x+3):
#         if(j%3==0 and j%5==0):
#             print('Z',end="")
#         elif(j%5==0):
#             print('Y',end="")
#         elif(j%3==0):
#             print('X',end="")
#         else:
#             print(j,end="")
#     x+=2
#     print()




# 1. Username Analyzer
# Take 5 usernames.

# For every username:

# Check length.
# Check first character.
# Count digits.
# Count underscores.
# Detect invalid special characters.
# Classify each username as:

# "Valid"
# "Needs Improvement"
# "Invalid"
        

ct_dig=0
ct_un=0
for i in range(5):
    name=input("Enter the username: ")
    length=len(name)
    for char in name:
        print(name[0])


    