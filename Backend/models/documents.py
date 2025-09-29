class Document:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return f"Document: {self.name}"

    def save_to_file(self, path):
        with open(path, 'w') as f:
            f.write(self.content)

    @classmethod
    def load_from_file(cls, path):
        with open(path, 'r') as f:
            content = f.read()
        name = path.split('/')[-1]
        return cls(name, content)
