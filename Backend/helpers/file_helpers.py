# helpers/file_helpers.py
"""
File helper functions (safe, using context managers)
"""
import os

def create_file(file_name, content=""):
    """Create or overwrite file with content"""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{file_name} created successfully!")

def read_file(file_name):
    """Return file content or a message if not exists"""
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    return f"{file_name} does not exist."

def write_file(file_name, content):
    """Overwrite file with content"""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{file_name} me naya content likh diya gaya hai.")

def append_file(file_name, content):
    """Append content to file"""
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(content)
    print(f"{file_name} me content successfully append ho gaya hai.")

def delete_file(file_name):
    """Delete file if exists"""
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} successfully delete ho gayi hai.")
    else:
        print(f"{file_name} exist nahi karti.")
