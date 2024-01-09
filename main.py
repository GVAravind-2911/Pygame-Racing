import threading
import socket
import pickle

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('',3000))
sock.listen()
print('listening for connection')
buddy, addr = sock.accept()
print('connected successfully to',addr)
running = True
def send():
	global running
	while running:
		i = input("ENTER: ")
		buddy.send(pickle.dumps(i))
		if i == 'end':
			running = False
			break
	buddy.close()

def recv():
	global running
	while running:
		m = pickle.loads(buddy.recv(2048))
		if m == 'end':
			running = False
		print('RECV:',m)
	sock.close()

s = threading.Thread(target = send)
r = threading.Thread(target = recv)

s.start()
r.start()