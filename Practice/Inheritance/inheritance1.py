class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_details(self):
        return f"Username: {self.username}, Email: {self.email}"
    
class AdminUser(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions
    
    def get_details(self):
        return f"[Admin] {self.username}, Permissions: {self.permissions}"
    
admin = AdminUser("Pragnesh", "pragnesh@email.com", "Full Access")
print(admin.get_details())