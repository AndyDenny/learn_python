cause = ''
while cause != 'exit':
    cause = input("Why you like programming? (type 'exit' to quit): ")
    if cause != 'exit':
        with open('causes.txt', 'a') as file_object:
            file_object.write(f"I like programming, because {cause}\n")


