class User:
    def __init__(self, username, password):
        self.username = username        # public
        self._email = f"{username}@mail.com"  # protected
        self.__password = password      # private

    def check_password(self, pwd):
        return self.__password == pwd


# child class for accessing protected attribute
class AdminUser(User):
    def show_email(self):
        return self._email


# object
user = User("Pragnesh", "111111")
admin = AdminUser("Pragnesh", "111111")

print(user.username)               # public
print(admin.show_email())          # protected via child
print(user.check_password("111111"))  # private via method
