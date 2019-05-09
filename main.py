#-*- coding:utf-8 -*-
#!/usr/bin/env python

import googleSTT
import naverTTS
import socketClient

tts = naverTTS.NaverTTS()

class Main:
    def start():
        gstt = googleSTT.GoogleSTT()
        ntts = naverTTS.NaverTTS()
        sc = socketClient.SocketClient()
        sc.runChat()

        step = 0
        with open('log.txt', 'a') as f:
            while True:
                # 음성 인식 될때까지 대기 한다.
                stt = gstt.getText()
                if stt is None:
                    break
                else:
                    print('나: ' + str(stt))
                    if step == 0 and '안녕 다솜' in stt.strip():
                        gstt.pauseMic()
                        ntts.play('말씀하세요.')
                        gstt.restartMic()
                        step = 1
                    elif step == 1:
                        sc.sndMsg('speaker\tnal\t' + stt.strip())
                        gstt.pauseMic()
                        msg = sc.getMsg()
                        print(msg)
                        ntts.play(msg)
                        gstt.restartMic()
                        step = 0
if __name__ == '__main__':
    Main.start()
