def addition(x, y):
    return x + y

def subtraction(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y

def display_history(history):
    if history:
        print("Calculation History:")
    else:
        print("Calculation History is empty.")

def calculator():
    history = []

    while True:
        print("Simple calculator:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exit")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                result = num1 + num2
                print("Result:", result)
            elif choice == '2':
                result = num1 - num2
                print("Result:", result)
            elif choice == '3':
                result = num1 * num2
                print("Result:", result)
            elif choice == '4':
                if num2 == 0:
                    print("Error! Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print("Result:", result)
            history.append((num1, num2, result))
        elif choice == '5':
            print("History:")
            for operation in history:
                print(operation)
        else:
            print("Invalid choice.")

calculator()