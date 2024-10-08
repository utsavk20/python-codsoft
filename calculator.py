# Define a function for each arithmetic operation
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Prompt the user to input two numbers and an operation choice
print("Simple Calculator")
print("----------------")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input("Enter your choice (1/2/3/4): "))

# Perform the calculation based on the user's choice
if operation == 1:
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is {result}")
elif operation == 2:
    result = sub(num1, num2)
    print(f"The result of {num1} - {num2} is {result}")
elif operation == 3:
    result = mul(num1, num2)
    print(f"The result of {num1} * {num2} is {result}")
elif operation == 4:
    result = div(num1, num2)
    print(f"The result of {num1} / {num2} is {result}")
else:
    print("Invalid operation choice!")
