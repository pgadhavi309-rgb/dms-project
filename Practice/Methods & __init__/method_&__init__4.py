class Book:
    def __init__(self, title, author, pages = "unknown"):
        self.title = title
        self.author = author
        self.pages = pages
    
    def info(self):
        print("Title:", self.title, "Author:", self.author, "Pages:", self.pages)

b1 = Book("Geeta", "Vedvyas")
b2 = Book("Samadhi", "Osho", 100)
b1.info()
b2.info()