# json module
import json
name = input("Enter your name: ")
age = int(input("Enter your age: "))
data = {"name": name, "age": age}
stringify_json = json.dumps(data) # dumps the data in same page
print("Serialised data of Json ", stringify_json)