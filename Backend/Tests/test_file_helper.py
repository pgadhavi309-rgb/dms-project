from backend.helpers.file_helpers import *

# ---------------- Test Folders ----------------
ensure_folder("backend/files")
ensure_folder("backend/backup")
ensure_folder("backend/archive")

# ---------------- Test Files ----------------
create_file("backend/files/test1.txt", "Hello Himu!")
create_file("backend/files/test2.txt", "Python Project Test")

append_to_file("backend/files/test1.txt", "Second line added.")
overwrite_file("backend/files/test2.txt", "This content is overwritten.")

# ---------------- List Files ----------------
print("\nListing all files with sizes in 'backend/files':")
list_files_with_sizes("backend/files")

# ---------------- Metadata ----------------
print("\nMetadata for test1.txt:")
file_metadata("backend/files/test1.txt")

# ---------------- Backup & Archive ----------------
backup_file("backend/files/test1.txt")
copy_file_to_backup("backend/files/test2.txt")
move_file_to_archive("backend/files/test1.txt")

# ---------------- File Info ----------------
info = get_file_info("backend/files/test2.txt")
print("\nFile Info dict:", info)

print("\nAll ultimate file_helpers functions tested successfully!")
