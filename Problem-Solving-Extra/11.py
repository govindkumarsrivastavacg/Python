# 11. Leap Year
# Take a year.

# Determine whether it is a leap year.

yr=int(input("Enter the year: "))
if(yr%400==0):
    print("Leap year")
elif(yr%4==0 and yr%100!=0):
    print("Leap year")
else:
    print("Not leap year")