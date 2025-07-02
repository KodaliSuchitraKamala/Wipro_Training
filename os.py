import os 
folder = input("Enter folder name to create: ")
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' created")
else:
    print("Folder already exists")