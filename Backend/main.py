from model.documents import Document
from iterators.document_iterator import (
    DocumentIterator,
    ReverseDocumentIterator,
    SkipDocumentIterator,
    LimitedDocumentIterator,
    SearchDocumentIterator
)

# Project documents (actual files in files/ folder)
docs = [
    Document("files/Python.txt"),
    Document("files/Geeta.txt"),
    Document("files/Report.docx"),
    Document("files/Notes.txt")
]

# 1. Normal Iterator
print("Normal Iterator:")
for doc in DocumentIterator(docs):
    print(doc.filename)

# 2. Reverse Iterator
print("\nReverse Iterator:")
for doc in ReverseDocumentIterator(docs):
    print(doc.filename)

# 3. Skip Iterator
print("\nSkip Iterator (every 2nd document):")
for doc in SkipDocumentIterator(docs, step=2):
    print(doc.filename)

# 4. Limited Iterator
print("\nLimited Iterator (first 2 documents):")
for doc in LimitedDocumentIterator(docs, limit=2):
    print(doc.filename)

# 5. Search Iterator (keyword 'Python')
print("\nSearch Iterator (keyword='Python'):")
for doc in SearchDocumentIterator(docs, keyword="Python"):
    print(f"{doc.filename} contains 'Python'")
