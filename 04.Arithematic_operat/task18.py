value = None

# Testing arithmetic with None:
# value + 5   -> TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# value - 5   -> TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
# value * 5   -> TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
# value / 5   -> TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'
# value // 5  -> TypeError: unsupported operand type(s) for //: 'NoneType' and 'int'
# value % 5   -> TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'
# value ** 5  -> TypeError: unsupported operand type(s) for **: 'NoneType' and 'int'

# Explanation: None represents the complete absence of a value. It doesn't have a numerical
# equivalent in Python, so arithmetic operators don't know how to evaluate it with numbers.