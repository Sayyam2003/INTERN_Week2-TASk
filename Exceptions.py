#Safe Integer Input loop
while True:
    try:
        user_input = int(input("Enter an integer: "))
        print(f"You entered: {user_input}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

#Open a File with Error Message
filename = "example.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as e:
    print(f"I/O error occurred: {e}")
