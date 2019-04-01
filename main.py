#-*- coding:utf-8 -*-
#!/usr/bin/env python

import googleSTT
import naverTTS
import socketClient

tts = naverTTS.NaverTTS()

#명령어 처리
cmdLists = [
        #명령어               대답                     종료 리턴값
        ['끝내자',     '그럼 꺼져!',            0],
        ['안녕',       '안녕하든가!',                      1],
        ['누구냐',     '난 구글 스피치와 네이버 TTS다.',   1],
        ['이름이 뭐니', '난 아직 이름이 없다.',                 1],
        ['나이는',     '난 태어나다 말았다.',                1],
        ['뭘 좋아해',   '잘생긴 심동근',                     1]]
def CommandProc(stt):
    # 문자 양쪽 공백 제거
    cmd = stt.strip()
    # 입력 받은 문자 화면에 표시
    # 2.x
    #print('나 : ' + cmd.encode('utf-8'))
    # 3.x
    #print('나 : ' + str(cmd))

    # 2.x : 문자가 unicode인지 확인 필요
    # if type(cmd) is unicode:

    #명령 리스트와 비교
    for cmdList in cmdLists:
        # 같은 유니코드끼린 바로 대입이 가능하다.
        if str(cmd) == cmdList[0]:

            #네이버 TTS
            tts.play(cmdList[1])

            #구글 스피치 대답 화면에 표시
            print ('구글 스피치 : ' + cmdList[1])

            # 종료 명령 리턴 0이면 종료
            # 1이면 계속
            return cmdList[2]

    # 명령이 없거나
    # unicode가 아니면 못 알아 들었다고 화면에 표시하고
    # 계속
    print ('죄송합니다. 알아듣지 못했습니다.')

    tts.play('죄송합니다. 알아듣지 못했습니다.')
    return 1

def main():
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
                if step == 0 and stt.strip() == '안녕 다솜':
                    gstt.pauseMic()
                    tts.play('말씀하세요.')
                    gstt.restartMic()
                    step = 1
                elif step == 1:
                    sc.sndMsg('speaker\tnal\t' + stt.strip())
                    gstt.pauseMic()
                    if CommandProc(stt) == 0:
                        break
                    gstt.restartMic()
                    step = 0
if __name__ == '__main__':
    main()
