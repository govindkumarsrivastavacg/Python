# Even or Odd + Positive or Negative
# Take a number.

# Print whether the number is:

# Positive Even
# Positive Odd
# Negative Even
# Negative Odd
# Zero

num=int(input("Enter a number : "))
if(num==0):
    print("Zero")
elif(num>0):
    if(num%2==0):
        print("Positive even")
    else:
        print("Positive odd")
else:
    if(num%2==0):
        print("Negative even")
    else:
        print("Negative odd")