"""
with open('File.txt','r') as file:
    lines = file.readlines()
print("List of lines: ", lines)

with open('File.txt','r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

with open('File.txt', 'r') as file:
    seperate_lines = [line.strip() for line in file. readlines()]
    print(seperate_lines)

# close() - manually
"""
file = open('File.txt', 'r')
print(file.closed)
file.close()
print(file.closed)
