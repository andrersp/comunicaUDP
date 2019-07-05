import socket
import threading

class cliente_UDP(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.ip = input('digite o ip do servidor: ')
        self.addr = ((self.ip,port))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def run(self):
        sendener(self.socket,self.addr)

def sendener(socket,addr):
    mensagem = ''
    while(mensagem != 'sair'):
	    mensagem = input('digite uma mensagem: ')
	    socket.sendto(mensagem.encode(),addr)
	    print ('mensagem enviada')
    else:
	    socket.close()

thread_cliente = cliente_UDP(7000)

thread_cliente.start()


