# Q1. break at the Beginning

# Guess the output.

#     for i in range(1, 5):
#         if i == 1:
#             break
#         print(i)

#     print("End")

#     End


# Q2. break in the Middle

#     for i in range(1, 7):
#         print(i)
#         if i == 4:
#             break
#     print("Finished")


#     1
#     2
#     3
#     4
#     Finished


# Q3. continue Skips One Value

#     for i in range(1, 6):
#         if i == 3:
#             continue
#         print(i)


#     1
#     2
#     4
#     5


# Q4. pass Does Nothing

#     for i in range(1, 5):
#         if i == 2:
#             pass
#         print(i)


#     1
#     2
#     3
#     4


# Q5. A Loop with else

#     for i in range(3):
#         print("Python")
#     else:
#         print("Done")


#     Python
#     Python
#     Python
#     Done


# Q6. Print Before break

#     for i in range(1, 5):
#         print("A", i)
#         if i == 3:
#             break
#         print("B", i)


#     A 1
#     B 1
#     A 2
#     B 2
#     A 3


# Q7. print() After continue

#     for i in range(1, 5):
#         if i == 2:
#             continue
#         print("Value:", i)
#         print("Next line")


#     Value: 1
#     Next line
#     Value: 3
#     Next line
#     Value: 4
#     Next line


# Q8. pass Before print()

#     for i in range(1, 4):
#         if i == 2:
#             pass
#             print("Inside if")
#         print("Outside if", i)


#     Outside if 1
#     Inside if
#     Outside if 2
#     Outside if 3


# Q9. break and Code Outside the Loop

#     for i in range(2, 8, 2):
#         print(i)
#         if i == 4:
#             break
#         print("Hello")

#     print("After loop")


#     2
#     Hello
#     4
#     After loop


# Q10. continue and Multiple Prints

#     for i in range(1, 5):
#         print("Start", i)
#         if i == 3:
#             continue
#         print("End", i)


#     Start 1
#     End 1
#     Start 2
#     End 2
#     Start 3
#     Start 4
#     End 4


# Q11. Normal Completion

#     for i in range(2, 5):
#         print(i)
#     else:
#         print("Loop completed")


#     2
#     3
#     4
#     Loop completed


# Q12. break Prevents Loop else

#     for i in range(1, 6):
#         if i == 4:
#             break
#         print(i)
#     else:
#         print("Completed")
#     print("Program end")


#     1
#     2
#     3
#     Program end


# Q13. continue Does Not Prevent Loop else

#     for i in range(1, 5):
#         if i % 2 == 0:
#             continue
#         print(i)
#     else:
#         print("Completed")

#     1
#     3
#     Completed


# Q14. Empty Sequence

#     for i in range(5, 5):
#         print(i)
#     else:
#         print("Else executed")

#     Else executed


# Q15. break After Some Iterations

#     for letter in "CODE":
#         print(letter)
#         if letter == "D":
#             break
#     else:
#         print("All letters checked")

#     C
#     O
#     D


# Q16. pass with for-else

#     for i in range(1, 4):
#         if i == 2:
#             pass
#         print(i)
#     else:
#         print("Finished normally")


#     1
#     2
#     3
#     Finished normally


# Q17. Search for a Character

#     word = "banana"

#     for ch in word:
#         if ch == "n":
#             print("Found")
#             break
#     else:
#         print("Not found")


#     Found


# Q18. Search Fails

#     word = "apple"

#     for ch in word:
#         if ch == "z":
#             print("Found")
#             break
#     else:
#         print("Not found")


#     Not found


# Q19. Skip Vowels

#     for ch in "education":
#         if ch in "aeiou":
#             continue
#         print(ch, end="")
#     print()

#     dctn


# Q20. Stop at a Particular Character

#     for ch in "programming":
#         if ch == "g":
#             break
#         print(ch, end="-")


#     p-r-o-


# Q21. Skip and Then Stop

#     for ch in "computer":
#         if ch == "o":
#             continue
#         if ch == "t":
#             break
#         print(ch, end="")


#     cmpu


# Q22. pass Inside a String Loop

#     for ch in "cat":
#         if ch == "a":
#             pass
#         print(ch.upper(), end=" ")


#     C A T 


# Q23. break in a while Loop

#     n = 1

#     while n <= 5:
#         print(n)
#         if n == 3:
#             break
#         n += 1

#     print("Stopped")


#     1
#     2
#     3
#     Stopped


# Q24. continue in a while Loop

#     n = 0

#     while n < 5:
#         n += 1
#         if n == 3:
#             continue
#         print(n)


#     1
#     2
#     4
#     5


# Q25. continue After Updating the Variable

#     n = 1

#     while n <= 5:
#         if n == 2:
#             n += 1
#             continue
#         print(n)
#         n += 1


#     1
#     3
#     4
#     5


# Q26. break Before Updating the Variable

#     n = 1

#     while n <= 4:
#         if n == 3:
#             break
#         print(n)
#         n += 1

#     print(n)

#     1
#     2
#     3


# Q27. break in the Inner Loop

#     for row in range(1, 4):
#         for col in range(1, 5):
#             if col == 3:
#                 break
#             print(row, col)


#     1 1
#     1 2
#     2 1
#     2 2
#     3 1
#     3 2


# Q28. continue in the Inner Loop

#     for row in range(1, 3):
#         for col in range(1, 4):
#             if col == 2:
#                 continue
#             print(row, col)


#     1 1
#     1 3
#     2 1
#     2 3


# Q29. break Does Not Stop the Outer Loop

#     for i in range(1, 4):
#         print("Outer", i)
#         for j in range(1, 4):
#             if j == 2:
#                 break
#             print("Inner", j)


#     Outer 1
#     Inner 1
#     Outer 2
#     Inner 1
#     Outer 3
#     Inner 1


# Q30. Inner Loop else

#     for i in range(1, 4):
#         for j in range(1, 4):
#             if j == 2:
#                 break
#             print(i, j)
#         else:
#             print("Inner else", i)

#     1 1
#     2 1
#     3 1


# Q31. continue with Inner Loop else

#     for i in range(1, 3):
#         for j in range(1, 4):
#             if j == 2:
#                 continue
#             print(i, j)
#         else:
#             print("Inner loop complete")


#     1 1
#     1 3
#     Inner loop complete
#     2 1
#     2 3
#     Inner loop complete


# Q32. continue, break, and for-else

#     for i in range(1, 7):
#         if i == 2:
#             continue
#         if i == 5:
#             break
#         print(i)
#     else:
#         print("Loop else")
#     print("End")


#     1
#     3
#     4
#     End


# Q33. pass Does Not Skip the Next Statement

#     for i in range(1, 5):
#         if i == 3:
#             pass
#         else:
#             print("Else block", i)
#         print("Number", i)


#     Else block 1
#     Number 1
#     Else block 2
#     Number 2
#     Number 3
#     Else block 4
#     Number 4


# Q34. Two print() Statements Around continue

#     for i in range(1, 5):
#         print("X", end="")
#         if i == 2:
#             continue
#         print("Y", end="")
#     print("Z")


#     XYXXYXXYZ


# Q35. Predict Carefully

#     for i in range(1, 5):
#         if i == 2:
#             pass
#         elif i == 3:
#             continue
#         elif i == 4:
#             break
#         print(i)
#     else:
#         print("Completed")
#     print("Outside")


#     1
#     2
#     Outside
