"""
Take two numbers from user and perform at least 4 arithmetic operations on them.
"""

# Input two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
add = num1 + num2

sub = num1 - num2

mul = num1 * num2

div = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Print results
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
