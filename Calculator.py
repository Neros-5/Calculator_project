# This is a Calculator project
number1 = eval(input("enter first number "))
number2 = eval(input("enter second number "))

operator = input("Enter operator: ")


def add(number1, number2):
    result = number1 + number2
    print(result)


def subtract(number1, number2):
    result = number1 - number2
    print(result)


def divide(number1, number2):
    result = number1 / number2
    print(result)


def multiply(number1, number2):
    result = number1 * number2
    print(result)


# Check operator functions
if operator == '+':
    add(number1, number2)
elif operator == '-':
    subtract(number1, number2)
elif operator == '/':
    divide(number1, number2)
elif operator == 'X' or operator == 'x' or operator == '*':
    multiply(number1, number2)
else:
    print("Invalid operator")

# Calculator functons well