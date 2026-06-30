class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is opened")

class IceCreamStand(Restaurant):
    def __init__(self):
        self.flavors = ["vanilla", "chocolate", "strawberry","raspberry"]

    def show_flavors(self):
        return self.flavors


ice_cream_stand = IceCreamStand()
print(ice_cream_stand.show_flavors())