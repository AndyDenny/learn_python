end = False
while not end:
    try:
        a = input("Enter first number (type 'q' to quit): ")
        if a == 'q':
            end = True
        a = int(a)
        b = input("Enter second number (type 'q' to quit): ")
        if b == 'q':
            end = True
        b = int(b)
        print(f"Total: {a + b}")
        end = True
    except ValueError:
        print("Please enter a number.\n")