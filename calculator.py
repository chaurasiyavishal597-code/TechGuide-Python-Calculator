
# Tech Guide Python Internship
# Task 1: Calculator

def display_title():
    print("=" * 35)
    print("       CALCULATOR")
    print("=" * 35)


def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input! Please enter a number.")


def show_operations():
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")


def calculate(num1, num2, choice):
    if choice == "1":
        return num1 + num2
    elif choice == "2":
        return num1 - num2
    elif choice == "3":
        return num1 * num2
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return None
        return num1 / num2
    else:
        print("Invalid operation selected.")
        return None


def main():
    display_title()

    while True:
        show_operations()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Please select a valid option.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        result = calculate(num1, num2, choice)

        if result is not None:
            print("Result:", result)


if __name__ == "__main__":
    main()
