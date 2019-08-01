# -*- coding: utf-8 -*-
from ui import mainUi
from multiprocessing import Process, Pipe
import ui.mainUi
import threading
import socket
import time

class GuiManager():
    def __init__(self):
        self.server = Server(self)
        self.server.start()
        self.main_pc, self.main_cc = Pipe()
        p = Process(target=ui.mainUi.MainUI, args=(self.main_cc,))
        p.start()
        p.join()


    def setMainAnswerText(self, text):
            self.main_pc.send(('setAnswerText\t' + text).encode())

    def setMainQuestionText(self, text):
            self.main_pc.send(('setQuestionText\t' + text).encode())

    def setTodayWeather(self, text):
            self.main_pc.send(('setTodayWeather\t' + text).encode())

    def setTomorrowWeather(self, text):
            self.main_pc.send(('setTomorrowWeather\t' + text).encode())

    def setAfterTomorrowWeather(self, text):
            self.main_pc.send(('setAfterTomorrowWeather\t' + text).encode())


class Server(threading.Thread):
    def __init__(self, gui):
        self.gui = gui
        threading.Thread.__init__(self)

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", 9671))
        server_socket.listen(5)

        print("TCPServer Waiting for client on port 9671")
        while True:
            client_socket, address = server_socket.accept()
            print("I got a connection from ", address)
            while True:
                try:
                    data = b''
                    while True:
                        part = client_socket.recv(1024)
                        data += part
                        if len(part) < 1024:
                            break
                    data = data.decode()
                    print('gui 받음' + data)
                    if '\r' in data:
                        sp = data.split('\r')
                        for data in sp:
                            data = data.split('\t')
                            if len(data) == 1:
                                data.append(' ')
                            if data[0] == 'setMainAnswerText':
                                self.gui.setMainAnswerText(data[1])
                            elif data[0] == 'setMainQuestionText':
                                self.gui.setMainQuestionText(data[1])
                            elif data[0] == 'setTodayWeather':
                                self.gui.setTodayWeather(data[1])
                            elif data[0] == 'setTomorrowWeather':
                                self.gui.setTomorrowWeather(data[1])
                            elif data[0] == 'setAfterTomorrowWeather':
                                self.gui.setAfterTomorrowWeather(data[1])
                            time.sleep(0.05)
                except Exception as e:
                    print("클라이언트 종료")
                    client_socket.close()
                    break
        server_socket.close()
        print("SOCKET closed... END")

GuiManager()
