import requests

mydit = {"name": "usman", "lastname": "khan", "sex": "male"}
r = requests.get("https://python.org")
print(r.status_code)
