from backend.helpers.file_helpers import create_file, read_file, write_file, append_file, delete_file

class Document:
    def __init__(self, filename, title=None, author=None):
        self.filename = filename      # file ka naam (required)
        self.title = title            # document title (optional)
        self.author = author          # document author (optional)

    def create(self, content=""):
        """Nayi file create kare with optional content"""
        return create_file(self.filename, content)

    def read(self):
        """File ka content read kare"""
        return read_file(self.filename)

    def update(self, content):
        """File ka purana content replace kare"""
        return write_file(self.filename, content)

    def append(self, content):
        """File me extra content add kare"""
        return append_file(self.filename, content)

    def delete(self):
        """File ko delete kare"""
        return delete_file(self.filename)

    def info(self):
        """Document ka basic info show kare"""
        print(f"Filename: {self.filename}")
        if self.title:
            print(f"Title: {self.title}")
        if self.author:
            print(f"Author: {self.author}")


# 👇 yeh neeche extension classes hai
class WordDocument(Document):
    def open(self):
        return f"Opening Word document: {self.filename}"

class PDFDocument(Document):
    def open(self):
        return f"Opening PDF document: {self.filename}"

class ImageDocument(Document):
    def open(self):
        return f"Opening Image document: {self.filename}"
