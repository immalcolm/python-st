# Operators in Python
# This script demonstrates various types of operators in Python
# Arithmetic, Comparison, Logical, and Assignment Operators
# Operators are from right to left precedence
# How is this important for QA Testers? QA Engineers?
# Understanding operators helps in validating calculations, conditions, and data manipulations in code.

a = 10
b = 3
# Arithmetic Operators
# These operators perform mathematical operations on numeric values
print("Addition: a + b =", a + b)
print("Subtraction: a - b =", a - b)
print("Multiplication: a * b =", a * b)
print("Division: a / b =", a / b)
print("Floor Division: a // b =", a // b)
print("Modulus: a % b =", a % b)
print("Exponentiation: a ** b =", a ** b)

# Comparison Operators
# These operators compare two values and return a boolean result
print("Equal: a == b is", a == b)
print("Not Equal: a != b is", a != b)
print("Greater than: a > b is", a > b)
print("Less than: a < b is", a < b)
print("Greater than or equal to: a >= b is", a >= b)
print("Less than or equal to: a <= b is", a <= b)

# Logical Operators
# These operators are used to combine conditional statements
x = True
y = False
print("Logical AND: x and y is", x and y)
print("Logical OR: x or y is", x or y)
print("Logical NOT: not x is", not x)
print("Logical NOT: not y is", not y)

# Assignment Operators
c = 5
print("Initial value of c:", c)
c += 2
print("After c += 2, c =", c)
c -= 1
print("After c -= 1, c =", c)
c *= 3
print("After c *= 3, c =", c)
c /= 2
print("After c /= 2, c =", c)
c %= 4
print("After c %= 4, c =", c)
c **= 2
print("After c **= 2, c =", c)
c //= 3
print("After c //= 3, c =", c)
print('\n new line')
print("End of program")

# Type conversion with operators
num_str = "100"
num_int = 50
# Convert string to integer for addition
total = int(num_str) + num_int
print("Total after converting string to integer and adding:", total)
# Concatenate string and integer (after converting integer to string)
concat = num_str + str(num_int)
print("Concatenation of string and integer (as string):", concat)
print('\n End of program')

# float and int conversion
float_num = 12.75
int_num = int(float_num)  # Convert float to int (truncates decimal)
print("Converted float to int:", int_num)
new_float = float(int_num)  # Convert int back to float
print("Converted int back to float:", new_float)
print('\n End of program')
