

encrypted = "24 27 13 C6 C6 13 16 E6  47 F5 26 96 47 F5 46 27 13 26 26 C6 56 F5 C3 C3 F5 E3 E3 00 00 00 00 00".split()
str_hex_to_byte = lambda x: int(x, 16)
encrypted = [str_hex_to_byte(x) for x in encrypted]

print(encrypted)

process = lambda x: ((x & 0xf0) >> 4) | ((x & 0x7) << 4 )

processed = [process(x) for x in encrypted]
print("".join([chr(x) for x in processed]))
