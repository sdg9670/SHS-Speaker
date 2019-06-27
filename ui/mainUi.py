# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QLayout, QGridLayout
import sys
import ui.todayUi as todayUi
import ui.tomorrowUi as tomorrowUi
import ui.afterTomorrowUi as afterTomorrowUi
import ast

class MainUI(QtWidgets.QWidget):
    def __init__(self, cc):
        app = QApplication(sys.argv)
        super(MainUI, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.cc = cc
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

        self.todayUi = todayUi.todayUi()
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.todayUi)
        self.todayUi.hide()

        self.tomorrowUi = tomorrowUi.tomorrowUi()
        layout.addWidget(self.tomorrowUi)
        self.tomorrowUi.hide()

        self.afterTomorrowUi = afterTomorrowUi.afterTomorrowUi()
        layout.addWidget(self.afterTomorrowUi)
        self.afterTomorrowUi.hide()

        self.setAnswerText('')
        self.setQuestionText('')

        self.pt = pipeThread(self, self.cc)
        self.pt.start()
        sys.exit(app.exec_())

    def paintEvent(self, event):
        pass

    def setAnswerText(self, text):
        msg = '<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; color:#ffffff;\">' + text + '</span></p></body></html>'
        self.answer.setText(msg)

    def setQuestionText(self, text):
        msg = '<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; color:#ffffff;\">' + text + '</span></p></body></html>'
        self.question.setText(msg)
        self.question.show()

        self.todayUi.hide()
        self.tomorrowUi.hide()
        self.afterTomorrowUi.hide()

    def setTodayWeather(self, text):
        self.todayUi.setUi(ast.literal_eval(text))
        self.todayUi.show()

        self.question.hide()

    def setTomorrowWeather(self, text):
        self.tomorrowUi.setUi(ast.literal_eval(text))
        self.tomorrowUi.show()

        self.question.hide()

    def setAfterTomorrowWeather(self, text):
        self.afterTomorrowUi.setUi(ast.literal_eval(text))
        self.afterTomorrowUi.show()

        self.question.hide()

class pipeThread(QtCore.QThread):
    def __init__(self, main, cc):
        QtCore.QThread.__init__(self)
        self.main = main
        self.cc = cc

    def run(self):
        while True:
            print('main 대기')
            msg = self.cc.recv().decode()
            print('main 받음' + msg)
            msg = msg.split('\t')

            if len(msg) == 1:
                msg.append(' ')
            print('msg ' + str(msg))
            if msg[0] == 'setAnswerText':
                self.main.setAnswerText(msg[1])
            elif msg[0] == 'setQuestionText':
                self.main.setQuestionText(msg[1])
            elif msg[0] == 'setTodayWeather':
                self.main.setTodayWeather(msg[1])
            elif msg[0] == 'setTomorrowWeather':
                self.main.setTomorrowWeather(msg[1])
            elif msg[0] == 'setAfterTomorrowWeather':
                self.main.setAfterTomorrowWeather(msg[1])
