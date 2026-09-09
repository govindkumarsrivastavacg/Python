num=int(input("Enter a number: "))
if(num<0):
    print("Number is Negative")
if(num<=10):
    print("Number is in range 0-10")
elif(num<=50):
    print("Number is in range 11-50")
elif(num<=100):
    print("Number is in range 51-100")
else:
    print("Number is above 100")