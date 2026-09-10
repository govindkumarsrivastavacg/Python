# 16. Electricity Bill
# Calculate electricity bill based on units.

# Rules:

# First 100 units      → ₹5 per unit
# Next 100 units       → ₹7 per unit
# Above 200 units      → ₹10 per unit

unit=int(input("Enter your electric units: "))
if(unit>0):
    if(unit<=100):
        bill=unit*5
    elif(unit<=200):
        bill=(unit-100)*7+500
    elif(unit>200):
        bill=(500+700+(unit-200)*10)
    print(bill)
else:
    print("Enter a valid unit")