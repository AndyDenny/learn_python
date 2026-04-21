def show_magicians(wizzard_list):
    for wizzard in wizzard_list:
        print("Hello " + wizzard.title() + "!")

wizzards = ["Sandy", "Mandy", "Vandy"]
show_magicians(wizzards)