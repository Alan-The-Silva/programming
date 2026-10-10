while True:
    num1 = float(input("what's your x? "))
    num2 = float(input("what's your y? "))
    choice = str(input("Choose operation(+,-,*,/) "))

    if choice == '+':
        print(round(num1 + num2, 2))
    elif choice == '-':
        print(round(num1 - num2, 2))
    elif choice == '*':
        print(round(num1 * num2, 2))
    elif choice == '/':
        if num2 == 0:
            print("Can't divide by zero")
        else:
            print(round(num1 / num2, 2))
    else:
        print("Invalid input! Choose the right operation")
        continue

    run_again = input("Do you want to continue? (yes/no): ").lower()
    if run_again != "yes":
        print("Goodbye! Have a Great Day.")