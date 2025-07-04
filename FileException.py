try:
    file = open("File1.txt")
    str = file.readline()
    print(str)
    file = open("File.txt")
    str = file.readline()
    print(str)
except IOError:
    print("Error occured during input take......")
else:
    print("Successfully fetch the data......")