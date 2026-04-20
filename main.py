input_str = "\nВведите топпинг для пиццы:"
input_str += "\n(Введите 'quit’ для остановки работы программы.) "

while True:
    topping = input(input_str)

    if topping == 'quit':
        break
    print(topping + " добавлен в заказ")