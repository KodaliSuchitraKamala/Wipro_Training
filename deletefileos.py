import os
file = "new_file.txt"
if os .path.exists(file):
    os.remove(file)
    print(f"{file} deleted.")
else:
    print(f"{file} not found.")