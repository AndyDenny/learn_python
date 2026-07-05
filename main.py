from collections import OrderedDict

favorite_digits = OrderedDict()

favorite_digits["Andy"]= "57"
favorite_digits["Vendy"]= "12338"
favorite_digits["Sandy"]= "45"
favorite_digits["Mandy"]= "120"

for name, digit in favorite_digits.items():
    print(f"{name}: {digit}")