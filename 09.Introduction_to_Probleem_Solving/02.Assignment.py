# Problem 1
# Take two numbers and print their sum.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
print(f"The sum of the two numbers is:: {sum}")


# Problem 2
# Take a number and print whether it is even or odd.
num=int(input("Enter number: "))
if(num%2==0):
    print("Number is odd")
else:
    print("Number is even")


# Problem 3
# Take three numbers and print the largest number.

n1,n2,n3=map(int,input("Enter the numbers: ").split())
if(n1>n2 and n1>n3):
    print(f"{n1} is the largest of the three")
elif(n2>n1 and n2>n3):
    print(f"{n2} is the largest of the three")
elif(n3>n1 and n3>n2):
    print(f"{n3} is the largest of the three")
else:
    print("Atleast 2 values are equal and largest")


# Problem 4
# Take a person's age and print whether they are eligible to vote. Assume the minimum age is 18.

age=int(input("Enter the age: "))
if(age>=18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Problem 5
# Take the price of an item. Give a 20% discount when the price is greater than or equal to 2000. Print the final price.

price=int(input("Enter price: "))
dis=price*(20/100)
if(price>=2000):
    print(f"The total price is: {price-dis}")
else:
    print(f"The total price is: {price}")


# Problem 6
# Take three subject marks and calculate the average. Print Pass if the average is at least 40; otherwise print Fail.

m1,m2,m3=map(int,input("Enter the marks:").split())
avg=(m1+m2+m3)/3
if(avg>=40):
    print("Pass")
else:
    print("Fail")