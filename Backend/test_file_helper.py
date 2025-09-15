# tests/test_file_helpers.py
from helpers.file_helpers import (
    create_file,
    read_file,
    write_file,
    append_file,
    delete_file
)

def run_tests():
    file_name = "demo.txt"

    # 1. Create file
    create_file(file_name, "Hello, this is the first line.\n")

    # 2. Read file
    print("File Content (after create):")
    print(read_file(file_name))

    # 3. Write (overwrite) file
    write_file(file_name, "This content replaced the old one.\n")

    # 4. Read file again
    print("File Content (after write):")
    print(read_file(file_name))

    # 5. Append new content
    append_file(file_name, "This line is appended.\n")

    # 6. Read file again
    print("File Content (after append):")
    print(read_file(file_name))

    # 7. Delete file
    delete_file(file_name)

    # 8. Try to read deleted file
    print("File Content (after delete):")
    print(read_file(file_name))


if __name__ == "__main__":
    run_tests()
