#-*- coding:utf-8 -*-
#!/usr/bin/env python

import googleSTT
import naverTTS
import socketClient
import os
import alarmProgram
import guiManager

class Main:
    def __init__(self):
        self.programs = {}
        self.gstt = googleSTT.GoogleSTT()
        self.ntts = naverTTS.NaverTTS()


        self.programs['alarm'] = alarmProgram.AlarmProgram()
        self.programs['gui'] = guiManager.GuiManager()
        self.sc = socketClient.SocketClient(self.programs)


    def start(self):
        self.sc.runChat()

        self.sc.sndMsg('getalarm')
        self.programs['alarm'].start()

        step = 0
        while True:
            # 음성 인식 될때까지 대기 한다.
            #self.programs['gui'].setMainQuestionText('')
            stt = self.gstt.getText()
            if stt is None:
                break
            else:
                #self.programs['gui'].setMainQuestionText(stt)
                print('나: ' + str(stt))
                if step == 0 and '안녕 다솜' in stt.strip():
                    #self.programs['gui'].setMainAnswerText('말씀하세요.')
                    self.gstt.pauseMic()
                    #self.ntts.play('말씀하세요.')
                    self.gstt.restartMic()
                    #self.programs['gui'].setMainAnswerText('')
                    step = 1
                elif step == 1:
                    self.sc.sndMsg('nal\t12345\t' + stt.strip())
                    self.gstt.pauseMic()
                    msg = self.sc.getMsg()
                    msg_sp = msg.split('\t')
                    print(msg_sp[1])
                    #self.programs['gui'].setMainAnswerText(msg_sp[1])
                    self.ntts.play(msg_sp[1])
                    self.gstt.restartMic()
                    #self.programs['gui'].setMainAnswerText('')
                    if msg_sp[0] == 'q':
                        step = 1
                    else:
                        step = 0

if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/shs_key.json"
    main = Main()
    main.start()
