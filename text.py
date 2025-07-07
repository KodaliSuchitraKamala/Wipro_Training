"""
file = open('File.txt', "rb")
print(file)
with open('File.txt', "r") as file:
    content = file.read()
    print(content)
with open('File.txt', "w") as file:
    file.write("Wipro, TCS, Capgemini \n")
    file.write("Google, Microsoft, CAT \n")
    file.write("Tech Mahindra, L&T, HCL \n")
"""
with open('File.txt', "a") as file:
    file.write("This is the appended data \n")