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




# 11. Username Analyzer
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
        

# ct_dig=0
# ct_un=0
# invalid=False
# for i in range(5):
#     name=input("Enter the username: ").lower()
#     length=len(name)
#     for char in name:
#         print(name[0])
#         if(char>='0' and char<='9'):
#             ct_dig+=1
#         elif(char=='_'):
#             ct_un+=1
#         elif(not(char>='a' and char<='z')):
#             invalid=True
#     if(invalid):
#         print("Invalid username")
#     else:
#         if(length>8 and ct_dig>0 and ct_un>0):
#             print("Valid")
#         else:
#             print("Needs improvement")



# 12. Vowel-Consonant Battle
# Take a sentence.

# Count vowels and consonants.

# Then:

# Print "Vowels Win" if vowels are greater.
# Print "Consonants Win" if consonants are greater.
# Print "Draw" if equal.
# Also print the frequency of each vowel.

# ct_vow=0
# ct_con=0
# Sen=input("Enter a sentence").lower()
# for char in Sen:
#     if(char in "aeiou"):
#         ct_vow+=1
#     elif(char>='a' and char<='z'):
#         ct_con+=1
# if(ct_vow>ct_con):
#     print("Vowels win")
# elif(ct_con>ct_vow):
#     print("Consonants Win")
# else:
#     print("Draw")
# print("Frequency of vowels: ",ct_vow)




# 13. Electricity Bill Calculator
# Take electricity usage for 6 customers.

# Calculate the bill using:

# First 100 units → ₹5/unit
# Next 100 units → ₹7/unit
# Next 200 units → ₹10/unit
# Above 400 units → ₹15/unit
# Also classify:

# Below ₹1000 → "Low"
# ₹1000–₹3000 → "Medium"
# Above ₹3000 → "High"
# Print total revenue.

# for i in range(6):
#     unit=int(input("Enter the units: "))
#     if(unit<=100):
#         bill=5*unit
#     elif(unit<=200):
#         bill=500+7*(unit-100)
#     elif(unit<=400):
#         bill=1200+10*(unit-200)
#     elif(unit>400):
#         bill=3200+15*(unit-400)
#     if(bill>3000):
#         cat="High"
#     elif(bill>=1000):
#         cat="Medium"
#     else:
#         cat="Low"
#     print(f"The bill is: {bill}")
#     print(cat)



# 14. Word Character Balance
# Take a sentence.

# For every word:

# Count vowels.
# Count consonants.
# If vowels > consonants → "Vowel Heavy"
# If consonants > vowels → "Consonant Heavy"
# Otherwise → "Balanced"
# Print the result for every word.


# ct_vow=0
# ct_con=0
# Sen=input("Enter a sentence").lower().strip().split()
# for word in Sen:
#     for char in word:
#         if(char in "aeiou"):
#             ct_vow+=1
#         elif(char>='a' and char<='z'):
#             ct_con+=1
#     if(ct_vow>ct_con):
#         print("Vowel Heavy")
#     elif(ct_con>ct_vow):
#         print("Consonants Heavy")
#     else:
#         print("Balanced")


# 15. Matrix Value Analyzer
# Take a 3 × 3 matrix using nested for loops.

# For every number:

# Identify even/odd.
# Identify positive/negative/zero.
# At the end, print:

# Even count
# Odd count
# Positive count
# Negative count
# Zero count
# Largest number
# Do not use max().


# ct_even=0
# ct_odd=0
# ct_pos=0
# ct_neg=0
# ct_zero=0
# mat=int(input("Enter the number of rows in the matrix: "))
# for row in range(1,mat+1):
#     for col in range(1,mat+1):
#         num=int(input("Enter the element"))
#         if(row==1 and col==1):
#             larg=num
#         if(num>larg):
#             larg=num
#         if(num%2==0):
#             ct_even+=1
#         if(num%2!=0):
#             ct_odd+=1
#         if(num>0):
#             ct_pos+=1
#         if(num<0):
#             ct_neg+=1
#         if(num==0):
#             ct_zero+=1
#     print()
# print("Even count is: ",ct_even)
# print("odd count is: ",ct_odd)
# print("positive count is: ",ct_pos)
# print("negative count is: ",ct_neg)
# print("zero count is: ",ct_zero)
# print(f"The largest element is: {larg}")



# 16. Password Character Distribution
# Take a password.

# Count:

# Uppercase
# Lowercase
# Digits
# Special characters
# Calculate the percentage of each category.

# Then classify the password based on which category dominates.

# ct_up=0
# ct_lw=0
# ct_spe=0
# ct_dig=0
# count=0
# Pass=input("Enter the password: ")
# length=len(Pass)
# for char in Pass:
#     if(char>='A' and char<='Z'):
#          ct_up+=1
#     elif(char>='a' and char<='z'):
#         ct_lw+=1
#     elif(char>='0' and char<='9'):
#         ct_dig+=1
#     else:
#         ct_spe+=1

# per_up=(ct_up/length)*100
# per_lw=(ct_lw/length)*100
# per_dig=(ct_dig/length)*100
# per_spe=(ct_spe/length)*100
# print(f"PErcetage of uppercase: {per_up}")
# print(f"PErcetage of lowercase: {per_lw}")
# print(f"PErcetage of dig: {per_dig}")
# print(f"PErcetage of speical: {per_spe}")

# if(ct_up>ct_lw and ct_up>ct_dig and ct_up>ct_spe):
#     print("UpperCase characters dominate")
# elif(ct_lw>ct_up and ct_lw>ct_dig and ct_lw>ct_spe):
#     print("LowerCase characters dominate")
# elif(ct_dig>ct_lw and ct_dig>ct_up and ct_dig>ct_spe):
#     print("digit characters dominate")
# elif(ct_spe>ct_lw and ct_spe>ct_up and ct_spe>ct_dig):
#     print("speical characters dominate")
# else:
#     print("Tie")



# 17. Student Name and Marks
# Take the name and marks of 5 students.

# For every student:

# Calculate grade.
# Count vowels in the student's name.
# Count characters in the name.
# Print whether the name has more vowels or consonants.
# Finally, print the student with the highest marks.

# Do not use max().
# high=0
# topper=""
# for i in range(5):
#     ct_vow=0
#     ct_cons=0
#     ct_name=0
#     name=input("Enter the name: ").lower().strip()
#     marks=int(input("Enter marks: "))
#     if(marks>=90):
#         grade="A"
#     elif(marks>=75):
#         grade="B"
#     elif(marks>=50):
#         grade="C"
#     elif(marks>35):
#         grade="D"
#     else:
#         grade="F"
#     print(f"The grade is: {grade}")
#     for char in name:
#         if(char in "aeiou"):
#             ct_vow+=1
#         elif(char>='a' and char<='z'):
#             ct_cons+=1
#     print(f"The number of characters in name: {len(name)}")
#     if(ct_vow>ct_cons):
#         print("Vowels appear more")
#     else:
#         print("Consonants appear more")
#     if(marks>high):
#         high=marks
#         topper=name
# print(f"The highest marks are of {topper}")



# 18. ATM Transaction Analyzer
# Take transactions for 7 days.

# Each transaction can be:

# Deposit
# Withdrawal
# For every transaction:

# Update balance.
# Reject withdrawal if balance is insufficient.
# Print "Low Balance" if balance falls below ₹1000.
# At the end, print final balance and transaction counts.

# balance=int(input("Enter the balance: "))
# tran_ct=0
# for i in range(7):
#     print("The current balance is: ",balance)
#     act=input("Do you want to withdraw or deposit? :").strip().lower()
#     if(act=="withdraw"):
#         amt=int(input("Enter the amount you want to withdraw: "))
#         if(balance>amt):
#             balance=balance-amt
#             tran_ct+=1
#         else:
#             print("Insufficient amount")
#     elif(act=="deposit"):
#         amt=int(input("Enter the amount you want to deposit: "))
#         balance=balance+amt
#         tran_ct+=1
#     else:
#         print("Learn how to spell")
#         continue
#     if(balance<1000):
#         print("Low Balance")
# print(f"The final balance is: {balance}")
# print(f"The transaction count is: {tran_ct}")
    

# 19. Sentence Security Scanner
# Take a sentence.

# Detect whether it contains:

# Digits
# URLs-like text containing .
# @
# Password-like patterns
# Repeated special characters
# Print a security classification:

# "Safe"
# "Review"
# "Suspicious"

# flag_dig=False
# flag_pass=False
# flag_dot=False
# flag_spe=False
# flag_at=False
# ct_spe=0
# count=0
# sen=input("Enter a string: ").strip()
# for char in sen.lower():
#     if(char=='.' and flag_dot==False):
#         flag_dot=True
#         count+=1
#     elif(char=='@' and flag_at==False):
#         flag_at=True
#         count+=1
#         count+=1
#     elif(char>='0' and char<='9') and flag_dig==False:
#         flag_dig=True
#         count+=1
#     elif(not(char>='a' and char<='z' ) and char!=" "):
#         ct_spe+=1
# if(ct_spe>1) and flag_spe==False:
#     flag_spe=True
#     count+=1
# if(flag_spe and flag_dig) and flag_pass==False:
#     flag_pass=True
#     count+=1

# if(count==6):
#     print("Suspicious")
# elif(count>2):
#     print("Review")
# else:
#     print("Safe")


# 20. Multiplication Grid Analyzer
# Take n.

# Generate an n × n multiplication grid using nested loops.

# For every result:

# Print "E" if even.
# Print "O" if odd.
# Print "F" if divisible by 5


# n=int(input("Enter the number of rows: "))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         result=row*col
#         if(result%5==0):
#             print('F', end="")
#         elif(result%2!=0):
#             print('O',end="")
#         elif(result%2==0):
#             print('E',end="")
#     print()



# 21. Shopping Discount System
# Take prices of 10 products.

# Apply:

# ≥ ₹5000 → 20% discount
# ≥ ₹3000 → 15%
# ≥ ₹1000 → 10%
# Otherwise → no discount
# Then:

# Calculate final price.
# Count how many products received each discount.
# Calculate total discount.



# Total=0
# total_dis=0
# ct_20dis=0
# ct_15dis=0
# ct_10dis=0
# ct_nodis=0
# for i in range(10):
#     dis=0
#     price=int(input("Enter the price of the product: "))
#     if(price>=5000):
#         dis=price*(20/100)
#         ct_20dis+=1
#     elif(price>=3000):
#         dis=price*(15/100)
#         ct_15dis+=1
#     elif(price>=1000):
#         dis=price*(10/100)
#         ct_10dis+=1
#     else:
#         ct_nodis+=1
#     total_dis+=dis
#     price-=dis
#     Total+=price
# print()
# print(f"The total price is: {Total}")
# print(f"No. of products that got 20% discount: {ct_20dis}")
# print(f"No. of products that got 15% discount: {ct_15dis}")
# print(f"No. of products that got 10% discount: {ct_10dis}")
# print(f"No. of products that got no discount: {ct_nodis}")
# print(f"The total discount is: {total_dis}")


# 22. String Compression Counter
# Take a string such as:

# aaabbccccdd
# Print:

# a3b2c4d2
# Use loops and conditions.

# Do not use libraries for compression


# Str=input("Enter a string: ")
# x=0

# for char in Str:
#     flag=False
#     count=0
#     y=0
#     for j in Str:
#         if(Str[x]==Str[x-1] and x!=0):
#             flag=True
#         if(char==j ):
#             if(y<x):
#                 flag=True
#                 break
                
#             else:
#                 count+=1
#         y+=1
#     if(flag==False):
#         print(char+str(count),end="")
#     x+=1
   



# comp=""
# Str=input("Enter a string: ").strip()
# x=0
# for i in Str:
#     ct=""
#     count=0
#     y=x
#     for j in Str:
#         if(y<len(Str)):
#             if(x==0):
#                 if(Str[x]!=Str[y]):
#                     break
#                 else:
#                     count+=1
#             else:
#                 if(Str[x]==Str[x-1]):
#                     break
#                 else:
#                     if(Str[x]!=Str[y]):
#                         break
#                     else:
#                         count+=1
#         y+=1
#     x+=count
#     ct=str(count)
#     comp=comp+i+ct
# print(comp)






# 23. Employee Salary Analyzer
# Take salaries of 8 employees.

# Classify:

# Below ₹25,000 → "Junior"
# ₹25,000–₹50,000 → "Mid"
# ₹50,001–₹1,00,000 → "Senior"
# Above ₹1,00,000 → "Executive"
# Print counts and average salary.



# total=0
# ct_jr=0
# ct_mid=0
# ct_sr=0
# ct_exe=0
# for i in range(8):
#     salary=int(input("Enter the salary: "))
#     if(salary>100000):
#         ct_exe+=1
#     elif(salary>50000):
#         ct_sr+=1
#     elif(salary>25000):
#             ct_mid+=1
#     else:
#          ct_jr+=1
#     total+=salary
# print(f"No of executive employees are: {ct_exe}")
# print(f"No of senior employees are: {ct_sr}")
# print(f"No of mid employees are: {ct_mid}")
# print(f"No of junior employees are: {ct_jr}")
# avg=total/8
# print(f"The average salary is: {avg}")




# 24. Secret Word Detector
# Take a sentence and a secret word.

# Check whether the secret word exists without using the in operator.

# If found:

# Print its starting position.
# Print how many times it occurs.
# If not found, print "Secret word not found".

# flag=False
# count=0
# sent=input("Enter a sentence: ").strip().split()
# secret=input("Enter the secret word: ").strip()
# x=0
# start=0
# for i in sent:
#     if(i==secret):
#         if(flag==False):
#             start=x
#         flag=True
#         count+=1
#     x+=1
# if(flag):
#     print(f"The starting position of the secret word is: {start}")
#     print(f"It appears {count} times")
# else:
#     print("Secret word not found")



# 25. Number Pyramid With Classification
# Take n.

# For every number printed in the pyramid:

# Even → print E
# Odd → print O
# Divisible by 3 → print T
# Divisible by both 3 and 5 → print F
# Use nested loops.

# n=int(input("Enter the number of rows: "))
# N=n*2
# start=N/2
# count=1
# for i in range(1,n+1):
#     ct=count
#     num=1
#     for j in range(1,N+1):
#         if(j<start ):
#             print(" ",end="")
#         elif(j>=start and ct>0):
#             if(num%5==0 and num%3==0):
#                 print("F",end="")
#             elif(num%3==0):
#                 print("T",end="")
#             elif(num%2==0):
#                 print("E",end="")
#             else:
#                 print("O",end="")
#             ct-=1
#             num+=1
#     start-=1
#     count+=2
#     print()


# 26. Movie Rating Analyzer
# Take ratings of 10 movies.

# Classify:

# 0–3 → "Poor"
# 3.1–5 → "Average"
# 5.1–7 → "Good"
# 7.1–9 → "Excellent"
# 9.1–10 → "Outstanding"
# Print category counts and average rating.


