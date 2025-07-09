"""
with open('File.txt', 'r+') as file:
    content = file.read()
    file.seek(0)
    file.write("Modification done here")
"""
with open('File.txt', 'a+') as file:
    file.write('\n Appended Data')
    file.seek(0)
    print(file.read())