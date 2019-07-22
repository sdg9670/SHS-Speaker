#-*- coding:utf-8 -*-
#!/usr/bin/env python

import googleSTT
import naverTTS
import socketClient
import os
import alarmProgram
import guiClient

class Main:
    def __init__(self):
        programs = {}
        programs['gstt'] = googleSTT.GoogleSTT()
        programs['ntts'] = naverTTS.NaverTTS()
        self.gstt = programs['gstt']
        self.ntts = programs['ntts']

        programs['alarm'] = alarmProgram.AlarmProgram(programs)
        self.alarm = programs['alarm']

        programs['guiClient'] = guiClient.GuiClient()
        self.guiClient = programs['guiClient']
        self.guiClient.runChat()


        self.sc = socketClient.SocketClient(programs)


    def start(self):
        self.sc.runChat()

        self.sc.sndMsg('getalarm')
        self.alarm.start()

        step = 0
        while True:
            # 음성 인식 될때까지 대기 한다.
            self.guiClient.sndMsg('setMainQuestionText\t' + '   ')
            stt = self.gstt.getText()
            if stt is None:
                continue
            else:
                self.guiClient.sndMsg('setMainQuestionText\t' + stt)
                print('나: ' + str(stt))
                if step == 0 and ('안녕 다솜' in stt.strip() or '안녕 바보' in stt.strip() or '안녕 다소' in stt.strip()):
                    self.guiClient.sndMsg('setMainAnswerText\t' + '말씀하세요.')
                    self.gstt.pauseMic()
                    self.ntts.play('말씀하세요.')
                    self.gstt.restartMic()
                    self.guiClient.sndMsg('setMainAnswerText\t' + ' ')
                    step = 1
                elif step == 0 and ('도와줘 다솜' in stt.strip()):
                    self.sc.sndMsg('help')
                    msg = self.sc.getMsg()
                    msg_sp = msg.split('\t')
                    print(msg_sp[1])
                    self.guiClient.sndMsg('setMainAnswerText\t' + msg_sp[1])
                    self.ntts.play(msg_sp[1])
                    self.gstt.restartMic()
                    self.guiClient.sndMsg('setMainAnswerText\t' + ' ')
                elif step == 1:
                    self.sc.sndMsg('nal\t12345\t' + stt.strip())
                    self.gstt.pauseMic()
                    msg = self.sc.getMsg()
                    msg_sp = msg.split('\t')
                    print(msg_sp[1])
                    self.guiClient.sndMsg('setMainAnswerText\t' + msg_sp[1])
                    self.ntts.play(msg_sp[1])
                    self.gstt.restartMic()
                    self.guiClient.sndMsg('setMainAnswerText\t' + ' ')
                    if msg_sp[0] == 'q':
                        step = 1
                    else:
                        step = 0

if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/shs_key.json"
    main = Main()
    main.start()
