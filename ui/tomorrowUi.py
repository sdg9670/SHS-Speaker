from PyQt5 import QtCore, QtGui, QtWidgets, uic

class tomorrowUi(QtWidgets.QWidget):
    def __init__(self):
        super(tomorrowUi, self).__init__()
        uic.loadUi('ui/tomorrow.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def setUi(self, temptomorrow):
        if '맑음' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '흐림' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '구름많음' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '흐리고' and '비' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '비' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        elif '눈' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '구름조금' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '뇌우' in temptomorrow['날씨']['오전날씨']:
            self.image_label.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        if '맑음' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '흐림' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '흐리고' and '비' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '비' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        elif '흐리고' and '눈' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '구름많음' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '흐리고 비' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '눈' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '흐리고 눈' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '구름조금' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '뇌우' in temptomorrow['날씨']['오후날씨']:
            self.image_label_26.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))

        if '맑음' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '구름많음' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '구름적음' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '흐림' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '뇌우' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        elif '흐리고' and '비' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '비' in temptomorrow['시간별날씨'][0]['날씨']:
            self.image_label_2.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if '맑음' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '구름많음' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '구름적음' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '흐림' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '뇌우' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        elif '흐리고' and '비' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '비' in temptomorrow['시간별날씨'][1]['날씨']:
            self.image_label_3.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if '맑음' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '구름많음' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '구름적음' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '흐림' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '뇌우' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        elif '흐리고' and '비' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '비' in temptomorrow['시간별날씨'][2]['날씨']:
            self.image_label_4.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if '맑음' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '구름많음' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '구름적음' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '흐림' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '뇌우' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        elif '흐리고' and '비' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '비' in temptomorrow['시간별날씨'][3]['날씨']:
            self.image_label_5.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if '맑음' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '구름많음' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '구름적음' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '흐림' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '뇌우' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        elif '흐리고' and '비' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '비' in temptomorrow['시간별날씨'][4]['날씨']:
            self.image_label_6.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if '맑음' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '구름많음' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '구름적음' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '흐림' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '뇌우' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        elif '흐리고' and '비' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '비' in temptomorrow['시간별날씨'][5]['날씨']:
            self.image_label_8.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if '맑음' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '구름많음' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '구름적음' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '흐림' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '뇌우' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        elif '흐리고' and '비' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '비' in temptomorrow['시간별날씨'][6]['날씨']:
            self.image_label_7.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if '맑음' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif '구름많음' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 11.png"))
        elif '구름적음' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 1.png"))
        elif '흐림' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif '뇌우' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 3.png"))
        elif '흐리고' and '비' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 7.png"))
        elif '흐리고' and '눈' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 8.png"))
        elif '눈' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 9.png"))
        elif '비' in temptomorrow['시간별날씨'][7]['날씨']:
            self.image_label_9.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))


        if int(temptomorrow['주간날씨'][0]['오전강수'].replace('%', '')) < 10:
            self.image_label_10.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][0]['오전강수'].replace('%', '')) < 60:
            self.image_label_10.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][0]['오전강수'].replace('%', '')) >= 60:
            self.image_label_10.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][0]['오후강수'].replace('%', '')) < 10:
            self.image_label_18.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][0]['오후강수'].replace('%', '')) < 60:
            self.image_label_18.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][0]['오후강수'].replace('%', '')) >= 60:
            self.image_label_18.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][1]['오전강수'].replace('%', '')) < 10:
            self.image_label_11.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][1]['오전강수'].replace('%', '')) < 60:
            self.image_label_11.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][1]['오전강수'].replace('%', '')) >= 60:
            self.image_label_11.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][1]['오후강수'].replace('%', '')) < 10:
            self.image_label_19.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][1]['오후강수'].replace('%', '')) < 60:
            self.image_label_19.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][1]['오후강수'].replace('%', '')) >= 60:
            self.image_label_19.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][2]['오전강수'].replace('%', '')) < 10:
            self.image_label_12.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][2]['오전강수'].replace('%', '')) < 60:
            self.image_label_12.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][2]['오전강수'].replace('%', '')) >= 60:
            self.image_label_12.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][2]['오후강수'].replace('%', '')) < 10:
            self.image_label_20.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][2]['오후강수'].replace('%', '')) < 60:
            self.image_label_20.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][2]['오후강수'].replace('%', '')) >= 60:
            self.image_label_20.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][3]['오전강수'].replace('%', '')) < 10:
            self.image_label_13.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][3]['오전강수'].replace('%', '')) < 60:
            self.image_label_13.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][3]['오전강수'].replace('%', '')) >= 60:
            self.image_label_13.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][3]['오후강수'].replace('%', '')) < 10:
            self.image_label_21.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][3]['오후강수'].replace('%', '')) < 60:
            self.image_label_21.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][3]['오후강수'].replace('%', '')) >= 60:
            self.image_label_21.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][4]['오전강수'].replace('%', '')) < 10:
            self.image_label_14.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][4]['오전강수'].replace('%', '')) < 60:
            self.image_label_14.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][4]['오전강수'].replace('%', '')) >= 60:
            self.image_label_14.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][4]['오후강수'].replace('%', '')) < 10:
            self.image_label_22.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][4]['오후강수'].replace('%', '')) < 60:
            self.image_label_22.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][4]['오후강수'].replace('%', '')) >= 60:
            self.image_label_22.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][5]['오전강수'].replace('%', '')) < 10:
            self.image_label_15.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][5]['오전강수'].replace('%', '')) < 60:
            self.image_label_15.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][5]['오전강수'].replace('%', '')) >= 60:
            self.image_label_15.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][5]['오후강수'].replace('%', '')) < 10:
            self.image_label_23.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][5]['오후강수'].replace('%', '')) < 60:
            self.image_label_23.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][5]['오후강수'].replace('%', '')) >= 60:
            self.image_label_23.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][6]['오전강수'].replace('%', '')) < 10:
            self.image_label_16.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][6]['오전강수'].replace('%', '')) < 60:
            self.image_label_16.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][6]['오전강수'].replace('%', '')) >= 60:
            self.image_label_16.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][6]['오후강수'].replace('%', '')) < 10:
            self.image_label_24.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][6]['오후강수'].replace('%', '')) < 60:
            self.image_label_24.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][6]['오후강수'].replace('%', '')) >= 60:
            self.image_label_24.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][7]['오전강수'].replace('%', '')) < 10:
            self.image_label_17.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][7]['오전강수'].replace('%', '')) < 60:
            self.image_label_17.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][7]['오전강수'].replace('%', '')) >= 60:
            self.image_label_17.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))
        if int(temptomorrow['주간날씨'][7]['오후강수'].replace('%', '')) < 10:
            self.image_label_25.setPixmap(QtGui.QPixmap("ui/image/자산 10.png"))
        elif 10 <= int(temptomorrow['주간날씨'][7]['오후강수'].replace('%', '')) < 60:
            self.image_label_25.setPixmap(QtGui.QPixmap("ui/image/자산 2.png"))
        elif int(temptomorrow['주간날씨'][7]['오후강수'].replace('%', '')) >= 60:
            self.image_label_25.setPixmap(QtGui.QPixmap("ui/image/자산 6.png"))


        self.weather_label_8.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">미세먼지 "+temptomorrow['날씨']['오후미세먼지']+"</span></p></body></html>")
        self.weather_label_7.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">미세먼지 "+temptomorrow['날씨']['오전미세먼지']+"</span></p></body></html>")
        self.weather_label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:28pt; font-weight:696; color:#ffffff;\">"+temptomorrow['날씨']['오전온도'].replace('도씨','')+"</span></p></body></html>")
        self.weather_label_9.setText("<html><head/><body><p align=\"justify\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:14pt; font-weight:696; color:#ffffff;\">시간대별 날씨</span></p></body></html>")
        self.weather_label_18.setText("<html><head/><body><p align=\"justify\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:14pt; font-weight:696; color:#ffffff;\">주간 날씨</span></p></body></html>")
        self.weather_label_10.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][0]['시간']+"</span></p></body></html>")
        self.weather_label_11.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][1]['시간']+"</span></p></body></html>")
        self.weather_label_12.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][2]['시간']+"</span></p></body></html>")
        self.weather_label_13.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][3]['시간']+"</span></p></body></html>")
        self.weather_label_14.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][4]['시간']+"</span></p></body></html>")
        self.weather_label_15.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][5]['시간']+"</span></p></body></html>")
        self.weather_label_16.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][6]['시간']+"</span></p></body></html>")
        self.weather_label_17.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][7]['시간']+"</span></p></body></html>")
        self.weather_label_19.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][0]['요일']+"</span></p></body></html>")
        self.weather_label_20.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][1]['요일']+"</span></p></body></html>")
        self.weather_label_21.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][2]['요일']+"</span></p></body></html>")
        self.weather_label_22.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][3]['요일']+"</span></p></body></html>")
        self.weather_label_23.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][4]['요일']+"</span></p></body></html>")
        self.weather_label_24.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][5]['요일']+"</span></p></body></html>")
        self.weather_label_25.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][6]['요일']+"</span></p></body></html>")
        self.weather_label_26.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:9pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][7]['요일']+"</span></p></body></html>")
        self.weather_label_35.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][0]['온도']+"</span></p></body></html>")
        self.weather_label_36.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][1]['온도']+"</span></p></body></html>")
        self.weather_label_37.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][2]['온도']+"</span></p></body></html>")
        self.weather_label_38.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][3]['온도']+"</span></p></body></html>")
        self.weather_label_39.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][4]['온도']+"</span></p></body></html>")
        self.weather_label_40.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][5]['온도']+"</span></p></body></html>")
        self.weather_label_41.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][6]['온도']+"</span></p></body></html>")
        self.weather_label_42.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['시간별날씨'][7]['온도']+"</span></p></body></html>")
        self.weather_label_43.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][0]['최고기온']+"</span></p></body></html>")
        self.weather_label_44.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][0]['최저기온']+"</span></p></body></html>")
        self.weather_label_45.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][1]['최저기온']+"</span></p></body></html>")
        self.weather_label_46.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][2]['최저기온']+"</span></p></body></html>")
        self.weather_label_47.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][3]['최저기온']+"</span></p></body></html>")
        self.weather_label_48.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][4]['최저기온']+"</span></p></body></html>")
        self.weather_label_49.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][5]['최저기온']+"</span></p></body></html>")
        self.weather_label_50.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][6]['최저기온']+"</span></p></body></html>")
        self.weather_label_51.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][7]['최저기온']+"</span></p></body></html>")
        self.weather_label_52.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][1]['최고기온']+"</span></p></body></html>")
        self.weather_label_53.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][2]['최고기온']+"</span></p></body></html>")
        self.weather_label_54.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][3]['최고기온']+"</span></p></body></html>")
        self.weather_label_55.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][4]['최고기온']+"</span></p></body></html>")
        self.weather_label_56.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][5]['최고기온']+"</span></p></body></html>")
        self.weather_label_57.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][6]['최고기온']+"</span></p></body></html>")
        self.weather_label_58.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:8pt; font-weight:696; color:#ffffff;\">"+temptomorrow['주간날씨'][7]['최고기온']+"</span></p></body></html>")
        self.weather_label_4.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'굴림,gulim,AppleSDGothicNeo-Regular,sans-serif\'; font-size:28pt; font-weight:696; color:#ffffff;\">"+temptomorrow['날씨']['오후온도'].replace('도씨','')+"</span></p></body></html>")
        self.weather_label_27.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">오전</span></p></body></html>")
        self.weather_label_28.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">오후</span></p></body></html>")
        self.weather_label_29.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">"+temptomorrow['날씨']['오전날씨']+"</span></p></body></html>")
        self.weather_label_30.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">"+temptomorrow['날씨']['오후날씨']+"</span></p></body></html>")
