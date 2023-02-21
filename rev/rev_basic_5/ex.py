
encrypted = "AD D8 CB CB 9D 97 CB C4 92 A1 D2 D7 D2 D6 A8 A5 DC C7 AD A3 A1 98 4C 00".split(" ")

str_to_byte = lambda x: int(x, 16)

encrypted = [str_to_byte(x) for x in encrypted]

print(encrypted)

cur = 0x4c

encrypted = encrypted[:-2]

flag = chr(cur)

for e in encrypted[::-1]:
	x = (e - cur) & 0xff
	cur = x
	flag = chr(cur) + flag

print(flag)
