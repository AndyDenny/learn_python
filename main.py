from unicodedata import digit

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\n--------------\n")
pizzas_menu = ["pepperoni", "calcione", "margarita", "neapolitan"]
my_favorite_pizza = 'roman'
print(my_favorite_pizza in pizzas_menu)
print(my_favorite_pizza not in pizzas_menu)
print(my_favorite_pizza == 'roman')
print(my_favorite_pizza == 'margarita')
print(my_favorite_pizza != 'roman')
print(my_favorite_pizza != 'margarita')
my_favorite_pizza = 'calcione'
print(my_favorite_pizza in pizzas_menu)
print(my_favorite_pizza not in pizzas_menu)
print(my_favorite_pizza == 'calcione')
print(my_favorite_pizza == 'margarita')
print(my_favorite_pizza != 'calcione')
print(my_favorite_pizza == my_favorite_pizza.lower())
print(my_favorite_pizza.title() == my_favorite_pizza.lower())
first_digit = 5
second_digit = 5
third_digit = 15
print(first_digit == second_digit)
print(first_digit != second_digit)
print(first_digit == third_digit)
print(first_digit != third_digit)
print(first_digit > second_digit)
print(first_digit >= second_digit)
print(first_digit > third_digit)
print(first_digit >= third_digit)
print(first_digit < second_digit)
print(first_digit <= second_digit)
print(first_digit < third_digit)
print(first_digit <= third_digit)
print(first_digit and second_digit == '5')
print((first_digit and second_digit) == 5)
print(first_digit and third_digit == '5')
print((first_digit and third_digit) == 5)
print((first_digit or second_digit) == '5')
print((first_digit or second_digit) == 5)
print((first_digit or third_digit) == '5')
print((first_digit or third_digit) == 5)
