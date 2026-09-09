# 10. Voting Eligibility
# Take age from the user.

# Rules:

# Age below 0 → Invalid age
# Age below 18 → Cannot vote
# Age 18 or above → Can vote
# Bonus
# Also reject an unrealistic age above 120.

age=int(input("Enter the numbers: "))
if(age>=18):
    print("Can vote")
elif(age<0):
    print("Invalid age")
else:
    print("Cannot vote")