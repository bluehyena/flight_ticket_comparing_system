import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton
, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout, QLabel, QCalendarWidget)
from PyQt5.QtCore import QDate

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(grid)

        self.setWindowTitle('항공권 비교 분석기')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('항공권의 종류를 선택하세요')

        radio1 = QRadioButton('편도')
        radio2 = QRadioButton('왕복')
        radio3 = QRadioButton('다구간')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox('왕복일 경우 체크 해주세요')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        popupbutton = QPushButton('여행기간을 입력해 주세요')
        menu = QMenu(self)
        menu.addAction('1일')
        menu.addAction('2일')
        menu.addAction('3일')
        menu.addAction('4일')
        menu.addAction('5일')
        menu.addAction('6일')
        menu.addAction('7일')
        menu.addAction('8일')
        menu.addAction('9일')
        menu.addAction('10일')
        menu.addAction('11일')
        menu.addAction('12일')
        menu.addAction('13일')
        menu.addAction('14일')
        menu.addAction('15일')
        menu.addAction('16일')
        menu.addAction('17일')
        menu.addAction('18일')
        menu.addAction('19일')
        menu.addAction('20일')
        menu.addAction('21일')
        menu.addAction('22일')
        menu.addAction('23일')
        menu.addAction('24일')
        menu.addAction('25일')
        menu.addAction('26일')
        menu.addAction('27일')
        menu.addAction('28일')
        menu.addAction('29일')
        menu.addAction('30일')
        popupbutton.setMenu(menu)

        popupbutton2 = QPushButton('희망기간을 입력해 주세요')
        menu2 = QMenu(self)
        menu2.addAction('1일')
        menu2.addAction('2일')
        menu2.addAction('3일')
        menu2.addAction('4일')
        menu2.addAction('5일')
        menu2.addAction('6일')
        menu2.addAction('7일')
        menu2.addAction('8일')
        menu2.addAction('9일')
        menu2.addAction('10일')
        menu2.addAction('11일')
        menu2.addAction('12일')
        menu2.addAction('13일')
        menu2.addAction('14일')
        menu2.addAction('15일')
        menu2.addAction('16일')
        menu2.addAction('17일')
        menu2.addAction('18일')
        menu2.addAction('19일')
        menu2.addAction('20일')
        menu2.addAction('21일')
        menu2.addAction('22일')
        menu2.addAction('23일')
        menu2.addAction('24일')
        menu2.addAction('25일')
        menu2.addAction('26일')
        menu2.addAction('27일')
        menu2.addAction('28일')
        menu2.addAction('29일')
        menu2.addAction('30일')
        popupbutton2.setMenu(menu2)


        vbox = QVBoxLayout()
        vbox.addWidget(popupbutton)
        vbox.addWidget(popupbutton2)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('편도일 경우')
        groupbox.setFlat(True)
        
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)

        lbl = QLabel()
        date = cal.selectedDate()
        lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(lbl)

        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        groupbox = QGroupBox('다구간일 경우 체크해주세요')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton('URL 바로가기')
        togglebutton = QPushButton('땡처리 알아보기')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('다구간 여정 추가하기')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('여정 목록')
        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addWidget(togglebutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())