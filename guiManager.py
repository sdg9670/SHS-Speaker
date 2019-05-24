from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import time


class MainUI(QtWidgets.QWidget):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAnswerText('')
        self.setQuestionText('')

    def setAnswerText(self, text):
        msg = '<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; color:#ffffff;\">' + text + '</span></p></body></html>'
        self.answer.setText(msg)

    def setQuestionText(self, text):
        self.question.setText(text)


class guiManager():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        mainui = MainUI()
        mainui.show()

        sys.exit(app.exec_())
