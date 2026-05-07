def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ValueError("Modulo by zero not allowed")
    return a % b

def floor_divide(a, b):
    if b == 0:
        raise ValueError("Integer division by zero not allowed")
    return a // b

def main():
    while True:
        print("\n--- PyCalc ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus (remainder)")
        print("7. Integer division")
        print("8. Exit")

        choice = input("Choose operation (1-8): ")

        if choice == '8':
            print("Exiting...")
            break

        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid choice, please try again.")
            continue

        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Invalid input, please enter numbers.")
            continue

        try:
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)
            elif choice == '6':
                result = modulo(num1, num2)
            elif choice == '7':
                result = floor_divide(num1, num2)

            print(f"Result: {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()