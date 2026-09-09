# Divisible by Either 3 or 7
# Take a number.

# Print:

# Divisible by both 3 and 7
# Divisible only by 3
# Divisible only by 7
# Divisible by neither

num=int(input("Enter a number: "))
if(num%3==0 or num%7==0):
    if(num%3!=0):
        print("Divisible by just 7")
    elif(num%7!=0):
        print("Divisible ny just 3")
    else:
        print("Divisible by both 3 and 7")
else:
    print("Divisible by neither 3 or 7")