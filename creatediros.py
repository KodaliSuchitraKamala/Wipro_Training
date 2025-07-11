import os
folder = "Wipro_Practice"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' created.")
else:
    print(f"Folder '{folder}' already exists.")