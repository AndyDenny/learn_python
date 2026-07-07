import json
"""
before using - delete 'dump.json'
"""
try:
    with open('dump.json') as file:
        number = json.load(file)
except FileNotFoundError:
    number = input("Enter your favorite number: ")
    with open('dump.json', 'w') as file:
        json.dump(number, file)
else:
    print(f"Your favorite number - {number}!")

