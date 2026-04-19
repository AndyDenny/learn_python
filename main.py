favorite_digits = {
    "Andy": ["57","59"],
    "Sandy": ["45","47"],
    "Mandy": ["120","123"],
    "Vendy": ["12338","12345"]
}
for name, digits in favorite_digits.items():
    print(name + "'s favorite digits:")
    for digit in digits:
        print(digit)
