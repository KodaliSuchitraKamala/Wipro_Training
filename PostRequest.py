import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title" : "Hi Students",
    "body" : "Wipro Geeks",
    "userID" : 1
}
response = requests.post(url, json = data)
print("Status Code: ", response.status_code)
print("Reponse JSON: ",response.json())