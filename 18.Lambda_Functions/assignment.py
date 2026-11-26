# Practice Questions
# Try solving these without looking at the examples.

# 1.Create a lambda function to multiply two numbers.

# product=lambda a,b:a*b
# print(product(6,7))

#2. Create a lambda function to calculate the cube of a number.

# cube=lambda a:a**3
# print(cube(5))


#3. Create a lambda function to check whether a number is positive or negative.

# check=lambda n:"positive" if n>=0 else "negative"
# print(check(-8))


#4. Create a lambda function to find the smaller of two numbers.

# smaller=lambda a,b:a if a<b else b
# print(smaller(9,-8))

#5. Create a lambda function to calculate the area of a rectangle.

# Area=lambda l,b:l*b
# print(Area(5,4))


#6. Create a lambda function to convert a string into lowercase.

# toLower=lambda a:a.lower()
# print(toLower("ProgramminG"))



#7. Create a lambda function to check whether a character is a vowel.

# check=lambda c:"Vowel" if c in "aieou" else "not a vowel"
# print(check('a'))

#8. Use map() and lambda to convert every character of "coding" into uppercase.

# word="IdkMan"
# up=map(lambda c:c.upper(),word)
# print("".join(up))

#9. Use filter() and lambda to extract vowels from "programming".
# word="Programming"
# vowel=filter(lambda c:c  in "aeiouAEIOU",word)
# print("".join(vowel))


