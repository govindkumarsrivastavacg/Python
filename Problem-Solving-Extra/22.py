# 22. ATM Withdrawal
# Take:

# Account balance
# Withdrawal amount
# Rules:

# Withdrawal amount must be greater than 0.
# Withdrawal amount must be divisible by 100.
# Withdrawal amount cannot be greater than the balance.
# After withdrawal, at least ₹500 must remain.


balance,withdrawal=map(int,input("Enter the values").split())
if(balance>withdrawal and withdrawal>0 and withdrawal%100==0 and balance-withdrawal>=500):
    print("Withdrawal Successful")
    print(f"Balance:{balance-withdrawal}")
else:
    print("Withdrawal Failed")
