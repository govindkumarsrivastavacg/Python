# Divisible by 5 and 11
# Take a number.

# Check whether it is:

# Divisible by both 5 and 11
# Divisible only by 5
# Divisible only by 11
# Divisible by neither

num=int(input("Enter a number: "))
if(num%5==0 or num%11==0):
    if(num%5!=0):
        print("Divisible by just 11")
    elif(num%11!=0):
        print("Divisible ny just 5")
    else:
        print("Divisible by both 5 and 11")
else:
    print("Divisible by neither 5 or 11")