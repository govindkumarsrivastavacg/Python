# Largest of Three Numbers
# Take three numbers and find the largest.

a,b,c=map(int,input("Enter the numbers: ").split())
if(a>b and a>c):
    print(f"{a} is the Largest")
if(b>a and b>c):
    print(f"{b} is the Largest")
elif(c>a and c>b):
    print(f"{c} is the Largest")
else:
    print("Atleast two values are the largest and equal")