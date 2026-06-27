def add(num1, num2):
    result = num1 + num2
    return add(num1, num2)
    print(result)
def subtract(num1, num2):
    result = num1 - num2
    return subtract(num1, num2)
    print(result)
def multiply(num1, num2):
    result = num1 * num2
    return multiply(num1, num2)
    print(result)
def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        return divide(num1, num2)
        print(result)
    else:
        return "Error: Division by zero is not allowed."