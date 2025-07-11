import os
file = "sysmodule.txt"
if os.path.exists(file):
    size = os.path.getsize(file)
    print(f"{file} size: {size} bytes.")
else:
    print("file not found.")