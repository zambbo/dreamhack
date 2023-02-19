url = str(input())
try:
	print(url.split('://')[1].split('/')[0].lower().split(":"))
except:
	print("can not parse")
