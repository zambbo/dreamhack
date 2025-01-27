

arr = [0xDE, 0xAD, 0xBE, 0xEF]

with open("encrypted", "rb") as f:
	encrypted_flag = f.read()

decrypted_flag = bytearray()

for i, en in enumerate(encrypted_flag):
	ch = en - 19
	ch = ch ^ arr[i % 4]
	ch = ch & 0xFF
	decrypted_flag.append(ch)

with open("flag.png", "wb") as f:
	f.write(decrypted_flag)
