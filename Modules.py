#Use random and datetime in script
import random
from datetime import datetime

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Get current date and time
now = datetime.now()

# Print results
print("Random Number:", random_number)
print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

#Create math_utils module and import it
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
# main.py

import math_utils

print("Add:", math_utils.add(5, 3))
print("Subtract:", math_utils.subtract(10, 4))
print("Multiply:", math_utils.multiply(2, 6))
print("Divide:", math_utils.divide(8, 2))
