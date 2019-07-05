import socket
import threading

class servidor_UDP(threading.Thread):
	def __init__(self, port):
		threading.Thread.__init__(self)
		self.host = ''
		self.addr = ((self.host,port))
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.socket.bind(self.addr)
	def run(self):
		listenner(self.socket)

def listenner(socket):
	con = socket
	print ('conectado...')
	mensagem = ''
	while(mensagem != 'sair'):
		print ('aguardando mensagem')
		mensagem, cliente = con.recvfrom(1024)
		mensagem = mensagem.decode('ascii')
		print (mensagem)
	else:
		socket.close()

thread_servidor = servidor_UDP(7000)

thread_servidor.start()

