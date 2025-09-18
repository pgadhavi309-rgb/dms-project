import os

def create_file(filepath, content=""):
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"{filepath} successfully created."
    except Exception as e:
        return f"Error creating file {filepath}: {e}"

def read_file(filepath):
    if not os.path.exists(filepath):
        return f"{filepath} does not exist."
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def write_file(filepath, content):
    if not os.path.exists(filepath):
        return f"{filepath} does not exist."
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return f"{filepath} me naya content likh diya gaya hai."

def append_file(filepath, content):
    if not os.path.exists(filepath):
        return f"{filepath} does not exist."
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n" + content)
    return f"{filepath} me content successfully append ho gaya hai."

def delete_file(filepath):
    if not os.path.exists(filepath):
        return f"{filepath} does not exist."
    os.remove(filepath)
    return f"{filepath} successfully delete ho gayi hai."
