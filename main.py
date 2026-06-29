class User:
    def __init__(self, first_name, last_name, email, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.birthday}, {self.email}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")


user1 = User("John", "Doe", "John@doe.com", "2010-10-10")
user2 = User("Michael", "Jackson", "Michael@jackson.com", "2009-09-09")
user3 = User("Sara", "Connor", "Sara@connor.com", "2008-08-08")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

