from Restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self):
        self.flavors = ["vanilla", "chocolate", "strawberry", "raspberry"]

    def show_flavors(self):
        return self.flavors


restr = Restaurant("MyTreshka","russian")
restr.open_restaurant()
