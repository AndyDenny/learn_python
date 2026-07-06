try:
    with open('cats2.txt') as file:
        filedata = file.read()
        print(filedata)
except FileNotFoundError:
    print(f"File cats2.txt not found")

try:
    with open('dogs.txt') as file:
        filedata = file.read()
        print(filedata)
except FileNotFoundError:
    print("File dogs2.txt doesn't exist")