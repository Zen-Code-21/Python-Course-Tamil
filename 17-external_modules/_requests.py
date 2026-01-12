import requests

r = requests.get('https://api.github.com/users/zen')
# print(r.text)

with open("zen.txt", "w") as f:
    f.write(r.text)


