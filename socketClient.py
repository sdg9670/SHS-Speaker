# -*- coding: utf-8 -*-
import socket
from threading import Thread
import queue
import json
import time

HOST = 'simddong.ga'
PORT = 9670


class SocketClient():
    def __init__(self, programs):
        self.sock = None
        self.msg = queue.Queue()
        self.alarm = programs['alarm']
        self.gui = programs['guiClient']



    def rcvMsg(self):
        long_data = ''
        while True:
            data = b''
            while True:
                part = self.sock.recv(1024)
                data += part
                if len(part) < 1024:
                    break
                else:
                    time.sleep(0.05)
            if not data:
                break
            data = data.decode('utf-8')
            split_data = data.split('\t')
            if split_data[0] == "server":
                if split_data[1] == "msg":
                    if split_data[2] == "weathertoday":
                        m = split_data[3]
                        self.gui.sndMsg('setTodayWeather\t' + split_data[4])
                        self.msg.put('a\t' + m)
                        print(split_data[4])
                    elif split_data[2] == "weathertommorow":
                        m = split_data[3]
                        self.gui.sndMsg('setTomorrowWeather\t' + split_data[4])
                        self.msg.put('a\t' + m)
                        print(split_data[4])
                    elif split_data[2] == "weatheraftertommorow":
                        m = split_data[3]
                        self.gui.sndMsg('setAfterTomorrowWeather\t' + split_data[4])
                        self.msg.put('a\t' + m)
                        print(split_data[4])
                    else:
                        self.msg.put(split_data[2] + '\t' + split_data[3])
                elif split_data[1] == "getalarm":
                    self.alarm.setAlarmList(json.loads(split_data[2]))

    def getMsg(self):
        return self.msg.get(block=True)

    def closeSocket(self):
        self.socket.close()

    def sndMsg(self, msg):
        self.sock.send(('speaker\t'+msg).encode('utf-8'))

    def runChat(self):
        self.c_name = '1'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        t = Thread(target=self.rcvMsg)
        t.daemon = True
        t.start()
        self.sock.send(self.c_name.encode('utf-8'))
