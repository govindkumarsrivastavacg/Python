# 25. Student Result System
# Take marks for three subjects.

# Rules:

# Every subject must have marks between 0 and 100.
# Every subject must have at least 35 marks to pass.
# If any subject is below 35 → Fail
# Otherwise calculate average.
# Grade based on average:

# 75 or above → Distinction
# 60–74       → First Class
# 50–59       → Second Class
# 35–49       → Pass
# Important
# Student must pass every subject.

sub1,sub2,sub3=map(int,input("Enter the marks: ").split())
avg=(sub1+sub2+sub3)/3
if(sub1 and sub2 and sub3>=0):
    if(sub1 and sub2 and sub3>=35):
        if(avg>=75):
            print("Distinction")
        elif(avg>=60):
            print("First Class")
        elif(avg>=50):
            print("Second Class")
        elif(avg>=35):
            print("Third Class")
    else:
        print("Fail")
        