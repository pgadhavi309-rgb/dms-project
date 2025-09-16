from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, title, uploaded_by):
        self.title = title
        self.uploaded_by = uploaded_by
    @abstractmethod    
    def download(self):
        pass
    @abstractmethod
    def upload(self):
        pass

class ImageDocument(Document):
    def download(self):
        return f"Downloading Image: {self.title}"
    def upload(self):
        return f"Uploading Image: {self.title}"
    
image = ImageDocument("Nature", "Pragnesh")
print(image.download())
print(image.upload())