
try:
    first_digit = int(input("Enter first number (type 'q' to quit): "))
except ValueError:
    print("Please enter a number.")

try:
    second_digit = int(input("Enter second number (type 'q' to quit): "))
except ValueError:
    print("Please enter a number.")


total = first_digit + second_digit

print(total)

