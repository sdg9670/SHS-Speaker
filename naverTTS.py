
# -*- coding: utf-8 -*-
# 네이버 음성합성 Open API 예제
import os
import sys
import urllib.request
import hashlib

client_id = "zyaeotr083"
client_secret = "RXbXFBJ2Dx4Wp4WnsvlXluctr447Cbx8jorhQfKt"

url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"

speakers = [
    'mijin',     #한국어 여성
    'jinho',     #한국어 남성
    'clara',     #영어 여성
    'matt',      #영어 남성
    'yuri',      #일본어 여성
    'shinji',    #일본어 남성
    'meimei',    #중국어 여성
    'liangliang',#중국어 남성
    'jose',      #스페인어 남성
    'carmen'     #스페인어 여성
    ]



class NaverTTS():
    def __init__(self, speaker=0, speed=0):
        self.speaker = speakers[speaker]
        self.speed=str(speed)
    def play(self, txt):
        m = hashlib.sha512(txt.encode())
        tmpPlayPath = 'tts/' + m.hexdigest() + '.mp3'
        if os.path.isfile(tmpPlayPath) == 1:
            print()
            os.system('cvlc ' + tmpPlayPath + ' --play-and-exit')
        else:
            encText = urllib.parse.quote(txt)
            data = "speaker=" + self.speaker + "&speed=" + self.speed + "&text=" + encText;

            request = urllib.request.Request(url)
            request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
            request.add_header("X-NCP-APIGW-API-KEY",client_secret)
            response = urllib.request.urlopen(request, data=data.encode('utf-8'))
            rescode = response.getcode()
            if(rescode==200):
                response_body = response.read()
                with open(tmpPlayPath, 'wb') as f:
                    f.write(response_body)

                #외부 프로그램 사용 vlc
                os.system('cvlc ' + tmpPlayPath + ' --play-and-exit')
                #라즈베리파이
                #os.system('omxplayer ' + tmpPlayPath)
            else:
                print("Error Code:" + rescode)

