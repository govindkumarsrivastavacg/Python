s1 = "Hello"
s2 = "World"

print("string + string works:", s1 + s2)
print("string * integer works:", s1 * 2)

# Unsupported operations:
# s1 - s2  -> TypeError: unsupported operand type(s) for -: 'str' and 'str'
# s1 / s2  -> TypeError: unsupported operand type(s) for /: 'str' and 'str'