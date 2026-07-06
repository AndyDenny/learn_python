try:
    with open('cats2.txt') as file:
        filedata = file.read()
        print(filedata)
except FileNotFoundError:
    pass

try:
    with open('dogs.txt') as file:
        filedata = file.read()
        print(filedata)
except FileNotFoundError:
    pass