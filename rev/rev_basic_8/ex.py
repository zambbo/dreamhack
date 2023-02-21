ans = "AC F3 0C 25 A3 10 B7 25 16 C6 B7 BC 07 25 02 D5 C6 11 07 C5 00".split(" ")

str_to_byte = lambda x: int(x, 16)

ans = [str_to_byte(x) for x in ans]

flag = ""

for a in ans:
	for c in range(0x00, 0x90, 1):
		if (c * 0xfb) & 0xff == a:
			flag += chr(c)

print(flag)
