import requests, json

BASE = "http://127.0.0.1:5000/"
headers = {'Content-Type': 'application/json'}

data = {"likes": 10, "name": "Lorem Ipsum", "views": 30145}  # Data to be sent in JSON format
json_data = json.dumps(data)

response = requests.post(BASE + "video/1", data = json_data, headers=headers )
print(response.json())