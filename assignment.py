#Python  Calculator

# Simple Calculator 

num1 = float(input("Enter the first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the chosen operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid operation!"

# Display the result
print("Result:", result)

