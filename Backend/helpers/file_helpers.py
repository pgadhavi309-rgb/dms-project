import os
import shutil
from datetime import datetime

# ---------------- Basic File Helpers ----------------

def ensure_folder(folder_path):
    folder_path = os.path.abspath(folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
        print(f"{folder_path} folder create kar diya gaya.")
    else:
        print(f"{folder_path} already exist karta hai.")
    return folder_path

def create_file(filepath, content=""):
    folder = os.path.dirname(filepath)
    if folder:
        ensure_folder(folder)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{filepath} successfully created.")

def append_to_file(filepath, content):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n" + content)
    print(f"{filepath} me content successfully append ho gaya hai.")

def overwrite_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{filepath} me naya content likh diya gaya.")

def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"{filepath} successfully deleted.")
    else:
        print(f"{filepath} exist nahi karta.")

def delete_folder(folderpath):
    if os.path.exists(folderpath):
        shutil.rmtree(folderpath)
        print(f"{folderpath} folder aur uske sabhi files delete ho gaye.")
    else:
        print(f"{folderpath} exist nahi karta.")

def list_files_with_sizes(folderpath):
    if os.path.exists(folderpath):
        files = os.listdir(folderpath)
        for f in files:
            filepath = os.path.join(folderpath, f)
            if os.path.isfile(filepath):
                size = os.path.getsize(filepath)
                print(f"{f} - {size} bytes")
    else:
        print(f"{folderpath} exist nahi karta.")

def file_metadata(filepath):
    if os.path.exists(filepath):
        stats = os.stat(filepath)
        print(f"📄 Metadata for: {filepath}")
        print(f"   Size: {stats.st_size} bytes")
        print(f"   Last Modified: {datetime.fromtimestamp(stats.st_mtime)}")
        print(f"   Created: {datetime.fromtimestamp(stats.st_ctime)}")
    else:
        print(f"{filepath} exist nahi karta.")

# ---------------- Advanced Helpers ----------------

def backup_file(src, dest_folder="backend/backup"):
    if not os.path.exists(src):
        return f"{src} does not exist."
    dest_folder = ensure_folder(dest_folder)
    base = os.path.basename(src)
    name, ext = os.path.splitext(base)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_file = os.path.join(dest_folder, f"{name}_{timestamp}{ext}")
    shutil.copy2(src, dest_file)
    print(f"Backup created: {dest_file}")
    return dest_file

def get_file_info(filepath):
    if not os.path.exists(filepath):
        return f"{filepath} does not exist."
    size = os.path.getsize(filepath)
    mtime = os.path.getmtime(filepath)
    last_modified = datetime.fromtimestamp(mtime).strftime("%d-%m-%Y %H:%M:%S")
    return {
        "path": filepath,
        "size_bytes": size,
        "last_modified": last_modified
    }

# ---------------- File Organize Helpers ----------------

def move_file_to_archive(src_file, archive_folder="backend/archive"):
    if not os.path.exists(src_file):
        return f"{src_file} does not exist."
    archive_folder = ensure_folder(archive_folder)
    base = os.path.basename(src_file)
    name, ext = os.path.splitext(base)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_file = os.path.join(archive_folder, f"{name}_{timestamp}{ext}")
    shutil.move(src_file, dest_file)
    print(f"{src_file} moved to {dest_file}")
    return dest_file

def copy_file_to_backup(src_file, backup_folder="backend/backup"):
    if not os.path.exists(src_file):
        return f"{src_file} does not exist."
    backup_folder = ensure_folder(backup_folder)
    base = os.path.basename(src_file)
    name, ext = os.path.splitext(base)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_file = os.path.join(backup_folder, f"{name}_{timestamp}{ext}")
    shutil.copy2(src_file, dest_file)
    print(f"{src_file} copied to {dest_file}")
    return dest_file
