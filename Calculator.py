# This is a Calculator project
number1 = eval(input("enter ftrst number "))
number2 = eval(input("enter second number "))

operator  = input("Enter operator: ")

def add(number1, number2):
    result = number1 + number2
    return result
def subtract(number1, number2):
    result = number1 - number2
    return result
def divide(number1, number2):
    result = number1 / number2
    return result
def multiply(number1,number2):
    result = number1 * number2
    return result
# Check operator function
if operator == '+':
    add(number1, number2)
elif operator == '-':
    subtract(number1, number2)
elif operator == '/':
    divide(number1, number2)
elif operator == 'X' or operator =='x' or operator =='*':
    multiply(number1, number2)