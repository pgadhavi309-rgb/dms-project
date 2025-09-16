class Document:
    def download(self):
        return "Checking access..."
    
class WordDocument(Document):
    def download(self):
        perent_msg = super().download()
        return f"{perent_msg}, Downloading Word content..."
    
word = WordDocument()
print(word.download())