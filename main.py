from random import randint

class Die:
    def __init__(self, side = 6):
        self.side = side

    def roll_die(self):
        return randint(1, self.side)


six_die = Die()
ten_die = Die(10)
twenty_die = Die(20)

for i in range(10):
    print(f"{six_die.roll_die()}")
print("=6 sides end=")

for i in range(10):
    print(f"{ten_die.roll_die()}")
print("=10 sides end=")

for i in range(10):
    print(f"{twenty_die.roll_die()}")
print("=20 sides end=")