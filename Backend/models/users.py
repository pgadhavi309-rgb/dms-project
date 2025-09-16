# backend/users.py
from typing import List, Optional
from backend.models.documents import Document
from backend.helpers.security_helpers import hash_password

class User:
    """
    Basic User model for DMS.
    Stores hashed password (private) and Document objects.
    """
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        # store hashed password (private)
        self.__password = hash_password(password)
        self.documents: List[Document] = []

    def upload_document(self, doc: Document, content: str = "") -> str:
        """Create file (using Document.create) and add Document object to user's list."""
        result = doc.create(content)
        # avoid duplicates: if same filename exists, replace object
        existing = self.get_document(doc.filename)
        if existing:
            # replace existing object with new doc object reference
            idx = self.documents.index(existing)
            self.documents[idx] = doc
        else:
            self.documents.append(doc)
        return f"{doc.filename} uploaded by {self.username} ({result})"

    def list_documents(self) -> List[str]:
        """Return list of filenames owned by user."""
        return [d.filename for d in self.documents]

    def get_document(self, filename: str) -> Optional[Document]:
        """Return Document object by filename or None."""
        for d in self.documents:
            if d.filename == filename:
                return d
        return None

    def read_document(self, filename: str):
        """Return file content via Document.read(), or not-found message."""
        d = self.get_document(filename)
        if not d:
            return f"{filename} not found in {self.username}'s documents."
        return d.read()

    def delete_own_document(self, filename: str) -> str:
        """Delete file from storage and remove from user's list."""
        d = self.get_document(filename)
        if not d:
            return f"{filename} not found in {self.username}'s documents."
        res = d.delete()
        self.documents.remove(d)
        return f"{res} removed from {self.username}'s list."

    def check_password(self, pwd: str) -> bool:
        """Verify password by hashing the provided pwd and comparing."""
        return self.__password == hash_password(pwd)

    def change_password(self, old_pwd: str, new_pwd: str) -> str:
        """Change password if old matches."""
        if not self.check_password(old_pwd):
            return "Old password incorrect."
        self.__password = hash_password(new_pwd)
        return "Password changed successfully."


class AdminUser(User):
    """
    AdminUser inherits User and has additional privileges.
    Admin can delete documents of any user and reset user passwords.
    """
    def __init__(self, username: str, email: str, password: str, permissions: str = "Full Access"):
        super().__init__(username, email, password)
        self.permissions = permissions
        self.is_admin = True

    def delete_document(self, target_user: User, filename: str) -> str:
        """Delete a document from another user (if exists)."""
        d = target_user.get_document(filename)
        if not d:
            return f"{filename} not found in {target_user.username}'s documents."
        res = d.delete()
        target_user.documents.remove(d)
        return f"Admin {self.username} => {res} removed from {target_user.username}'s list."

    def reset_password(self, target_user: User, new_pwd: str) -> str:
        """Reset target user's password (uses name-mangling to set private attr)."""
        hashed = hash_password(new_pwd)
        # name-mangled attribute for User.__password is _User__password
        target_user._User__password = hashed
        return f"Admin {self.username} reset {target_user.username}'s password."

    def view_user_documents(self, target_user: User) -> List[str]:
        """Return target user's document filenames."""
        return target_user.list_documents()
