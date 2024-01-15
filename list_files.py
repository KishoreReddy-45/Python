import os

folders = input("please provide a list of folders:").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide the Valid folder name: " + folder)
        break
    except PermissionError:
        break
        print("No access to this folder: " + folder)

    print("----- listing files for the folder " + folder)

    for file in files:
        print(file)
