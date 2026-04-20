input_str = "\nВведите возраст чтобы узнать стоимость:"
input_str += "\n(Введите 'quit’ для остановки работы программы.) "
active = True

while active:
    age = input(input_str)
    if age == 'quit':
        active = False

    if int(age) < 3:
        print("Билет бесплатный")
    elif int(age) >= 3 and int(age) <= 12:
        print("Билет стоит $10")
    elif int(age) >= 12:
        print("Билет стоит $15")

