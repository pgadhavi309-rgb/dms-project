# Step 1: Document class
class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

# Step 2: Iterator class
class DocumentIterator:
    def __init__(self, documents):
        self.documents = documents
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.documents):
            doc = self.documents[self.index]  # yahan self.index use karo
            self.index += 1
            return doc
        else:
            raise StopIteration  # raise karna hota hai

# Step 3: Documents list
docs = [
    Document("Python.txt", "I learn Python"),
    Document("Geeta.txt", "Spiritual knowledge"),
    Document("Report.docx", "Project report content")
]

# Step 4: Iterator use karna
doc_iterator = DocumentIterator(docs)
for doc in doc_iterator:
    print("Title:", doc.title)
