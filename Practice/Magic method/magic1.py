class Document:
    def __init__(self, title, content):
        self.__title = title
        self.__content = content

    def __str__(self):
        return f"{self.__title} of {self.__content}"
    
    def __repr__(self):
        return f"Document(title='{self.__title} content={self.__content}')"
    
    def __eq__(self, other):
        return self.__content == other.__content
    
    def __add__(self, other):
        
        new_title = self.__title + " & " + other.__title
        new_content = self.__content + " " + other.__content
        return Document(new_title, new_content)

    
    def __len__(self):
        return len(self.__content)
    
    

a = Document("Coding", "I learn coding")
b = Document("Geeta", "Geeta sloka")
c = Document("Python", "I learn coding")
print(a)
print(len(a))
print(a == c)
print(a + b)
d = a + b
print(d)
print(repr(a))
        