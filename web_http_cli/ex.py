import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "host3.dreamhack.games"
PORT = 15058

soc.connect((HOST, PORT))

def recv_until(s: str):
	while True:
		recv = soc.recv(1024)
		print(recv)
		if s in recv:
			return
		
while True:
	recv_until(b"> ")
	data = str(input()).encode()
	soc.send(data)
	print(soc.recv(1024))	
