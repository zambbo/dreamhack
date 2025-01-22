def decode(encoded_ptr: bytes, table: bytes) -> bytes:
    reverse_table = {value: index for index, value in enumerate(table)}
    print("Reverse table:", reverse_table)
    
    decoded = bytearray()
    cs = 0
    while cs < len(encoded_ptr):
        if encoded_ptr[cs] == 61:
            break

        try:
            a = reverse_table[encoded_ptr[cs]] << 2
            b = reverse_table[encoded_ptr[cs+1]]
            decoded.append(a | (b >> 4))
            
            if cs + 2 < len(encoded_ptr) and encoded_ptr[cs+2] != 61:
                c = reverse_table[encoded_ptr[cs+2]]
                decoded.append(((b & 0xF) << 4) | (c >> 2))
            if cs + 3 < len(encoded_ptr) and encoded_ptr[cs+3] != 61:
                d = reverse_table[encoded_ptr[cs+3]]
                decoded.append(((c & 0x3) << 6) | d)
        except KeyError as e:
            print(f"Error: Encoded character {encoded_ptr[cs]} not in reverse table")
            break

        cs += 4
    return bytes(decoded)

with open("flag_out.txt", "rb") as f:
    encoded_ptr = f.read()
with open("table.new", "rb") as f:
    table = f.read()

decoded_flag = decode(encoded_ptr, table)
print("Decoded flag (string):", decoded_flag.decode('utf-8', errors='replace'))

