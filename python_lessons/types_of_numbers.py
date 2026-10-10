import sys

try:
    num = int(input("Enter the number: "))
except ValueError:
    print("Error: Invalid input!")
    sys.exit(1)

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")