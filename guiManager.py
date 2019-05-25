from ui import mainUi
from multiprocessing import Process, Pipe
import ui.mainUi

class GuiManager():
    def __init__(self):
        self.main_pc, self.main_cc = Pipe()
        p = Process(target=ui.mainUi.MainUI, args=(self.main_cc,))
        p.start()
        p.join()


    def setMainAnswerText(self, text):
            self.main_pc.send(('setAnswerText\t' + text).encode())
    def setMainQuestionText(self, text):
            self.main_pc.send(('setQuestionText\t' + text).encode())s