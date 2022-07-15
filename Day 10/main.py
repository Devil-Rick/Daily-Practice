import logo as lg
import replit as rep


def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == '/':
        return num1 / num2


try:
    print(lg.logo, "\n\n")
    again = ''
    num1 = int(input("What's the 1st number ? : "))
    while again != 'clear':
        if again == "n":
            rep.clear()
            print(lg.logo, "\n\n")
            num1 = float(input("What's the 1st number ? : "))
        print("+\n-\n*\n/")
        operation = input("Pick an operation : ")
        num2 = float(input("What's the 2nd number ? : "))
        answer = calculator(num1, num2, operation)
        num1 = answer
        again = input(
            f"Type 'y' to continue calculating with {answer} , 'n' to start a new calculation , 'clear' to terminate the program : ").lower()
except:
    print("Invalid Input")
