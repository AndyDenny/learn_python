with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('learning_python.txt') as file_object:
    contents = file_object.readlines()
    for line in contents:
        print(line)

with open('learning_python.txt') as file_object:
    contents = file_object.readlines()
    t_line = ''
    for line in contents:
        t_line += line

print(t_line)