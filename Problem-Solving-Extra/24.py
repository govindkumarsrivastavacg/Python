# 24. Discount Calculator
# Take purchase amount.

# Apply:

# Below ₹500       → 0%
# ₹500–999         → 5%
# ₹1000–1999       → 10%
# ₹2000–4999       → 15%
# ₹5000 and above  → 20%
# Print:

# Original amount
# Discount percentage
# Discount amount
# Final amount

orig_amt=int(input("Enter original amount"))
if(orig_amt<0):
    print("Invalid amount")
elif(orig_amt<500):
    disc=(orig_amt)*0/100 
    x=0 
elif(orig_amt<=999):
    disc=(orig_amt)*5/100
    x=5
elif(orig_amt<=1999):
    disc=(orig_amt)*10/100
    x=10
elif(orig_amt<=4999):
    disc=(orig_amt)*15/100
    x=15
elif(orig_amt>=5000):
    disc=(orig_amt)*0.2
    x=20
print(f"Original amount:{orig_amt}")
print(f"Discount%:{x}")
print(f"Discount amount:{disc}")
print(f"final amount:{orig_amt-disc}")