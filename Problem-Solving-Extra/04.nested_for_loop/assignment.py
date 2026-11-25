# Q1. Number Pair Generator
# Print all pairs (i, j) where both values range from 1 to 3.

# Test Case
# Input: No input

# Expected Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3


# n=int(input("enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"({i},{j})")


# Q2. Multiplication Pair
# Take N and print the multiplication result for every pair from 1 to N.

# Test Case
# Input: 3

# Expected Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

# n=int(input("enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i} x {j} = {i*j}")



# Q3. Repeated Character Grid
# Take a character, rows and columns. Print the character as a rectangle.

# Test Case
# Input: `*`, rows=3, columns=4

# Expected Output:
# ****
# ****
# ****

# rows=int(input("Enter the number of rows: "))
# columns=int(input("Enter the number of columns: "))
# c=input("Enter a character: ")


# for i in range(rows):
#     for j in range(columns):
#         print(c,end="")
#     print()


# Q4. Coordinate Grid
# Take rows and columns and print every coordinate.

# Test Case
# Input: rows=2, columns=3

# Expected Output:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)

# rows=int(input("Enter the number of rows: "))
# columns=int(input("Enter the number of columns: "))

# for i in range(rows):
#     for j in range(columns):
#         print(f"({i},{j})",end=" ")
#     print()


# Q5. Row Number Pattern
# Take N and print the row number N times in each row.

# Test Case
# Input: 4

# Expected Output:
# 1111
# 2222
# 3333
# 4444


# N=int(input("Enter the number of rows: "))
# for i in range(1,N+1):
#     for j in range(N):
#         print(i,end="")
#     print()


# Q6. Column Number Pattern
# Take N and print 1 to N in every row.

# Test Case
# Input: 4

# Expected Output:
# 1234
# 1234
# 1234
# 1234



# N=int(input("Enter the number of rows: "))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(j,end="")
#     print()


# Q7. Increasing Number Grid
# Take N and print 1, then 12, then 123, and so on.

# Test Case
# Input: 4

# Expected Output:
# 1
# 12
# 123
# 1234

# N=int(input("Enter the number of elements in the last row: "))
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# Q8. Decreasing Number Grid
# Take N and print 1..N, then one fewer number on every row.

# Test Case
# Input: 4

# Expected Output:
# 1234
# 123
# 12
# 1


# N=int(input("Enter the number of elements in the last row: "))
# for i in range(N,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



# Q9. Star Rectangle
# Take rows and columns and print a rectangle of *.

# Test Case
# Input: rows=3, columns=5

# Expected Output:
# *****
# *****
# *****


# rows=int(input("Enter the number of rows: "))
# columns=int(input("Enter the number of columns: "))


# for i in range(rows):
#     for j in range(columns):
#         print("*",end="")
#     print()


# Q10. Alternating 0 and 1
# Take N and print an N×N grid where columns alternate between 0 and 1.

# Test Case
# Input: 4

# Expected Output:
# 0101
# 0101
# 0101
# 0101

# N=int(input("Enter the number of rows: "))
# for i in range(N):
#     for j in range(N):
#         if(j%2==0):
#             print("0",end="")
#         else:
#             print("1",end="")
#     print()


# Q11. Even Number Grid
# Print only even column values for every row.

# Test Case
# Input: rows=3, columns=6

# Expected Output:
# 2 4 6
# 2 4 6
# 2 4 6


# row=int(input("Enter the number of rows: "))
# col=int(input("Enter the number of columns: "))
# for i in range(row):
#     x=2
#     for j in range(col):
#         if(j%2==0):
#             print(" ",end="")
#         else:
#             print(x,end=" ")
#             x+=2
#     print()


# Q12. Odd Number Grid
# Print odd numbers from 1 to N in every row.

# Test Case
# Input: N=7

# Expected Output:
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7


# N=int(input("Enter the number of rows: "))
# for i in range(N):
#     x=1
#     for j in range(1,N+1):
#         if(j%2==0):
#             print(" ",end="")
#         else:
#             print(x,end=" ")
#             x+=2
#     print()


# Q13. Even-Odd Classification
# For i and j from 1 to 4, print E when i+j is even, otherwise O.

# Test Case
# Input: No input

# Expected Output:
# E O E O
# O E O E
# E O E O
# O E O E

# row=int(input("Enter the number of rows: "))
# for i in range(row):
#     for j in range(row):
#         if((i+j)%2==0):
#             print("E",end=" ")
#         else:
#             print("O",end=" ")
#     print()


# Q14. Equal Coordinate Detector
# For every pair from 1 to 5, print Same when i==j, otherwise Different.

# Test Case
# Input: N=3

# Expected Output:
# Same Different Different
# Different Same Different
# Different Different Same


# row=int(input("Enter the number of rows: "))
# for i in range(row):
#     for j in range(row):
#         if i==j:
#             print("Same",end=" ")
#         else:
#             print("Different",end=" ")
#     print()


# Q15. Diagonal Values
# Create an N×N grid with 1 on the main diagonal and 0 elsewhere.

# Test Case
# Input: N=4

# Expected Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

# row=int(input("Enter the number of rows: "))
# for i in range(row):
#     for j in range(row):
#         if i==j:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()


# Q16. Number Divisibility Grid
# For i,j from 1 to 5, print X if i is divisible by j, otherwise -.

# Test Case
# Input: No input

# Expected Output:
# X - - - -
# X X - - -
# X - X - -
# X X - X -
# X - - - X

# row=int(input("Enter the number of rows: "))
# for i in range(1,row+1):
#     for j in range(1,row+1):
#         if i%j==0:
#             print("X",end=" ")
#         else:
#             print("-",end=" ")
#     print()


# Q17. Multiples Detector
# For every i from 1 to N, print values j from 1 to N that are multiples of i.

# Test Case
# Input: N=4

# Expected Output:
# 1 2 3 4
# 2 4
# 3
# 4

# N=int(input("enter the number of rows: "))
# for i in range(1,N+1):
#     j=1
#     while (i*j<=N):
#         print(i*j,end=" ")
#         j+=1
#     print()


# Q18. Pair Sum Filter
# Print all pairs from 1 to N whose sum is greater than N.

# Test Case
# Input: N=4

# Expected Output:
# 1 4
# 2 3
# 2 4
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4

# N=int(input("Enter the Number: "))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if(i+j>N):
#             print(f"{i} {j}")


# Q19. Pair Product Filter
# Print pairs and products only when the product is even.

# Test Case
# Input: N=3

# Expected Output:
# 1 2 2
# 2 1 2
# 2 2 4
# 2 3 6
# 3 2 6

# N=int(input("Enter the Number: "))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if(i*j)%2==0:
#             print(f"{i} {j} {i*j}")



# Q20. Special Coordinate
# Print SPECIAL for i==j, PAIR for i+j==N, otherwise NORMAL. Decide condition priority carefully.

# Test Case
# Input: N=4

# Expected Output: A 4×4 classification grid; diagonal positions are SPECIAL and remaining sum-4 positions are PAIR.


# N=int(input("Enter the Number: "))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i==j:
#             print("SPEICAL",end=" ")
#         elif(i+j==N):
#             print("PAIR",end=" ")
#         else:
#             print("NORMAL",end=" ")
#     print()


# Q21. Character Repetition
# For every character, print it three times.

# Test Case
# Input: `CAT`

# Expected Output:
# CCC
# AAA
# TTT


# Str=input("Enter the word: ")
# for i in Str:
#     print(i*len(Str))



# Q22. Character with Position
# For every character, print it with repetition numbers 0,1,2.

# Test Case
# Input: `AB`

# Expected Output:
# A 0
# A 1
# A 2
# B 0
# B 1
# B 2

# Str=input("Enter a string: ")
# for i in Str:
#     for j in range(0,3):
#         print(f"{i} {j}")


# Q23. Compare Every Character
# Compare every character with every other character and label Same/Different.

# Test Case
# Input: `AB`

# Expected Output: A/A is Same; all other ordered pairs are Different.

# Str=input("enter the string: ")
# for i in Str:
#     for j in Str:
#         if(i==j):
#             print(f"{i}/{j} are same")
#         elif(i!=j):
#             print(f"{i}/{j} are different")


# Q24. Character Matching
# Compare every character of two strings and print equal pairs.

# Test Case
# Input: `ABC` and `BCD`

# Expected Output:
# B B
# C C

# Str1=input("Enter first string:")
# Str2=input("Enter the second string:")
# for i in Str1:
#     for j in Str2:
#         if(i==j):
#             print(i,j)


# Q25. Count Matching Characters
# Count equal character comparisons between two strings without using count().

# Test Case
# Input: `ABC` and `BCD`

# Expected Output:
# 2

# Str1=input("Enter first string:")
# Str2=input("Enter the second string:")
# count=0
# for i in Str1:
#     for j in Str2:
#         if(i==j):
#             count+=1
# print(count)


# Q26. Character Frequency Without count()
# For each character, count its occurrences using nested loops.

# Test Case
# Input: `BANANA`

# Expected Output:
# B = 1
# A = 3
# N = 2


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
#     x+=1
#     if(count>0):
#         print(f"{char} = {count}")


# Q27. Vowel-Consonant Classification
# Compare each character against AEIOUaeiou using a nested loop.

# Test Case
# Input: `AbC`

# Expected Output:
# A = Vowel
# b = Consonant
# C = Consonant

# Str=input("Enter a string: ").strip()
# for i in Str:
#     if(i.upper()>='A' and i.upper()<='Z'):
#         if i in 'aeiouAEIOU':
#             print(f"{i} = Vowel")
#         else:
#             print(f"{i} = consonant")
#     else:
#          print("Invalid Input")




# Q28. Common Characters
# Print characters occurring in both strings without using set().

# Test Case
# Input: `HELLO` and `WORLD`

# Expected Output: Common characters include L and O.


# Str1=input("Enter a string: ")
# Str2=input("Enter a string: ")
# x=0
# for i in Str1:
#     flag=False
#     y=0
#     for z in Str1:
#         if(i==z):
#             if(y<x):
#                 break
#             else:
#                 flag=True
#                 break
#         y+=1
#     for j in Str2:
#         if(i==j and flag):
#             print(f"{i} is a common word")
#     x+=1



# Q29. Character Pair Generator
# Print every ordered pair of characters.

# Test Case
# Input: `ABC`

# Expected Output:
# A A
# A B
# A C
# B A
# B B
# B C
# C A
# C B
# C C


# Str=input("Enter a string: ")
# for i in Str:
#     for j in Str:
#         print(i,j)



# Q30. Different Character Pairs
# Print ordered pairs whose positions are different.

# Test Case
# Input: `ABC`

# Expected Output: A B, A C, B A, B C, C A, C B.

# Str=input("Enter a string: ").strip()
# for i in Str:
#     for j in Str:
#         if(i!=j):
#             if(i==Str[-1] and j==Str[-2]):
#                 print(i,j,end=".")
#             else:
#                 print(i,j,end=", ")


# Q31. Same or Different Pair
# Print each character pair with Same/Different and the pair itself.

# Test Case
# Input: `AAB`

# Expected Output: Equal A/A is Same; all unequal pairs are Different.


# Str=input("enter the string: ")
# R=""
# for i in Str:
#     for j in Str:
#         if(i==j and j not in R):
#             R+=j
#             print(f"{i}/{j} are same")
#         elif(i!=j):
#             print(f"{i}/{j} are different")




# Q32. Vowel-Consonant Pair
# Print pairs where first character is vowel and second is consonant.

# Test Case
# Input: `ABEC`

# Expected Output: Pairs such as A-B, A-C, E-B, E-C.


# Str=input("Enter the string: ")

# for i in Str:
#     for j in Str:
#         if i in "AEIOUaeiou" and j not in "AEIOUaeiou":
#             print(i+j)



# Q33. Same Case Pair
# Print pairs whose two characters have the same case.

# Test Case
# Input: `AbCD`

# Expected Output: Uppercase-uppercase and lowercase-lowercase pairs only.




# Str=input("Enter the string: ")
# x=0
# for i in Str:
#     y=0
#     for j in Str:
#         if i==j:
#             continue
#         if (i >='a' and i<='z') and (j >='a' and j<='z'):
#             print(i+j)
#         if (i >='A' and i<='Z') and (j >='A' and j<='Z'):
#             print(i+j)
#         y+=1
#     x+=1



# Q34. ASCII Difference
# For every pair, print the pair and absolute ASCII difference.

# Test Case
# Input: `ABC`

# Expected Output: A B -> 1, A C -> 2, B C -> 1, with reverse pairs as well.

# Str=input("Enter the string: ")
# x=0
# for i in Str:
#     y=0
#     for j in Str:
#         if x==y:
#             continue
#         print(f"{i} - {j} = {abs(ord(i)-ord(j))}")
#         print(f"{j} - {i} = {abs(ord(j)-ord(i))}")
#         y+=1
#     x+=1



# Q35. ASCII Relationship
# Classify each pair as Increasing, Decreasing or Same by ASCII value.

# Test Case
# Input: `ABC`

# Expected Output: A→B Increasing, B→A Decreasing, A→A Same, etc.

# Str=input("Enter the string: ")
# for i in Str:
#     for j in Str:
#         diff=ord(i)-ord(j)
#         if(diff>0):
#             print(F"{i} -> {j} Increases")
#         elif(diff<0):
#             print(F"{i} -> {j} decreases")
#         else:
#             print(F"{i} -> {j} Same")


# Q36. Compare Words
# Split a sentence and print every word pair.

# Test Case
# Input: `I love Python code`

# Expected Output: All ordered word pairs.
        

# Sentence=input("Enter a sentence").split()
# x=0
# for i in Sentence:
#     y=0
#     for j in Sentence:
#         if x==y:
#             y+=1
#             continue
#         print(i,j)
#         y+=1
#     x+=1



# Q37. Same-Length Word Pairs
# Print pairs of words having equal length.

# Test Case
# Input: `I love Python code`

# Expected Output:
# love code

# l=[]
# Sentence=input("Enter a sentence").split()
# x=0
# for i in Sentence:
#     y=0
#     for j in Sentence:
#         if x==y:
#             y+=1
#             continue
#         if len(i)==len(j):
#             if(i not in l and j not in l):
#                 print(i,j)
#                 l.append(i)
#                 l.append(j)
#         y+=1
#     x+=1



# Q38. Common Starting Character
# Print word pairs whose first characters match.

# Test Case
# Input: `cat car dog`

# Expected Output:
# cat car



# L=[]
# Sentence=input("Enter a sentence: ").split()
# x=0
# for i in Sentence:
#     y=0
#     for j in Sentence:
#         if(x==y):
#             y+=1
#             continue
#         if(i[0]==j[0]):
#             if(i not in L and j not in L):
#                 print(i,j)
#                 L.append(i)
#                 L.append(j)
#         y+=1
#     x+=1


# Q39. Common Ending Character
# Print word pairs whose final characters match.

# Test Case
# Input: `cat bat dog`

# Expected Output:
# cat bat



# L=[]
# Sentence=input("Enter a sentence: ").split()
# x=0
# for i in Sentence:
#     y=0
#     for j in Sentence:
#         if(x==y):
#             y+=1
#             continue
#         if(i[len(i)-1]==j[len(j)-1]):
#             if(i not in L and j not in L):
#                 print(i,j)
#                 L.append(i)
#                 L.append(j)
#         y+=1
#     x+=1




# Q40. Word Character Match
# Print word pairs sharing at least one character; do not use set().

# Test Case
# Input: `apple pie orange`

# Expected Output: Matching word pairs.

# Sent=input("Enter a sentence: ").strip().split()
# for word in Sent:
#     flag=True
#     for words in Sent:
#         if(word==words):
#             continue
#         for char in word:
#             if char in words:
#                 print(word,words)
#                 break
        


# Q41. Word Length Difference
# Print each pair and absolute difference of their lengths.

# Test Case
# Input: `I love Python code`

# Expected Output: Every ordered pair with its length difference.

# Sentence=input("Enter a sentence: ").split()
# l=[]
# for i in Sentence:
#     for j in Sentence:
#         if i==j:
#             continue
#         if(list(i)+list(j) not in l):
#             print(f"{i} - {j} : {abs(len(i)-len(j))}")
#             l.append(list(j)+list(i))





# Q42. Longest and Shortest Word Pair
# Use nested loops to identify longest and shortest words without max/min.

# Test Case
# Input: `I love Python programming`

# Expected Output:
# Longest = programming
# Shortest = I


# small=""
# large=""
# Sent=input("Enter a string: ").split()
# x=0
# for i in Sent:
#     if(x==0):
#         small=i
#         large=i
#         x+=1
#         continue
#     if(len(i)>len(large)):
#         large=i
#     if(len(i)<len(small)):
#         small=i
#     x+=1
# print(f"The largest word is: {large} and the smallest word is: {small}")


# Q43. Growing Inner Loop
# For each i from 1 to N, run inner loop 1..i.

# Test Case
# Input: 4

# Expected Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



# Q44. Shrinking Inner Loop
# Decrease the inner-loop size each row.

# Test Case
# Input: 4

# Expected Output:
# 1 2 3 4
# 1 2 3
# 1 2
# 1



# n=int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



# Q45. Multiplication Triangle
# For row i, print i×1 through i×i.

# Test Case
# Input: 4

# Expected Output: Row 4 contains 4 8 12 16.

# N=int(input("Enter the number of rows: "))
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print()





# Q46. Conditional Dynamic Loop
# Run inner loop i times and print only even inner values.

# Test Case
# Input: 4

# Expected Output:
# 2
# 2
# 2 4
# 2 4 6

# n=int(input("enter the number of rows : "))
# for i in range(n):
#     x=2
#     if i==1:
#         print(x)
#         continue
#     for j in range(i+1):
#         print(x,end="")
#         x+=2
#     print()


# Q47. Dynamic Range Based on Input
# For i=0..N-1, run range(i).

# Test Case
# Input: 4

# Expected Output: i=0 produces no inner output; later rows show 0, then 0 1, then 0 1 2.

# n=int(input("enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(j,end="")
#     print()



# Q48. Reverse Dynamic Range
# For each i, print i down to 1.

# Test Case
# Input: 4

# Expected Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1


# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1,0,-1):
#         print(j,end="")
#     print()



# Q49. Factors of Every Number
# Print all factors of every number from 1 to N.

# Test Case
# Input: 6

# Expected Output:
# 1 -> 1
# 2 -> 1 2
# 3 -> 1 3
# 4 -> 1 2 4
# 5 -> 1 5
# 6 -> 1 2 3 6

# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i%j==0:
#             print(j,end="")
#     print()

# Q50. Perfect Number Detector
# Find perfect numbers up to N using divisor sums.

# Test Case
# Input: 30

# Expected Output:
# Perfect: 6, 28

# n=int(input("Enter the number: "))
# for i in range(1,n):
#     sum=0
#     for j in range(1,i):
#         if(i%j==0):
#             sum+=j
#     if sum==i:
#         print(i)


# Q51. Prime Numbers Using Nested Loops
# Find all primes from 2 to N.

# Test Case
# Input: 20

# Expected Output:
# 2 3 5 7 11 13 17 19



# n=int(input("Enter the range: "))
# for i in range(2,n):
#     if i==2:
#         print(i,end=" ")
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")



# Q52. Prime Factor Display
# For every prime up to N, display its factors.

# Test Case
# Input: 10

# Expected Output: 2->1,2; 3->1,3; 5->1,5; 7->1,7.


# n=int(input("Enter the range: "))
# for i in range(2,n):
#     if i==2:
#         print(1,2,sep=",",end="; ")
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(1,i,sep=",",end="; ")


# Q53. Common Factors
# Find common factors of A and B using nested loops.

# Test Case
# Input: A=12, B=18

# Expected Output:
# 1 2 3 6

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# x=b
# if(a<b):
#     x=a
# for i in range(1,x+1):
#     if a%i==0 and b%i==0:
#         print(i,end=" ")




# Q54. Common Multiples
# Generate multiples and print common multiples up to a limit.

# Test Case
# Input: A=6, B=8, limit=30

# Expected Output: No common multiple below 30 except 24.

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# limit=int(input("Enter the range: "))
# x=b
# if(a>b):
#     x=a
# for i in range(x,limit+1):
#     if(i%a==0 and i%b==0):
#         print(i)


# Q55. Pair With Greatest Product
# Generate all pairs from 1..N and find greatest product.

# Test Case
# Input: N=4

# Expected Output:
# Pair = 4,4
# Product = 16

# n=int(input("Enter a number: "))
# print(f"Pair = {n},{n}")
# print(f"Product = {n*n}")



# Q56. Pair With Target Sum
# Print all pairs from 1..N whose sum equals target.

# Test Case
# Input: N=5, target=7

# Expected Output:
# 2 5
# 3 4
# 4 3
# 5 2


# n=int(input("enter a number: "))
# target=int(input("enter the target: "))
# for i in range(1,n+1):
#     rem=target-i
#     for j in range(1,n+1):
#         if j==rem:
#             print(i,j,sep=" ")



# Q57. Right Triangle
# Print a right triangle of stars.

# Test Case
# Input: 4

# Expected Output:
# *
# **
# ***
# ****

# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()



# Q58. Number Triangle
# Print increasing number sequences.

# Test Case
# Input: 4

# Expected Output:
# 1
# 12
# 123
# 1234





# Q82
# Str1=input("Enter a string: ").lower().strip()
# Str2=input("Enter a string: ").lower().strip()
# count=0
# if len(Str1)==len(Str2):
#     for char in Str1:
#         if char in Str2:
#             count+=1
#     if(count==len(Str1)):
#         print("Anagram")
#     else:
#         print("Not Anagram")
# else:
#     print("Not anagram")

