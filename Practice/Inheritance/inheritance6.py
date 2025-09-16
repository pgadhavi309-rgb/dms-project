class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.documents = []   # user ke documents list me store honge

    def upload_document(self, doc_title):
        self.documents.append(doc_title)
        return f"{doc_title} uploaded by {self.username}"

    def view_documents(self):
        return f"{self.username}'s Documents: {self.documents}"


class AdminUser(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    def delete_document(self, user, doc_title):
        if doc_title in user.documents:
            user.documents.remove(doc_title)
            return f"Admin {self.username} deleted {doc_title} from {user.username}'s documents."
        return f"{doc_title} not found in {user.username}'s documents."


# 🧪 Testing
user1 = User("Pragnesh", "pragnesh@email.com")
admin1 = AdminUser("Himu", "himu@email.com", "Full Access")

print(user1.upload_document("MyNotes.docx"))
print(user1.upload_document("Resume.pdf"))
print(user1.view_documents())

print(admin1.delete_document(user1, "Resume.pdf"))
print(user1.view_documents())
