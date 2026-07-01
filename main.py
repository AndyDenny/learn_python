class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading += mileage
        else:
            print("Sorry, that's not enough odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car hasn't a gas tank")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 280
        elif self.battery_size == 85:
            range = 1600

        print(f"This car has {range} miles left")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


mytesla = ElectricCar('Tesla', 'model s', 2020)
print(mytesla.get_descriptive_name())
mytesla.battery.describe_battery()
mytesla.battery.get_range()
mytesla.battery.upgrade_battery()
mytesla.battery.get_range()

