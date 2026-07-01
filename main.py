class User:
    def __init__(self, first_name, last_name, email, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.birthday}, {self.email}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")


class Admin(User):

    def __init__(self):
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей" ]

    def show_privileges(self):
        return self.privileges


admin = Admin()
print(admin.privileges.show_privileges())
