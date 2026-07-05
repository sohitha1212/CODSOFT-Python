# ============================================
# CodSoft Python Internship
# Task 2: Simple Calculator
# ============================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


while True:
    print("\n" + "=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 40)

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("\nThank you for using the Calculator!")
        break

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")

            elif choice == "2":
                print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == "3":
                print(f"\nResult: {num1} × {num2} = {multiply(num1, num2)}")

            elif choice == "4":
                result = divide(num1, num2)
                print(f"\nResult: {result}" if isinstance(result, str)
                      else f"\nResult: {num1} ÷ {num2} = {result}")

        except ValueError:
            print("\nInvalid input! Please enter valid numbers.")

    else:
        print("\nInvalid choice! Please select a number between 1 and 5.")
