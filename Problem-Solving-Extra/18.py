# 18. Temperature Classifier
# Take temperature in Celsius.

# Print:

# Below 0      → Freezing
# 0–15         → Very Cold
# 16–25        → Cold
# 26–35        → Normal
# Above 35     → Hot

temp=int(input("Enter the temperature: "))
if(temp<0):
    print("Freezing")
elif(temp<16):
    print("Very Cold")
elif(temp<26):
    print("Cold")
elif(temp<36):
    print("Normal")
else:
    print("Hot")