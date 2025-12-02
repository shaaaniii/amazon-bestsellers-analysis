def show_menu():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide(/)")
    print("5. Exponentiation (^)")
    print("5. Exit")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter choice(1-5) : or 6 to exit ")

    try:
        if choice == '1':
            print("result = " f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print("result = " f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print("result = " f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            print("result = " f"{num1} ^ {num2} = {num1 ** num2}")
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
        else:
            print("Invalid input")
            result = None
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

    while True:
        show_menu()
        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    show_menu()
