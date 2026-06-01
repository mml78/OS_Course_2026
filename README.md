# OS_Course_2026

Marques Leben Michèle
St64039


Asignement 2 :

This program interacts with the Linux file system using Python. It asks the user for a directory path, lists all files in the directory, and displays each file's size and permissions.

Functions used : 

1. os.listdir() = Used to retrieve all entries contained in a directory. --> os.listdir(directory)
2. os.path.isfile() = Used to verify that an entry is a file and not a subdirectory. --> os.path.isfile(file_path)
3. os.stat() = Used to obtain file metadata such as file size. --> os.stat(file_path)
4. os.access() = Used to check file permissions. --> os.access(file_path, os.R_OK)
