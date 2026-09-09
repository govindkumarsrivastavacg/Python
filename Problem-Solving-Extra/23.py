# 23. Login System
# Take:

# Username
# Password
# Assume:

# Username = admin
# Password = python123
# Print:

# Login successful
# Wrong password
# User not found
# Logic
# If username is wrong, print User not found.

# If username is correct but password is wrong, print Wrong password.

# If both are correct, print Login successful.

username=input("Enter username").strip()
password=input("Enter password").strip()
if(username!="admin"):
    print("User not found")
if(username=="admin" and password!="python123"):
    print("Wrong Password")
if(username=="admin" and password=="python123"):
    print("Login Successful")