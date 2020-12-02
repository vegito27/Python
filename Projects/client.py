import socket 


PORT=5050

HEADER=64

SERVER="192.168.43.223"


DISCONNECT_MESSAGE='!DISCONNECT'

ADDR=(SERVER,PORT)

FORMAT='utf-8'

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
	message=msg.encode(FORMAT)
	msg_length=len(message)
	send_length=str(msg_length).encode(FORMAT)
	send_length +=b' ' * (HEADER-len(send_length))
	client.send(send_length)
	client.send(message)


send("Hello")