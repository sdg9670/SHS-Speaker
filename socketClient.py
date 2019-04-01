import socket
from threading import Thread
 
HOST = 'simddong.ga'
PORT = 9670

class SocketClient():
    def __init__(self):
        self.sock = None
        
    def rcvMsg(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                with open('log.txt', 'a') as f:
                    f.write(data.decode())
                print(data.decode())
            except:
                pass
    
    def closeSocket(self):
        self.socket.close()
        
    def sndMsg(self, msg):
        self.sock.send(msg.encode())

    def runChat(self):
        self.c_name = '현지 방 스피커'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        t = Thread(target=self.rcvMsg)
        t.daemon = True
        t.start()
        self.sock.send(self.c_name.encode())
