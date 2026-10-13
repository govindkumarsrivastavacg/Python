



# Q1. Stop Before Printing 5
# Predict the output.

# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")

#1
#2
#3
#4
#Finished



# Q2. Stop at the First Vowel
# Predict the output.

# word = "skyline"

# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)


#s
#k
#y
#l



# Q3. break in a while Loop
# Predict the output.

# n = 2

# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2



#2
#4
#6



# Q4. Stop at a Target Number
# Take an integer limit. Print numbers from 1 through limit, but stop before printing 7.

# If limit is less than 7, print all numbers up to limit.

# Test cases

# Input Expected output

# 10 1 2 3 4 5 6 5 1 2 3 4 5 7 1 2 3 4 5 6

# Print the numbers on one line, separated by spaces.

# limit=int(input("Enter the limit: "))
# for i in range(1,limit+1):
#     if(i==7):
#         break
#     print(i)



# Q5. Find the First Matching Character
# Take a string and a target character. Scan the string from left to right. Print each character as it is checked. Stop immediately after finding the target.

# If the target does not appear, check the entire string.

# Test cases

# Input string Target Expected checked characters

# Str=input("Enter a string: ")
# char=input("Enter a character: ")
# for i in Str:
#     if(i==char):
#         print(i)
#         break
#     print(i)
# else:
#     print("Checked")




# Q6. Stop at a Negative Number
# Given a sequence of integers, print numbers from left to right and stop when the first negative number is encountered. Do not print the negative number.

# Test cases

# Input Expected output

# l1=[0,4,8,9,-5,-9,7,5]
# for i in l1:
#     if(i<0):
#         break
#     print(i)


# Q7. break Only Exits the Inner Loop
# Predict the output.

# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)
# Explain why the outer loop continues.

# (1,1)
# (1,2)
# (2,1)
# (2,2)
# (3,1)
# (3,2)
# (4,1)
# (4,2)


# Q8. Search a Word
# Take a sentence and a target word. Check the words from left to right. Print "Found" and stop when the target word is found. If the target is absent, print "Not found".

# Test cases

# Sentence Target Expected output


# sentence=input("Enter a sentence: ").strip().split()

# target=input("Enter a target word: ").strip

# for word in sentence:
#     if(word==target):
#         print("Found")
#         break
# else:
#     print("Not found")

# Q9. Skip Number 4
# Predict the output.

# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)

# 1 2 3 5 6



# Q10. Skip Vowels
# Predict the output.

# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")


# ectn


# Q11. continue in a while Loop
# Predict the output.

# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

# 124




# Q12. Print Numbers That Are Not Multiples of 3
# Take an integer n. Print numbers from 1 to n, skipping multiples of 3.

# Test cases

# Input Expected output

# n=int(input("Enter the range: "))
# for i in range(1,n+1):
#     if(i%3==0):
#         continue
#     print(i)



# Q13. Remove a Chosen Character from Display
# Take a string and a character. Print the string without displaying any occurrence of that character. Do not use string replacement methods; use a loop and continue.

# Test cases

# String Character Expected output

# Str=input("Enter a string: ").strip()
# chosen=input("Enter the character you want to remove: ")
# for i in Str:
#     if i==chosen:
#         continue
#     print(i,end="")


# Q14. Print Only Passing Marks
# Given marks separated by spaces, print only marks that are at least 40. Use continue to skip marks below 40.

# Test cases

# Input Expected output

# marks=input('Enter the marks: ').strip().split()
# print("The passing marks are given below: ")
# for i in marks:
#     if(int(i)<40):
#         continue
#     print(int(i),end=" ")



# Q15. continue Does Not Skip the Whole Loop
# Predict the output.

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)
# Which lines are skipped when i == 2?

# A 1
# B 1
# A 3
# B 3
# A 4
# B 4


# Q16. Fix the Infinite Loop
# The following program does not finish. Rewrite it so that it skips 3 and prints 1, 2, 4, and 5.

# n = 0

# while n < 5:
#     if n == 3:
#         continue
#     n += 1
#     print(n)

# n=1
# while(n<=5):
#     if n==3:
#         continue
#     print(n)
#     n+=1


# Q17. Count Non-Vowel Characters
# Take a word and count how many characters are not vowels. Use continue to skip vowels.

# Test cases

# Input Expected output

# education 4 rhythm 6 apple 3

# For this question, treat a, e, i, o, and u as vowels.

# Str=input("Enter a string: ").strip()
# count=0
# for i in Str:
#     if(i in'aeiouAEIOU'):
#         continue
#     count+=1
# print(count)



# Q18. Normal Completion
# Predict the output.

# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")


# 1
# 2
# 3
# Done


# Q19. Completion After continue
# Predict the output.

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")


# 1
# 3
# 4
# Completed


# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")


# 1
# 2
# outside loop


# Q21. Empty Iterable
# Predict the output.

# for item in []:
#     print("Inside")
# else:
#     print("Else block")

# Else block


# Q22. Search for a Number
# Take a list of integers and a target number. If the target exists, print "Found". Otherwise, print "Not found" using for-else.

# Test cases

# List Target Expected output


# chosen=int(input("Enter the chosen number: "))
# num=input("Enter the numbers: ").strip().split()
# for i in num:
#     if(int(i)==chosen):
#         print("Found")
#         break
# else:
#     print("Not found")


# Q23. Check Whether a Character Exists
# Take a string and a target character. Use for-else to print "Character exists" if found, or "Character missing" otherwise.

# Test cases

# String Target Expected output


# chosen=(input("Enter the chosen character: "))
# Str=input("Enter the String: ").strip()
# for i in Str:
#     if(i==chosen):
#         print("Found")
#         break
# else:
    # print("Character Missing")



# Q24. Find the First Divisor
# Take a positive integer n greater than 1. Search for a divisor from 2 through n - 1. If a divisor is found, print "Not prime" and stop. If the loop finishes without finding one, print "Prime" using for-else.

# num=int(input("Enter a number: "))
# for i in range(2,num-1):
#     if(num%i==0):
#         print("Not prime")
#         break
# else:
#     print("Prime")


# Q25. Trace the else
# Predict the output.

# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

# All are even




# Q26. Does else Run?
# For each case, state whether the loop's else block runs and explain why.

# Case A

# for x in range(3):
#     continue
# else:
#     print("A")

# Yes

# Case B

# for x in range(3):
#     break
# else:
#     print("B")

# No

# Case C

# for x in range(0):
#     print(x)
# else:
#     print("C")

# Yes


# Q27. Find the First Repeated Character
# Given a string, scan each character and check whether it appears again later in the string. Stop at the first character that meets your chosen repeated-character rule and print it. If no character repeats, use for-else to print "No repeated character".

# Str=input("Enter a string: ").strip()
# x=0
# for i in Str:
#     for j in Str[x+1:]:
#         if i==j:
#             print(i)
#             break
#     else:
#         x+=1
#         continue
#     break
# else:
#     print("No Characters Repepated")



# Q28. pass Inside a Loop
# Predict the output.

# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

# 1 2 3

# 29. Empty if Block
# Predict the output.

# x = 10

# if x > 5:
#     pass

# print("Finished")

# Finished


# Q30. pass in a Loop Body
# Predict the output.

# for letter in "cat":
#     pass

# print("Loop ended")

# Loop ended


# Q31. Create a Placeholder for Future Work
# Write a program with a for loop from 1 to 5. Inside the loop, use pass when the number is even. Print every number after the conditional block.

# Test cases

# Input range Expected output

# 1 to 5 1 2 3 4 5 1 to 3 1 2 3

# Explain why the even numbers are still printed.

# for i in range(1,6):
#     if i%2==0:
#         pass
#     print(i)



# Q32. Incomplete Menu Option

# Write a simple menu-like program using if / elif / else. For one option, put pass as a temporary placeholder. Print "Program closed" after the conditional structure.

# Test cases

# Choice Expected output
#    `1` The message for option 1, then `Program closed`
#    `2` No action for option 2, then `Program closed`
#    `9` The message for an unknown option, then `Program closed`
# Choose and clearly document the messages for options 1 and 9.


# choice=int(input('Enter a chooice: '))
# if choice==1:
#     print("The message for option 1")
# elif(choice==2):
#     pass
# elif(choice==9):
#     print("The message for unknown option")

# print("Program Closed")


# Q33. Compare pass and continue
# Predict the output of each program.

# Program A

# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)

# 1 2 3 4

# Program B

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)
# Explain the difference.

# 1 2 4 


# Q34. Complete the Skeleton
# Fill in the blank with exactly one of break, continue, or pass so the output is 1 2 4 5.

# for i in range(1, 6):
#     if i == 3:
#         ______
#     print(i)
# Explain why the other two choices do not produce the required output.


# continue



# Q35. Output Prediction
# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finished")
# Write the exact output and explain why else does or does not run.

#  1 3


# Q36. Search and Report
# Write a program that searches for a target number in a list.

# Skip negative numbers using continue.
# Stop when the target is found using break.
# Use for-else to print "Target not found" if the loop finishes without finding the target.
# Test cases

# List Target Expected output


# chosen=int(input("Enter the chosen number: "))
# num=input("Enter the numbers: ").strip().split()
# for i in num:
#     if(int(i)<0):
#         continue
#     if(int(i)==chosen):
#         print("Found")
#         break
# else:
#     print("Not found")



# Q37. Skip, Stop, or Complete?
# Write a program that reads integers from a list in order:

# Skip 0 using continue.
# Stop before printing -1 using break.
# If the loop finishes without encountering -1, print "All values processed" using for-else.
# Test cases

# Input Expected output

# num=input("Enter the numbers: ").strip().split()
# for i in num:
#     if(int(i)==0):
#         continue
#     if(int(i)==-1):
#         break
#     print(i)
# else:
#     print("All values processed")


# Q38. Understand Nested Loops
# Predict the output.

# for row in range(1, 4):
#     for col in range(1, 4):
#         if col == 2:
#             continue
#         if row == 3:
#             break
#         print(row, col)
#     else:
#         print("Inner loop completed")

# 1,1
# 1,3
# inner loop completed
# 2,1
# 2,3
# inner loop completed



# Q39. Find the First Number Divisible by Both 4 and 6
# Given a list of integers, find the first number divisible by both 4 and 6. Skip negative numbers using continue. Stop when a matching number is found using break. Use for-else to report when no matching number exists.


# num=input("Enter the numbers: ").strip().split()
# for i in num:
#     if(int(i)<0):
#         continue
#     if(int(i)%4==0 and int(i)%6==0):
#         print(i)
#         break
# else:
#     print("No matching number")




# Q40. Explain the Best Statement
# For each situation, choose the most suitable option: break, continue, for-else, or pass. Some situations may need more than one.

# Stop searching immediately after finding a username.  break
# Skip a blank string and process the remaining strings.  continue
# Display "Not found" only when a search loop finishes without finding a match.  else
# Keep an unfinished function syntactically valid while its implementation is planned. pass
# Skip the current number but keep processing later numbers. continue
# Stop a loop when a user enters a sentinel value. break
# Report that all items were checked, provided no match caused an early stop. else
# Temporarily leave a conditional block empty without causing a syntax error. pass