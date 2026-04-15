users_name = []

if users_name:
    for name in users_name:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + name + ', thank you for logging in again')
else:
    print("We need to find some users!")

