my_pizzas = ["pepperoni", "calcione", "margarita", "neapolitan"]
friend_pizzas =  my_pizzas[:]
my_pizzas.append("pineapple")
friend_pizzas.append("romana")
for pizza in my_pizzas:
    print("My favorite pizzas are: " + pizza)

for pizza in friend_pizzas:
    print("My friend’s favorite pizzas are:" + pizza)