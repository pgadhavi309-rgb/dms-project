from backend.helpers.file_helpers import create_file, read_file, write_file, append_file, delete_file

class Document:
    def __init__(self, filename):
        self.filename = filename

    def create(self, content=""):
        return create_file(self.filename, content)

    def read(self):
        return read_file(self.filename)

    def update(self, content):
        return write_file(self.filename, content)

    def append(self, content):
        return append_file(self.filename, content)

    def delete(self):
        return delete_file(self.filename)
