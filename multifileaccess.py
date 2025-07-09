with open('File.txt', 'r') as file1, open('File2.txt', 'r') as file2:
    content1 = file1.read()
    content2 = file2.read()
    print("Data of file1: ")
    print(content1)
    print("Data of file2: ")
    print(content2)
    file1.close()
    file2.close()