
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None

def get_operation():
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    return input("Enter choice (1/2/3/4): ")

def perform_calculation(choice, a, b):
    if choice == "1":
        return add(a, b)
    elif choice == "2":
        return subtract(a, b)
    elif choice == "3":
        return multiply(a, b)
    elif choice == "4":
        return divide(a, b)
    else:
        return "Invalid operation"

def main():
    print("CALCULATOR")

    while True:
        a, b = get_numbers()

        if a is None or b is None:
            continue

        choice = get_operation()
        result = perform_calculation(choice, a, b)

        print("Result:", result)

        again = input("\nDo you want to continue? (yes/no): ")
        if again.lower() != "yes":
            print("Thank You!")
            break

if __name__ == "__main__":
    main()
