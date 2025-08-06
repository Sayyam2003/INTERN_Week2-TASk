#Simple Calculator Function
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif op == '%':
        return a % b
    else:
        return "Invalid operator"

# Example:
print(calc(10, 5, '+'))  # Output: 15
print(calc(10, 0, '/'))  # Output: Error: Division by zero

#Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example:
print(factorial(5))  # Output: 120
