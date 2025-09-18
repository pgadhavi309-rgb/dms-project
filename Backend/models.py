# backend/models.py

class Document:
    def __init__(self, title, content):
        self.__title = title
        self.__content = content

    def __str__(self):
        return f"Document: {self.__title}"  # user-friendly

    def __repr__(self):
        return f"Document(title='{self.__title}', content='{self.__content}')"  # developer-friendly

    def __len__(self):
        return len(self.__content)

    def __eq__(self, other):
        return self.__title == other.__title

    def __add__(self, other):
        new_title = self.__title + " & " + other.__title
        new_content = self.__content + " " + other.__content
        return Document(new_title, new_content)

    def __gt__(self, other):
        return len(self.__content) > len(other.__content)

    def __lt__(self, other):
        return len(self.__content) < len(other.__content)


class ProjectMember:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def __str__(self):
        return f"{self.__name} is a {self.__role}"  # user-friendly

    def __repr__(self):
        return f"ProjectMember(name='{self.__name}', role='{self.__role}')"  # developer-friendly

    def __eq__(self, other):
        return self.__role == other.__role

    def __len__(self):
        return len(self.__role)
