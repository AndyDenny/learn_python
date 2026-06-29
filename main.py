class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_guests):
        self.number_served += number_guests


    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is opened")



restaurant = Restaurant("Myres", "russian")
print(restaurant.number_served)
restaurant.number_served = 7
print(restaurant.number_served)
restaurant.set_number_served(14)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)


