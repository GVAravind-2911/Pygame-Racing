import threading
import socket
import pickle

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('localhost',3000))

running = True
def send():
	global running
	while running:
		i = input("\nENTER: ")
		sock.send(pickle.dumps(i))
		if i == 'end':
			running = False
			break
	sock.close()

def recv():
	global running
	while running:
		m = pickle.loads(sock.recv(2048))
		if m == 'end':
			running = False
			break
		print('\nRECV:',m)

s = threading.Thread(target = send)
r = threading.Thread(target = recv)

s.start()
r.start()