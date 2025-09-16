# helpers/file_helpers.py
"""
File helper functions with proper error handling (try/except + context managers)
"""
import os


def create_file(file_name, content=""):
    """Create or overwrite file with content"""
    try:
        # 👇 ensure parent folder exists
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
        return f"{file_name} created successfully!"
    except Exception as e:
        return f"Error creating file {file_name}: {e}"


def read_file(file_name):
    """Return file content or a message if not exists"""
    try:
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                return f.read()
        else:
            return f"{file_name} does not exist."
    except Exception as e:
        return f"Error reading file {file_name}: {e}"


def write_file(file_name, content):
    """Overwrite file with content"""
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
        return f"{file_name} me naya content likh diya gaya hai."
    except Exception as e:
        return f"Error writing to file {file_name}: {e}"


def append_file(file_name, content):
    """Append content to file"""
    try:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(content)
        return f"{file_name} me content successfully append ho gaya hai."
    except Exception as e:
        return f"Error appending to file {file_name}: {e}"


def delete_file(file_name):
    """Delete file if exists"""
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            return f"{file_name} successfully delete ho gayi hai."
        else:
            return f"{file_name} exist nahi karti."
    except Exception as e:
        return f"Error deleting file {file_name}: {e}"
