from User import User 


class Admin(User):

    def __init__(self):
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей" ]

    def show_privileges(self):
        return self.privileges

