num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
oparation=input("Choose the operation (+, -, *, /):")
match oparation:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        try:
            print(num1/num2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
    case "_":
        print("oparation not available")