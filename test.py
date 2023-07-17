import requests

BASE = "http://127.0.0.1:5000/"

responce = requests.get(BASE + "helloworld/bill")
print(responce.json())
