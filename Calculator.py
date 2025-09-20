print("Welcome to the Calculator Created using Python Language")

def addition(x , y):
    return x + y

def subtraction(x , y):
    return x-y

def multiplication(x , y):
    return x * y

def division(x , y):
    if y == 0:
        print(f"You can not divide {x} by Zero.")
        return None
    else:
        return x / y

while True:
    num1 = float(input("Enter First Digit:"))
    operator = input("Enter Operators (+, -, *, /, ^) or 'e' to exit: ")
    if operator == 'e':
        print("GoodBye!")
        break
    else:
        num2 = float(input("Enter Second Digit:"))
        match operator:
            case "+":
                print(f"{num1} + {num2} = " , addition(num1 , num2))
            case "-":
                print(f"{num1} - {num2} = " , subtraction(num1 , num2))
            case "*":
                print(f"{num1} * {num2} = " , multiplication(num1 , num2))
            case "/":
                result = division(num1 , num2)
                if result is not None:
                    print(f"{num1} / {num2} = " , result)
            case "^":
                print(f"{num1} ^ {num2} = " , pow(num1 , num2))
            case _:
                print("You've Chosen Wrong Operator.")
