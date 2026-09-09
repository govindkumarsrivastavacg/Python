# 30. Complete Scholarship Decision ⭐
# Take:

# Student age
# Marks
# Family income
# Attendance percentage
# Scholarship requirements:

# Age:             18–25
# Marks:           85 or above
# Attendance:      75% or above
# Family income:   ₹300000 or below
# The student gets the scholarship only when all conditions are satisfied.

age=int(input("Enter student's age: "))
marks=int(input("Enter marks"))
atten=int(input("Enter the attendance: "))
fam_inc=int(input("Enter family income: "))
if((age>=18 and age<=25) and  (marks>=85 and marks<=100) and (atten>=75 and atten<=100) and (fam_inc<=300000)):
    print("Eligible for scholarship")
else:
    print("Ineligible for scholarship")
    if((age>=18 and age<=25)==False):
        print("Age condition failed")
    if((marks>=85 and marks<=100)==False):
        print("Marks condition failed")
    if((atten>=75 and atten<=100)==False):
        print("Attendance condition failed")
    if((fam_inc<=300000)==False):
        print("Family income condition failed")
