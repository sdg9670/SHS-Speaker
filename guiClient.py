# -*- coding: utf-8 -*-
import socket
from threading import Thread

HOST = 'localhost'
PORT = 9671


class GuiClient():
    def __init__(self):
        self.sock = None


    def closeSocket(self):
        self.socket.close()

    def sndMsg(self, msg):
        self.sock.send((msg).encode())

    def runChat(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
