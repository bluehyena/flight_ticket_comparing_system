#encoding='utf-8-sig'

import csv
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QHBoxLayout, QRadioButton, QCheckBox, QPushButton, QMenu,
                             QGridLayout, QVBoxLayout, QLabel, QCalendarWidget, QLineEdit, QLayout, QComboBox)
from PyQt5.QtCore import QDate


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.systemFont = QFont('Arial', 30)

        layoutFirst = self.createLayoutFirst()      # 첫 번째 화면, 목적지 입력
        layoutSecond = self.createLayoutSecond()    # 두 번째 화면, 편도 or 왕복 선택
        layoutThird = self.createLayoutThird()      # 세 번째 화면, 기간 입력 (편도 -> 출발 기간 입력 & 왕복 -> 출발 기간 입력 그리고 여행 기한 입력)

        self.setLayout(layoutFirst)
        self.setWindowTitle('항공권 비교 분석기')
        self.setGeometry(300, 300, 480, 320)

        self.show()


    def createLayoutFirst(self):
        self.comboBox_11 = QComboBox()
        self.comboBox_11.setFixedHeight(50)
        self.comboBox_11.setFont(self.systemFont)
        airportList = []
        for line in self.csvRead('../airportList.csv'):
            airportList.append(line[1] + '(' + line[0] + ')' + line[2])
        for airport in airportList:
            self.comboBox_11.addItem(airport)

        self.pushButton_12 = QPushButton("확인")
        self.pushButton_12.setFixedHeight(50)
        self.pushButton_12.setFixedWidth(100)
        self.pushButton_12.setFont(self.systemFont)
        self.pushButton_12.clicked.connect(self.aboutPushButton_12)

        hbox = QHBoxLayout()
        hbox.addWidget(self.comboBox_11)
        hbox.addWidget(self.pushButton_12)

        return hbox

    def aboutPushButton_12(self):
        print(self.comboBox_11.currentText()[-3:])

    def createLayoutSecond(self):

        lineEdit = QLineEdit("도착지 입력")
        pushButton = QPushButton("확인")

        hbox = QHBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(pushButton)

        return hbox

    def createLayoutThird(self):

        lineEdit = QLineEdit("도착지 입력")
        pushButton = QPushButton("확인")

        hbox = QHBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(pushButton)

        return hbox

    def csvRead(self, path):
        fR = open(path, 'r', encoding='utf-8-sig', newline='\n')
        rdr = csv.reader(fR)
        return rdr
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())