from backend.helpers.file_helpers import create_file, read_file, write_file, append_file, delete_file
from backend.helpers.logging_decorator import log_method

class Document:
    def __init__(self, filename, title=None, author=None):
        self.filename = filename
        self.title = title
        self.author = author

    @log_method
    def create(self, content=""):
        return create_file(self.filename, content)

    @log_method
    def read(self):
        return read_file(self.filename)

    @log_method
    def update(self, content):
        return write_file(self.filename, content)

    @log_method
    def append(self, content):
        return append_file(self.filename, content)

    @log_method
    def delete(self):
        return delete_file(self.filename)

    @log_method
    def info(self):
        return {"filename": self.filename, "title": self.title, "author": self.author}


class WordDocument(Document):
    @log_method
    def open(self):
        return f"Opening Word document: {self.filename}"

class PDFDocument(Document):
    @log_method
    def open(self):
        return f"Opening PDF document: {self.filename}"

class ImageDocument(Document):
    @log_method
    def open(self):
        return f"Opening Image document: {self.filename}"
