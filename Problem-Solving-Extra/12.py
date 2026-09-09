# 12. Character Type
# Take one character.

# Determine whether it is:

# Uppercase alphabet
# Lowercase alphabet
# Digit
# Special character

charac=input("Enter a character: ").strip()
if(charac.islower()):
    print("Lowercase Alphabet")
elif(charac.isupper()):
    print("Uppercase Alphabet")
elif(charac.isdigit()):
    print("Digit")
else:
    print("Speical Character")
