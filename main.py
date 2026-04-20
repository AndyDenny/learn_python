active = True
answers = {}

while active:
    user_name = input("What is your name? ")
    user_country = input("Which country would you like to travel someday? ")
    proceed = input("Would you like to let another person respond? (y/n) ")

    answers[user_name.title()] = user_country.title()

    if proceed == "n":
        active = False

print("__Pool is finished!__")
for key, value in answers.items():
    print(key + " want's travel to " + value)

