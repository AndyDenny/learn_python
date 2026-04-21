def make_great(wizzard_list):
    for i in range(len(wizzard_list)):
        wizzard_list[i] = "Great " + wizzard_list[i]
    return wizzard_list



wizzards = ["Sandy", "Mandy", "Vandy"]
print(make_great(wizzards)) 