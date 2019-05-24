import socket
from threading import Thread
import queue
import json

HOST = 'simddong.ga'
PORT = 9670


class SocketClient():
    def __init__(self, programs):
        self.sock = None
        self.msg = queue.Queue()
        self.alarm = programs['alarm']

    def rcvMsg(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            data = data.decode()
            with open('log.txt', 'a') as f:
                f.write(data)
            split_data = data.split('\t')
            if split_data[0] == "server":
                if split_data[1] == "msg":
                    self.msg.put(split_data[2] + '\t' + split_data[3])
                elif split_data[1] == "getalarm":
                    self.alarm.setAlarmList(json.loads(split_data[2]))

    def getMsg(self):
        return self.msg.get(block=True)

    def closeSocket(self):
        self.socket.close()

    def sndMsg(self, msg):
        self.sock.send(('speaker\t'+msg).encode())

    def runChat(self):
        self.c_name = '1'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        t = Thread(target=self.rcvMsg)
        t.daemon = True
        t.start()
        self.sock.send(self.c_name.encode())
