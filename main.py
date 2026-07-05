name = ''
while name != 'exit':
    name = input("What is your name? (type 'exit' to quit): ")
    if name != 'exit':
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f"{name.title()}\n")
            print(f"Glad to see you {name.title()}!")

