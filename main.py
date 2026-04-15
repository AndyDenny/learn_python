current_users = ["Andy", "Sandy", "admin" ,"Mandy", "Vendy"]
new_users = ["Jack", "John", "Mandy", "Sara", "Vendy"]

for user in new_users:
    if user in current_users:
        print('User - ' + user + ' already exist')
    else:
        print('Username - ' + user + ' is free')

