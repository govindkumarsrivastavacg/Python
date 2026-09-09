# Pass or Fail
# Take marks from the user.

# Rules:

# Marks below 0 → Invalid marks
# Marks above 100 → Invalid marks
# Marks 40 or above → Pass
# Marks below 40 → Fail

marks=int(input("Enter a number: "))
if(marks<0 or marks>100):
    print("Invalid marks")
elif(marks>=40):
    print("Pass")
else:
    print("Fail")