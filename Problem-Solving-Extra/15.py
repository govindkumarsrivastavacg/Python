# 15. Profit/Loss Percentage
# Take:

# Cost price
# Selling price
# Calculate:

# Profit = Selling Price - Cost Price
# Loss = Cost Price - Selling Price
# Then calculate the appropriate percentage.

cp,sp=map(int,input("Enter the price: ").split())
if(cp>sp):
    Loss=cp-sp
    loss_per=(Loss/cp)*100
    print(f"The Loss % is: {loss_per}")
elif(cp<sp):
    Profit=sp-cp
    profit_per=(Profit/cp)*100
    print(f"The profit % is: {profit_per}")
else:
    print("No profit no loss")