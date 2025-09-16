class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
class NormalUser(User):
    def __init__(self, username, email, storage_limit):
        super().__init__(username, email)
        self.storage_limit = storage_limit

info = NormalUser("Pragnesh", "pragnesh@email.com", "512GB")
print(info.username, info.email, info.storage_limit)