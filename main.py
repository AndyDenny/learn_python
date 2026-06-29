class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is opened")



restaurant1 = Restaurant("Myres", "russian")
restaurant2 = Restaurant("Rrestourant", "english")
restaurant3 = Restaurant("Mrestorante", "italian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
