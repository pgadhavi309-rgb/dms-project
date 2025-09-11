from helpers.file_helpers import create_file, write_file, read_file, append_file
create_file("my_project.txt", "Hello, My name is Pragnesh.\nI am a student.I learn Python.\n")
write_file("my_project.txt", "I love coding.\n")
append_file("my_project.txt", "I love Python.\n")
content = read_file("my_project.txt")
print(content)