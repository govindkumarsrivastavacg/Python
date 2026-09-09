# 28. Youngest of Three People
# Take the name and age of three people.

# Find the youngest person.
name1=input("Enter first name: ")
name2=input("Enter second name: ")
name3=input("Enter third ")
age1,age2,age3=map(int,input("Enter the ages of 3 people: ").split())
if(age1>=0 and age2>=0 and age3>=0):
    if(age1<age2 and age1<age3):
        print(f"{name1} is the youngest")
    elif(age2<age1 and age2<age3):
        print(f"{name2} is the youngest")
    elif(age3<age2 and age3<age1):
        print(f"{name1} is the youngest")
    elif(age1==age2==age3):
        print("All are of same age")
    else:
        print("Atleast two people are of the same age and youngest")
else:
    print("Invalid age")
