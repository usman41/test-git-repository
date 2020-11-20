import requests

mydit = {"name": "usman", "fathername": "bashir", "sex": "male"}
r = requests.get("https://python.org")
print(r.status_code)
