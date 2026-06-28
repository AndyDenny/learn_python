"""
Автомобили: напишите функцию для сохранения информации об автомобиле в словаре.
Функция всегда должна возвращать производителя и название модели, но при этом она может получать произвольное количество именованных аргументов.
Вызовите функцию с передачей обязательной информации и еще двух пар «имя — значение» (например, цвет и комплектация).
Ваша функция должна работать для вызовов следующего вида:
car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
Выведите возвращаемый словарь и убедитесь в том, что вся информация была сохранена правильно.
"""
def make_car(model: str, provider: str, color = 'blue', tow_package = True):
    """Строит словарь с информацией об автомобиле."""
    car_info = {
        'model': model,
        'provider': provider,
        'color': color,
        'tow_package': tow_package
    }

    for key, value in car_info.items():
        car_info[key] = value
    return car_info

car = make_car('subaru', 'outback', 'blue', True)
print(car)