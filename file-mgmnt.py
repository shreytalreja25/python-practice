import random

try:
    with open("file.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print("ERROR >>> ",e)