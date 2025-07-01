num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        print(f'The result is{num1 + num2}')
    case "-":
        print(f'The result is{num1 - num2}')
    case "*":
        print(f'The result is{num1 * num2}')
    case "/":
        try:
            print(f'The result is{num1 / num2}')
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
    case _:
        print("operation not available")
