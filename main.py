with open('learning_python.txt') as file_object:
    contents = file_object.readlines()
    for line in contents:
        new_line = line.replace('Python', 'C')
        print(new_line.strip())