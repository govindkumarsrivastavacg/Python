# 26. Date Validator
# Take:

# Day
# Month
# Year
# Determine whether the date is valid.

date,month,yr=map(int,input("Enter a value\n Use numbers from 1 to 12 for months").split())
if month in (1, 3, 5, 7, 8, 10, 12):
    if(date<=31 and date>0):
        print(f"Valid date{date}/{month}/{yr}")
elif(month==2):
    if(yr%400==0 or(yr%4==0 and yr%100!=0)):
        if(date>0 and date<=29):
            print(f"Valid date{date}/{month}/{yr}")
    else:
        if(date>0 and date<=28):
            print(f"Valid date{date}/{month}/{yr}")
elif month==4 or month==6 or month ==9 or month==11:
    if(date<=30 and date>0):
            print(f"Valid date{date}/{month}/{yr}")
else:
    print("Invalid date")
