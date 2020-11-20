import math
import os
import sys

import requests


def myfunction(para1):
    print(para1)


name = input("enter your name ?")
print("ur name is ", name)
print("my name is usman")

print("my name is usman")
h12 = "japan"
print(h12)
myfunction("this is string")
mydit = {"name": "usman", "fathername": "bashir", "sex": "male"}
myfunction(mydit)
r = requests.get("https://python.org")
print(r.status_code)
print(sys.version)
print(sys.executable)
