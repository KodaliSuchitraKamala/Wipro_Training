"""
data = b'This is a sample of binary data'
with open("binary_file.bin", 'wb') as file:
    file.write(data)
"""
with open("binary_file.bin", 'rb') as file:
    content = file.read()
    print(content)