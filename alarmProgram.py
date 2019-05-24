import os
import threading
import time
import naverTTS
from datetime import datetime

class AlarmProgram(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.alarms = {}

    def alarmOn(self, id):
        naverTTS.NaverTTS().play(self.alarms[id]['datetime'] + ' ' + self.alarms[id]['content'] + ' 알람이 울립니다.')
        self.alarms.pop(id)
        os.system('cvlc sound/alarm.mp3 --play-and-exit')

    def run(self):
        while True:
            now = datetime.now()
            for key, value in self.alarms.items():
                if datetime.strptime(self.alarms[key]['datetime'], '%Y/%m/%d %H:%M:%S') <= now:
                    self.alarmOn(key)
                    break;
            time.sleep(30)

    def setAlarmList(self, alarms):
        self.alarms = alarms
        print(alarms)
