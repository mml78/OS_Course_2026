import os
import stat

# Demande du chemin du dossier
directory = input("Enter directory path: ")

# Vérifie que le dossier existe
if not os.path.isdir(directory):
    print("Invalid directory path.")
    exit()

print(f"\nFiles in {directory}:\n")

# Parcours du dossier
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)

    # Ignore les sous-dossiers
    if os.path.isfile(file_path):

        # Récupération des informations
        file_stats = os.stat(file_path)
        file_size = file_stats.st_size

        # Permissions
        permissions = ""
        permissions += "r" if os.access(file_path, os.R_OK) else "-"
        permissions += "w" if os.access(file_path, os.W_OK) else "-"
        permissions += "x" if os.access(file_path, os.X_OK) else "-"

        print(f"File: {file_name}")
        print(f"Size: {file_size} bytes")
        print(f"Permissions: {permissions}")
        print("-" * 30)
