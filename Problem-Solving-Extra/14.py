# 14. Profit or Loss
# Take:

# Cost price
# Selling price
# Determine whether there is:

# Profit
# Loss
# No profit and no loss

cp,sp=map(int,input("Enter the price: ").split())
if(cp>sp):
    print(f"Loss={cp-sp}")
elif(cp<sp):
    print(f"Profit={sp-cp}")
else:
    print("No profit no loss")