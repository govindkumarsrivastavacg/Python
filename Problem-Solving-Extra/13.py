# 13. Vowel or Consonant
# Take one character.

# Determine whether it is:

# Vowel
# Consonant
# Invalid input

charac=input("Enter an alphabet:").lower().strip()
if(charac=="a" or charac=="e" or charac=="i" or charac=="o" or charac=="u"):
    print("Vowel")
elif(charac.isalpha()==False):
    print("invalid input")
else:
    print("Consonant")