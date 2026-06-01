import os
import stat

# Ask directory path
directory = input("Enter directory path: ")

# Verify that the folder exist
if not os.path.isdir(directory):
    print("Invalid directory path.")
    exit()

print(f"\nFiles in {directory}:\n")

# Iterate through all entries in the directory
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)

    # Process only files and ignore subdirectories
    if os.path.isfile(file_path):

        # Retrieve file information
        file_stats = os.stat(file_path)
        
        # Get the file size in bytes
        file_size = file_stats.st_size

        # Check file permissions
        permissions = ""
        permissions += "r" if os.access(file_path, os.R_OK) else "-"
        permissions += "w" if os.access(file_path, os.W_OK) else "-"
        permissions += "x" if os.access(file_path, os.X_OK) else "-"

        print(f"File: {file_name}")
        print(f"Size: {file_size} bytes")
        print(f"Permissions: {permissions}")
        print("-" * 30)
