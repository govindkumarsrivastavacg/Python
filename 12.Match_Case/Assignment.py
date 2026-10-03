# # Q1. Food Ordering System
# # A restaurant has the following menu:

# # 1 → Pizza
# # 2 → Burger
# # 3 → Pasta
# # 4 → Sandwich
# # Write a program that takes the customer's choice and displays the selected food.

# # If the customer enters any other number, display:

# # Invalid Menu Choice

# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Pizza")
# #     case 2:
# #         print("Burger")
# #     case 3:
# #         print("Pasta")
# #     case 4:
# #         print("Sandwich")
# #     case _:
# #         print("Invalid Menu Choice")


# # Q2. Mobile Settings
# # Create a simple mobile settings menu:

# # 1 → Wi-Fi
# # 2 → Bluetooth
# # 3 → Mobile Data
# # 4 → Airplane Mode
# # 5 → Exit
# # Take the user's choice and display the selected setting.

# # For an invalid choice, display:

# # Invalid Setting


# # settings=int(input("Enter your choice: "))
# # match settings:
# #     case 1:
# #         print("Wi-Fi Selected")
# #     case 2:
# #         print("Bluetooth selected")
# #     case 3:
# #         print("Mobile Data selected")
# #     case 4:
# #         print("Airplane Mode selected")
# #     case 5:
# #         print("Exit")
# #     case _:
# #         print("Invaid choice")


# # Q3. ATM Main Menu
# # Create an ATM menu:

# # 1 → Check Balance
# # 2 → Withdraw Money
# # 3 → Deposit Money
# # 4 → Change PIN
# # 5 → Exit
# # Take the user's choice and display the corresponding message.

# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Check Balance selected")
# #     case 2:
# #         print("Withdraw Money selected")
# #     case 3:
# #         print("Deposit money selected")
# #     case 4:
# #         print(("Change pin selected"))
# #     case 5:
# #         print("Exit")


# # Q4. Traffic Signal
# # Take a traffic signal color as input:

# # red
# # yellow
# # green
# # Use match-case to display:

# # red    → Stop
# # yellow → Wait
# # green  → Go
# # For any other color:

# # Invalid Signal


# # signal=input("Enter the signal: ").strip().lower()
# # match signal:
# #     case "red":
# #         print("Stop")
# #     case "yellow":
# #         print("Wait")
# #     case "green":
# #         print("Go")
# #     case _:
# #         print("Invalid signal")


# # Q5. Student Portal
# # Create a student portal menu:

# # 1 → View Profile
# # 2 → View Courses
# # 3 → View Marks
# # 4 → View Attendance
# # 5 → Logout
# # Take the user's choice and display an appropriate message.

# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("View Profile selected")
# #     case 2:
# #         print("View courses selected")
# #     case 3:
# #         print("View marks selected")
# #     case 4:
# #         print("View attandance selected")
# #     case 5:
# #         print("Logout selected")
# #     case _:
# #         print("Invalid choice")


# # Q6. Online Shopping Menu
# # Create an online shopping menu:

# # 1 → Electronics
# # 2 → Clothing
# # 3 → Books
# # 4 → Grocery
# # 5 → Exit
# # Display the selected category.


# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Opening Electronics")
# #     case 2:
# #         print("Opening Clothing")
# #     case 3:
# #         print("Opening Books")
# #     case 4:
# #         print("Opening Grocery")
# #     case 5:
# #         print("Exit")
# #     case _:
# #         print("Invalid choice")


# # Q7. Banking Service Selection
# # A banking application provides:

# # 1 → Account Balance
# # 2 → Mini Statement
# # 3 → Fund Transfer
# # 4 → Bill Payment
# # 5 → Customer Support
# # Write a program using match-case to display the selected service.



# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Opening Account balance")
# #     case 2:
# #         print("Opening Mini Statement")
# #     case 3:
# #         print("Opening Fund Transfer")
# #     case 4:
# #         print("Opening Payment")
# #     case 5:
# #         print("Opening Customer Support")
# #     case _:
# #         print("Invalid choice")


# # Q8. Movie Ticket Booking
# # Create a movie booking menu:

# # 1 → Morning Show
# # 2 → Afternoon Show
# # 3 → Evening Show
# # 4 → Night Show
# # Display the selected show.


# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Morning Show selected")
# #     case 2:
# #         print("Afternoon Show selected")
# #     case 3:
# #         print("Evening Show selected")
# #     case 4:
# #         print("Night Show selected")
# #     case _:
# #         print("Invalid choice")

# # Q9. Weather Advice
# # Take the weather condition as input:

# # sunny
# # rainy
# # cloudy
# # snowy
# # Display appropriate advice:

# # sunny  → Wear sunglasses
# # rainy  → Carry an umbrella
# # cloudy → Weather may change
# # snowy  → Wear warm clothes
# # For any other input:

# # Unknown Weather


# # weather=input("Enter the weather").strip().lower()
# # match weather:
# #     case "sunny":
# #         print("Wear Sunglasses")
# #     case "rainy":
# #         print("Carry an umbrella")
# #     case "cloudy":
# #         print("Weather may change")
# #     case "snowy":
# #         print("Wear warm clothes")
# #     case _:
# #         print("Unknown weather")


# # Q10. Payment Method
# # An online store accepts:

# # upi
# # card
# # cash
# # wallet
# # Display the selected payment method.


# # pay=input("Enter payment method: ").strip().lower()
# # match pay:
# #     case "upi":
# #         print("UPI method selected")
# #     case "card":
# #         print("Card method selected")
# #     case "wallet":
# #         print('Wallet method selected')
# #     case "cash":
# #         print("cash method selected")
# #     case _:
# #         print("Invalid payment method")


# # Q11. File Type Detector
# # Take a file extension as input:

# # pdf
# # jpg
# # png
# # mp3
# # mp4
# # Display the type of file.

# # Example:

# # pdf → Document
# # jpg → Image
# # png → Image
# # mp3 → Audio
# # mp4 → Video

# # choice=input("Enter extension: ").strip.lower()
# # match choice:
# #     case "pdf":
# #         print("Document file")
# #     case "jpg":
# #         print("image")
# #     case "png":
# #         print("image")
# #     case "mp3":
# #         print("Audio file")
# #     case "mp4":
# #         print("Video file")
# #     case _:
# #         print("Invalid extension")


# # Q12. User Role
# # A system supports these roles:

# # admin
# # teacher
# # student
# # guest
# # Display the appropriate access message.

# # Example:

# # admin   → Full Access
# # teacher → Teacher Dashboard
# # student → Student Dashboard
# # guest   → Limited Access
# # For an unknown role:

# # Invalid Role


# # choice=input("Enter role: ").strip.lower()

# # match choice:
# #     case "admin":
# #         print("Full access")
# #     case "teacher":
# #         print("Teacher Dashboard")
# #     case "student":
# #         print("Student Dashboard")
# #     case "guest":
# #         print("Limited access")
# #     case _:
# #         print("Unknown role")



# # Q13. Weekday or Weekend
# # Take a day number:

# # 1 → Monday
# # 2 → Tuesday
# # 3 → Wednesday
# # 4 → Thursday
# # 5 → Friday
# # 6 → Saturday
# # 7 → Sunday
# # Use match-case and | to display:

# # Weekday
# # for Monday to Friday and:

# # Weekend
# # for Saturday and Sunday.

# # For any other number:

# # Invalid Day


# # day=int(input("Enter the day"))
# # match day:
# #     case 1|2|3|4|5:
# #         print("Weekday")
# #     case 6|7:
# #         print("Weekend")
# #     case _:
# #         print("Invalid day")


# # Q14. Customer Support Priority
# # A support system receives priority numbers:

# # 1 → Low
# # 2 → Medium
# # 3 → High
# # 4 → Critical
# # Treat priorities 1 and 2 as:

# # Normal Priority
# # Treat priorities 3 and 4 as:

# # Urgent Priority
# # Use | where appropriate.


# # prio=int(input("Enter The priority: "))
# # match prio:
# #     case 1|2:
# #         print("Normal priority")
# #     case 3|4:
# #         print("Urgent priority")
# #     case _:
# #         print("Invalid input")




# # Q15. Store Discount Category
# # A store uses membership levels:

# # 1 → Bronze
# # 2 → Silver
# # 3 → Gold
# # 4 → Platinum
# # Group the levels:

# # 1, 2 → Basic Membership
# # 3, 4 → Premium Membership
# # Display the appropriate category.

# # choice=int(input("enter choice: "))
# # match choice:
# #     case 1|2:
# #         print("Basic Membership")
# #     case 3|4:
# #         print("Premium Membership")
# #     case _:
# #         print("Invalid input")


# # Q16. University Portal
# # Create a university portal.

# # First ask the user to select:

# # 1 → Student
# # 2 → Teacher
# # If the user selects Student, show:

# # 1 → View Courses
# # 2 → View Marks
# # 3 → View Attendance
# # If the user selects Teacher, show:

# # 1 → View Students
# # 2 → Enter Marks
# # 3 → View Attendance
# # Use nested match-case.

# # role=int(input("Enter your role: "))
# # match role:
# #     case 1:
# #         print("Opening student section")
# #         choice=int(input("Enter your choice: "))
       
# #         match choice:
# #             case 1:
# #                 print("View COurses")
# #             case 2:
# #                 print("View Marks")
# #             case 3:
# #                 print("View attendance")
# #     case 2:
# #         print("Opening Teachers section")
# #         choice=int(input("Enter your choice"))
        
# #         match choice:
# #             case 1:
# #                 print("View Students")
# #             case 2:
# #                 print("View marks")
# #             case 3:
# #                 print("View attendance")
# #     case _:
# #         print("Invalid input")


# # Q17. ATM with Account Type

# # First ask for account type:

# # 1 → Savings
# # 2 → Current
# # Then show:

# # 1 → Check Balance
# # 2 → Deposit
# # 3 → Withdraw
# # Use nested match-case to display the selected account and operation.

# # account=int(input("Enter the type of account: "))
# # match account:
# #     case 1:
# #         print("Opening Savings Account")
# #         choice=int(input("Enter the action you want to perform: "))
# #         match choice:
# #             case 1:
# #                 print("Check balance selected")
# #             case 2:
# #                 print("Deposite selected")
# #             case 3:
# #                 print("Withdraw selected")
# #     case 2:
# #         print("Opening Current Account")
# #         choice=int(input("Enter the action you want to perform: "))
# #         match choice:
# #             case 1:
# #                 print("Check balance selected")
# #             case 2:
# #                 print("Deposite selected")
# #             case 3:
# #                 print("Withdraw selected")
# #     case _:
# #         print("Invalid input")




# # Q18. E-Commerce Application
# # First ask for a category:

# # 1 → Electronics
# # 2 → Clothing
# # For Electronics:

# # 1 → Mobile
# # 2 → Laptop
# # 3 → Headphones
# # For Clothing:

# # 1 → Shirt
# # 2 → Jeans
# # 3 → Shoes
# # Use nested match-case.


# # cat=int(input("Enter the category: "))
# # match cat:
# #     case 1:
# #         print("Opening Electronics section")
# #         choice=int(input("Enter the action you want to perform: "))
# #         match choice:
# #             case 1:
# #                 print("Mobile selected")
# #             case 2:
# #                 print("Laptop selected")
# #             case 3:
# #                 print("Headphone selected")
# #     case 2:
# #         print("Opening Clothing")
# #         choice=int(input("Enter the action you want to perform: "))
# #         match choice:
# #             case 1:
# #                 print("Shirt selected")
# #             case 2:
# #                 print("Jeans selected")
# #             case 3:
# #                 print("Shoes selected")
# #     case _:
# #         print("Invalid input")



# # Q19. Food Delivery Application
# # First ask:

# # 1 → Vegetarian
# # 2 → Non-Vegetarian
# # If Vegetarian:

# # 1 → Paneer
# # 2 → Dal
# # 3 → Veg Biryani
# # If Non-Vegetarian:

# # 1 → Chicken Biryani
# # 2 → Chicken Curry
# # 3 → Fish Fry
# # Use nested match-case.


# # food=int(input("Enter the food: "))
# # match food:
# #     case 1:
# #         print("Opening Vegetarian section")
# #         choice=int(input("Enter the action you want to perform: "))
# #         match choice:
# #             case 1:
# #                 print("Paneer selected")
# #             case 2:
# #                 print("Dal selected")
# #             case 3:
# #                 print("Veg Biryani selected")
# #     case 2:
# #         print("Opening Nonvegetarian Section")
# #         choice=int(input("Enter the action you want to perform: "))
# #         match choice:
# #             case 1:
# #                 print("Chicken Biryani selected")
# #             case 2:
# #                 print("Chicken Curry selected")
# #             case 3:
# #                 print("Fish selected")
# #     case _:
# #         print("Invalid input")



# # Q20. Simple Calculator
# # Take two numbers and an operator:

# # +
# # -
# # *
# # /
# # Use match-case to perform the selected operation.


# # a,b=map(int,input("Enter the numbers: ").split())
# # choice=input("Enter the operation you want to perform: ").strip().lower()
# # match choice:
# #     case "add":
# #         print(f"The result is {a+b}")
# #     case "subtract":
# #         print(f"The result is {a-b}")
# #     case "multiply":
# #         print(f"The result is {a*b}")
# #     case "divide":
# #         print(f"The result is {a/b}")
# #     case _:
# #         print("Invalid operation")



# choice=int(input("Enter the conversion you want to perform: "))
# match choice:
#     case 1:
#         temp=int(input("Enter temperature in celcius: "))
#         temp=temp*(9/5)+32
#         print("The temperature in farenheit is: ",temp)

#     case 2:
#         temp=int(input("Enter temperature in farenheit: "))
#         temp=(temp-32)*(5/9)
#         print("The temperature in celcius is: ",temp)
#     case _:
#         print("Enter a valid value: ")



# # Q22. Unit Converter
# # Create a unit conversion menu:

# # 1 → Kilometers to Meters
# # 2 → Meters to Kilometers
# # 3 → Kilograms to Grams
# # 4 → Grams to Kilograms
# # Take the required value and perform the selected conversion.


# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         a=int(input("Enter the distance in kms: "))
# #         a=a*1000
# #         print(f"The distance in m is {a}")
# #     case 2:
# #         a=int(input("Enter the distance in m: "))
# #         a=a/1000
# #         print(f"The distance in kms is {a}")
# #     case 1:
# #         a=int(input("Enter the weight in kgs: "))
# #         a=a*1000
# #         print(f"The weight in gms is {a}")
# #     case 2:
# #         a=int(input("Enter the weight in gms: "))
# #         a=a/1000
# #         print(f"The weight in kgs is {a}")
# #     case _:
# #         print("Invalid input")



# # Q23. ATM Withdrawal
# # Create an ATM withdrawal program.

# # First use match-case for:

# # 1 → Savings
# # 2 → Current
# # For either account, ask for withdrawal amount.

# # Use if to check:

# # If amount is positive, continue.
# # If amount is zero or negative, display Invalid Amount.



# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         print("Opening savings account")
# #         a=int(input("Enter the Withdrawal amount: "))
# #         if(a>0):
# #             print(f"Withdrawal successfull")
# #         else:
# #             print("Invalid amount")
# #     case 2:
# #         print("Openings Current account")
# #         a=int(input("Enter the Withdrawal amount: "))
# #         if(a>0):
# #             print(f"Withdrawal successfull")
# #         else:
# #             print("Invalid amount")
# #     case _:
# #         print("Invalid input")


# # Q24. Online Exam Portal
# # Create a menu:

# # 1 → Start Exam
# # 2 → View Result
# # 3 → Exit
# # If the user selects Start Exam, ask for age.

# # Use if to check whether the student is at least 18 years old.


# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         print("Start exam selected")
# #         a=int(input("Enter the age: "))
# #         if(a>18):
# #             print(f"Eligible for exam")
# #         else:
# #             print("Inelligible for exam")
# #     case 2:
# #         print("View result selected")
# #         print("Your result is A+")
# #     case _:
# #         print("Exit selected")



# # Q25. Movie Ticket System
# # Create a movie ticket menu:

# # 1 → Regular
# # 2 → Premium
# # 3 → VIP
# # Ask for the customer's age after selecting the ticket type.

# # If age is below 5, display:

# # Free Entry
# # Otherwise display the selected ticket type.

# # Use match-case for ticket selection and if for the age condition

# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         a=int(input("Enter the age: "))
# #         if(a<5):
# #             print(f"Free entry")
# #         else:
# #             print("Regular ticket")
# #     case 2:
# #         a=int(input("Enter the age: "))
# #         if(a<5):
# #             print(f"Free entry")
# #         else:
# #             print("Premium ticket")
# #     case 3:
# #             a=int(input("Enter the age: "))
# #             if(a<5):
# #                 print(f"Free entry")
# #             else:
# #                 print("Vip ticket")
# #     case _:
# #         print("You dont have a ticket")



# # Q26. Smart Home Controller
# # Create a smart home controller:

# # 1 → Light
# # 2 → Fan
# # 3 → AC
# # 4 → TV
# # For each device, display an appropriate message.

# # Example:

# # Enter device: 3

# # AC Controller Opened

# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         print("Fan controller opened")
# #     case 2:
# #         print("Light controller opened")
# #     case 3:
# #         print("AC contoller opened")
# #     case 4:
# #         print("TV controller opened")
# #     case _:
# #         print("Invalid input")


# # Q27. Hospital Department Selection
# # Create a hospital department menu:

# # 1 → General Medicine
# # 2 → Cardiology
# # 3 → Orthopedics
# # 4 → Pediatrics
# # 5 → Emergency
# # Display the selected department.

# # For invalid input, display:

# # Invalid Department

# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         print("General Medicine Department")
# #     case 2:
# #         print("Cardiology Department")
# #     case 3:
# #         print("Orthopedics Department")
# #     case 4:
# #         print("pediatrics Department")
# #     case 5:
# #         print("Emergency Department")
# #     case _:
# #         print("Invalid input")


# # Q28. Railway Ticket System
# # Create a railway ticket menu:

# # 1 → Book Ticket
# # 2 → Cancel Ticket
# # 3 → Check PNR
# # 4 → Train Schedule
# # 5 → Exit
# # Display the appropriate action.


# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         print("Book ticket selected")
# #     case 2:
# #         print("Cancel ticket selected")
# #     case 3:
# #         print("Check PNR selected")
# #     case 4:
# #         print("Train schedule selected")
# #     case 5:
# #         print("Exit selected")
# #     case _:
# #         print("Invalid input")


# # Q29. Library Management System
# # Create a library menu:

# # 1 → Search Book
# # 2 → Issue Book
# # 3 → Return Book
# # 4 → View Issued Books
# # 5 → Exit
# # Use match-case to process the user's choice.


# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         print("Search book selected")
# #     case 2:
# #         print("Issue book selected")
# #     case 3:
# #         print("Return Book selected")
# #     case 4:
# #         print("View issued books selected")
# #     case 5:
# #         print("Exit selected")
# #     case _:
# #         print("Invalid input")


# # Q30. Food Delivery Order Status
# # Take an order status:

# # placed
# # confirmed
# # preparing
# # out_for_delivery
# # delivered
# # cancelled
# # Display a suitable message for each status.

# # Example:

# # Enter status: out_for_delivery



# # choice=int(input("Enter the conversion you want to perform: "))
# # match choice:
# #     case 1:
# #         print("Order placed")
# #     case 2:
# #         print("Order confirmed")
# #     case 3:
# #         print("preparing Order")
# #     case 4:
# #         print("Order out_for_delivery")
# #     case 5:
# #         print("Order delivered")
# #     case 6:
# #         print("Order Cancelled")
# #     case _:
# #         print("Invalid input")

# # Q31. Banking Application with Nested Menu
# # Create a banking application.

# # Main menu:

# # 1 → Personal Banking
# # 2 → Business Banking
# # Personal Banking:

# # 1 → Balance
# # 2 → Transfer
# # 3 → Loan
# # Business Banking:

# # 1 → Balance
# # 2 → Payroll
# # 3 → Business Loan
# # Use nested match-case.

# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Personal Banking selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Balance")
# #             case 2:
# #                 print("Transfer")
# #             case 3:
# #                 print("Loan")
# #     case 2:
# #         print("Business Banking selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Balance")
# #             case 2:
# #                 print("Payroll")
# #             case 3:
# #                 print("Business loan")
# #     case _:
# #         print("Invalid input")




# # Q32. School Management System
# # Create a school management system.

# # First select:

# # 1 → Student
# # 2 → Teacher
# # 3 → Parent
# # Student options:

# # 1 → Marks
# # 2 → Attendance
# # 3 → Homework
# # Teacher options:

# # 1 → Enter Marks
# # 2 → Attendance
# # 3 → Assign Homework
# # Parent options:

# # 1 → Child Marks
# # 2 → Child Attendance
# # 3 → Contact Teacher
# # Use nested match-case.



# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Student options selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Marks")
# #             case 2:
# #                 print("Attendance")
# #             case 3:
# #                 print("Homework")
# #     case 2:
# #         print("Teacher options selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Enter marks")
# #             case 2:
# #                 print("Attendance")
# #             case 3:
# #                 print("Assign homework")
# #     case 3:
# #             print("Parent option selected")
# #             a=int(input("Enter your choice: "))
# #             match a:
# #                 case 1:
# #                     print("Child marks")
# #                 case 2:
# #                     print("Child attendance")
# #                 case 3:
# #                     print("Contact teacher")
# #     case _:
# #         print("Invalid input")




# # Q33. Travel Booking System
# # Create a travel booking system.

# # Select transport:

# # 1 → Flight
# # 2 → Train
# # 3 → Bus
# # Then show options:

# # Flight:

# # 1 → Economy
# # 2 → Business
# # Train:

# # 1 → Sleeper
# # 2 → AC
# # Bus:

# # 1 → Ordinary
# # 2 → Volvo
# # Use nested match-case.


# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Flight selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Economy")
# #             case 2:
# #                 print("Business")
# #     case 2:
# #         print("Train selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Sleeper")
# #             case 2:
# #                 print("AC")
# #     case 3:
# #             print("Bus selected")
# #             a=int(input("Enter your choice: "))
# #             match a:
# #                 case 1:
# #                     print("Ordinary")
# #                 case 2:
# #                     print("Volvo")
# #     case _:
# #         print("Invalid input")




# # Q34. Gaming Console Menu
# # Create a gaming console menu:

# # 1 → Start Game
# # 2 → Load Game
# # 3 → Settings
# # 4 → Exit
# # If Settings is selected, show:

# # 1 → Sound
# # 2 → Graphics
# # 3 → Controls
# # Use nested match-case for the Settings menu.

# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Start Game")
# #     case 2:
# #         print("Load Game")
# #     case 3:
# #         print("Settings")
# #         a=int(input("Enter choice: "))
# #         match a:
# #             case 1:
# #                 print("Sound")
# #             case 2:
# #                 print("Graphics")
# #             case 3:
# #                 print("Controls")
# #     case 4:
# #         print("Exit")
# #     case _:
# #         print("Invalid input")



# # Q35. Restaurant Ordering System
# # Create a restaurant ordering system.

# # First select a category:

# # 1 → Starters
# # 2 → Main Course
# # 3 → Desserts
# # 4 → Drinks
# # Then show different items for each category.

# # Example:

# # Starters:

# # 1 → Soup
# # 2 → Spring Roll
# # 3 → Garlic Bread
# # Main Course:

# # 1 → Pizza
# # 2 → Pasta
# # 3 → Biryani
# # Desserts:

# # 1 → Ice Cream
# # 2 → Cake
# # 3 → Gulab Jamun
# # Drinks:

# # 1 → Coffee
# # 2 → Tea
# # 3 → Juice
# # Use nested match-case.



# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Starters options selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Soup")
# #             case 2:
# #                 print("Spring Roll")
# #             case 3:
# #                 print("Garlic Bread")
# #     case 2:
# #         print("Main course options selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Pizza")
# #             case 2:
# #                 print("Pasta")
# #             case 3:
# #                 print("Biryani")
# #     case 3:
# #             print("Drinks option selected")
# #             a=int(input("Enter your choice: "))
# #             match a:
# #                 case 1:
# #                     print("Coffee")
# #                 case 2:
# #                     print("Tea")
# #                 case 3:
# #                     print("Juice")
# #     case 4:
# #                 print("Desserts option selected")
# #                 a=int(input("Enter your choice: "))
# #                 match a:
# #                     case 1:
# #                         print("Ice Cream")
# #                     case 2:
# #                         print("Cake")
# #                     case 3:
# #                         print("Gulab Jamun")
# #     case _:
# #         print("Invalid input")




# # Q36. Digital Payment Application
# # Create a digital payment application.

# # Payment type:

# # 1 → UPI
# # 2 → Card
# # 3 → Wallet
# # If UPI is selected:

# # 1 → Scan QR
# # 2 → Enter UPI ID
# # If Card is selected:

# # 1 → Credit Card
# # 2 → Debit Card
# # If Wallet is selected:

# # 1 → Add Money
# # 2 → Pay Using Wallet
# # Use nested match-case.

# # choice=int(input("Enter your choice: "))
# # match choice:
# #     case 1:
# #         print("Upi selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Scan QR")
# #             case 2:
# #                 print("Enter UPI id")
# #     case 2:
# #         print("Card selected")
# #         a=int(input("Enter your choice: "))
# #         match a:
# #             case 1:
# #                 print("Credit Card")
# #             case 2:
# #                 print("Debit Card")
# #     case 3:
# #             print("Wallet selected")
# #             a=int(input("Enter your choice: "))
# #             match a:
# #                 case 1:
# #                     print("Add Money")
# #                 case 2:
# #                     print("Pay using wallet")
# #     case _:
# #         print("Invalid input")




# # Q37. Online Learning Platform
# # Create an online learning platform.

# # First select:

# # 1 → Programming
# # 2 → Mathematics
# # 3 → Communication
# # Programming:

# # 1 → Python
# # 2 → Java
# # 3 → C++
# # Mathematics:

# # 1 → Algebra
# # 2 → Calculus
# # 3 → Statistics
# # Communication:

# # 1 → English
# # 2 → Presentation
# # 3 → Interview Skills
# # Use nested match-case.



# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("Programming")
#         a=int(input("Enter your choice: "))
#         match a:
#             case 1:
#                 print("Python")
#             case 2:
#                 print("Java")
#             case 3:
#                 print("C++")
#     case 2:
#         print("Mathematics")
#         a=int(input("Enter your choice: "))
#         match a:
#             case 1:
#                 print("Algebra")
#             case 2:
#                 print("Calculus")
#             case 3:
#                 print("Statistics")
#     case 3:
#             print("Communication")
#             a=int(input("Enter your choice: "))
#             match a:
#                 case 1:
#                     print("English")
#                 case 2:
#                     print("Communication")
#                 case 3:
#                     print("Interview Skills")
#     case _:
#         print("Invalid input")





# # Q38. Smart Vehicle Dashboard
# # Create a vehicle dashboard.

# # Main options:

# # 1 → Engine
# # 2 → Lights
# # 3 → Music
# # 4 → Navigation
# # For Engine:

# # 1 → Start
# # 2 → Stop
# # For Lights:

# # 1 → Headlights
# # 2 → Indicators
# # 3 → Hazard Lights
# # For Music:

# # 1 → Play
# # 2 → Pause
# # 3 → Next
# # 4 → Previous
# # For Navigation:

# # 1 → Start Navigation
# # 2 → Stop Navigation
# # Use nested match-case.

# # dashboard = int(input('----Smart Vehicle Dashboard----\n1.Engine\n2.Lights\n3.Music\n4.Navigation\n: '))

# # match dashboard:
# #     case 1:
# #         engine = int(input('----Engine----\n1.Start\n2.Stop\n: '))
# #         match engine:
# #             case 1:
# #                 print("Engine Started")
# #             case 2:
# #                 print("Engine Stopped")
# #     case 2:
# #         lights= int(input('----Lights----\n1.Headlights\n2.Indicators\n3.Hazard Lights\n: '))
# #         match lights:
# #             case 1:
# #                 print("Headlights Turned On")
# #             case 2:
# #                 print("Indicators Turned On")
# #             case 3:
# #                 print("Hazard Lights Turned On")
# #     case 3:
# #         music = int(input('----Music----\n1.Play\n2.Pause\n3.Next\n4.Previous\n: '))
# #         match music:
# #             case 1:
# #                 print("Music Playing")
# #             case 2:
# #                 print("Music Paused")
# #             case 3:
# #                 print("Next Track Playing")
# #             case 4:
# #                 print("Previous Track Playing")
# #     case 4:
# #         navigation = int(input('----Navigation----\n1.Start Navigation\n2.Stop Navigation\n: '))
# #         match navigation:
# #             case 1:
# #                 print("Navigation Started")
# #             case 2:
# #                 print("Navigation Stopped")



# # Q39. Employee Portal
# # Create an employee portal.

# # Main menu:

# # 1 → Employee
# # 2 → Manager
# # Employee options:

# # 1 → View Profile
# # 2 → Apply Leave
# # 3 → View Salary
# # Manager options:

# # 1 → View Team
# # 2 → Approve Leave
# # 3 → View Reports
# # Use nested match-case.

# # For the Apply Leave option, ask for the number of leave days.

# # Use if to check:

# # If leave days are greater than 0, display Leave Request Submitted.
# # Otherwise display Invalid Leave Days.
# # This problem should use both match-case and if.

# choice=int(input("Enter the choice: "))
# match choice:
#     case 1:
#         print("Employee")
#         a=int(input("Enter your choice: "))
#         match a:
#             case 1:
#                 print("View Profile")
#             case 2:
#                 print("Apply Leave")
#                 leave=int(input("Enter the number of leaves: "))
#                 if(leave>0):
#                     print("Leave approved")
#                 else:
#                     print("Invalid leave days")
#             case 3:
#                 print("View salary")
#     case 2:
#         print("Manager")
#         a=int(input("Enter your choice: "))
#         match a:
#             case 1:
#                 print("View Team")
#             case 2:
#                 print("Approve Leave")
#             case 3:
#                 print("View Reports")
#     case _:
#         print("Invalid input")



# # 40.Create a small college portal.

# # Main menu:

# # 1 → Student
# # 2 → Teacher
# # 3 → Administration
# # Student
# # 1 → Profile
# # 2 → Marks
# # 3 → Attendance
# # 4 → Courses
# # Teacher
# # 1 → Students
# # 2 → Enter Marks
# # 3 → Attendance
# # 4 → Courses
# # Administration
# # 1 → Fees
# # 2 → Admissions
# # 3 → Notices
# # 4 → Departments
# # Requirements:

# # Use match-case for the main menu.
# # Use nested match-case for the selected role.
# # Use case _ for invalid choices.
# # Keep the program easy to read.
# # Do not use if-elif-else for fixed menu choices.
# # Sample Input
# # Enter role: 1
# # Enter option: 2
# # Sample Output
# # Opening Student Marks

# choice = int(input('----Your Role---\n1.Student\n2.Teacher\n3.Administration\n: '))

# match choice :
#     case 1:
#         student_choice=int(input('---Student Menu---\n1.Profile\n2.Marks\n3.Attendance\n4.Courses\n: '))
#         match student_choice:
#             case 1:
#                 print('Opening Profile')
#             case 2:
#                 print('Opening Marks')
#             case 3:
#                 print('Opening Attendance')
#             case 4:
#                 print('Opening Courses')
#             case _:
#                 print('Invalid Choice')     
#     case 2:
#         teacher_choice = int(input('---Teacher Menu---\n1.Student\n2.Enter Marks\n3.Attendance\n4.Courses\n: '))
#         match teacher_choice:
#             case 1:
#                 print('Opening Students List')
#             case 2:
#                 print('Opening Marks Entering Page')
#             case 3:
#                 print('Opening Attendance Page')
#             case 4:
#                 print('Opening Courses')
#             case _:
#                 print('Invalid Choice')     
#     case 3:
#         admin_choice=int(input('---Admin Menu---\n1.Fees\n2.Admissions\n3.Notices\n4.Departments\n: '))
#         match admin_choice:
#             case 1:
#                 print('Opening Fee Management Portal')
#             case 2:
#                 print('Opening Admission Management Portal')
#             case 3:
#                 print('Opening Notice Mangement Portal')
#             case 4:
#                 print('Opening Department Management Portal')
#             case _:
#                 print('Invalid Choice')   
                
#     case _:
#         print('Invalid Choice')