with open('Alice2.txt') as file:
    content = file.read()
    print(content.lower().count('the'))