#encoding='utf-8-sig'

import csv
import datetime
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QHBoxLayout, QRadioButton, QCheckBox, QPushButton, QMenu,
                             QGridLayout, QVBoxLayout, QLabel, QCalendarWidget, QLineEdit, QLayout, QComboBox,
                             QMainWindow)
from PyQt5.QtCore import QDate, Qt

inputData = []

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiFirst = UIFirst()
        self.uiSecond = UISecond()
        self.uiThird = UIThird()
        self.uiFourth = UIFourth()
        self.uiFifth = UIFifth()
        self.uiSixth = UISixth()
        self.uiSeventh = UISeventh()
        self.startUIFirst()

    def startUIFirst(self):
        self.uiFirst.setupUI(self)
        self.uiFirst.pushButton.clicked.connect(self.startUISecond)
        self.show()

    def startUISecond(self):
        self.uiSecond.setupUI(self)
        self.uiSecond.pushButton1.clicked.connect(self.startUIThird)
        self.uiSecond.pushButton2.clicked.connect(self.startUIThird)
        self.show()

    def startUIThird(self):
        self.uiThird.setupUI(self)
        self.uiThird.pushButton.clicked.connect(self.startUIFourth)
        self.show()

    def startUIFourth(self):
        self.uiFourth.setupUI(self)
        if(inputData[1] == '왕복'):
            self.uiFourth.pushButton.clicked.connect(self.startUIFifth)
        elif(inputData([1] == '편도')):
            self.uiFourth.pushButton.clicked.connect(self.startUISixth)
        self.show()

    def startUIFifth(self):
        self.uiFifth.setupUI(self)
        self.uiFifth.pushButton.clicked.connect(self.startUISixth)
        self.show()

    def startUISixth(self):
        self.uiSixth.setupUI(self)
        self.uiSixth.pushButton.clicked.connect(self.startUISeventh)
        self.show()

    def startUISeventh(self):
        self.uiSeventh.setupUI(self)
        self.show()

class UIFirst(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 720, 480)

        self.centralwidget = QWidget(MainWindow)

        self.systemFont = QFont('Arial', 30)
        self.layoutFirst = self.createLayoutFirst()      # 첫 번째 화면, 목적지 입력

        MainWindow.setCentralWidget(self.centralwidget)


    def createLayoutFirst(self):
        self.comboBox = QComboBox()
        self.comboBox.setFixedHeight(50)
        self.comboBox.setFont(self.systemFont)
        airportList = []
        for line in self.csvRead('../airportList.csv'):
            airportList.append(line[1] + '(' + line[0] + ')' + line[2])
        for airport in airportList:
            self.comboBox.addItem(airport)

        self.pushButton = QPushButton("확인")
        self.pushButton.setFixedHeight(50)
        self.pushButton.setFixedWidth(100)
        self.pushButton.setFont(self.systemFont)
        self.pushButton.clicked.connect(self.aboutPushButton)

        hbox = QHBoxLayout(self.centralwidget)
        hbox.addWidget(self.comboBox)
        hbox.addWidget(self.pushButton)

        return hbox

    def aboutPushButton(self):
        inputData.append(self.comboBox.currentText()[-3:])

    def csvRead(self, path):
        fR = open(path, 'r', encoding='utf-8-sig', newline='\n')
        rdr = csv.reader(fR)
        return rdr

class UISecond(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 720, 480)

        self.centralwidget = QWidget(MainWindow)

        self.systemFont = QFont('Arial', 30)
        self.layoutSecond = self.createLayoutSecond()  # 두 번째 화면, 편도 or 왕복 선택

        MainWindow.setCentralWidget(self.centralwidget)

    def createLayoutSecond(self):
        self.pushButton1 = QPushButton("편도")
        self.pushButton1.setFixedHeight(50)
        self.pushButton1.setFixedWidth(100)
        self.pushButton1.setFont(self.systemFont)
        self.pushButton1.clicked.connect(self.aboutPushButton1)

        self.pushButton2 = QPushButton("왕복")
        self.pushButton2.setFixedHeight(50)
        self.pushButton2.setFixedWidth(100)
        self.pushButton2.setFont(self.systemFont)
        self.pushButton2.clicked.connect(self.aboutPushButton2)

        hbox = QHBoxLayout(self.centralwidget)
        hbox.addWidget(self.pushButton1)
        hbox.addWidget(self.pushButton2)
        return hbox

    def aboutPushButton1(self):
        inputData.append("편도")

    def aboutPushButton2(self):
        inputData.append("왕복")

class UIThird(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 720, 480)

        self.centralwidget = QWidget(MainWindow)

        self.systemFont = QFont('Arial', 30)
        self.layoutThird = self.createLayoutThird()  # 세 번째 화면, 최소 출발 기간 입력

        MainWindow.setCentralWidget(self.centralwidget)

    def createLayoutThird(self):
        self.label = QLabel("최소 출발 기한")
        self.label.setFont(self.systemFont)
        self.label.setFixedHeight(50)

        self.comboBox1 = QComboBox()
        self.comboBox1.setFixedHeight(30)
        self.comboBox1.setFixedWidth(100)
        self.comboBox1.addItem("년")
        for year in range(2020, 2022):
            self.comboBox1.addItem(str(year))

        self.comboBox2 = QComboBox()
        self.comboBox2.setFixedHeight(30)
        self.comboBox2.setFixedWidth(100)
        self.comboBox2.addItem("월")
        for month in range(1, 13):
            self.comboBox2.addItem(str(month))

        self.comboBox3 = QComboBox()
        self.comboBox3.setFixedHeight(30)
        self.comboBox3.setFixedWidth(100)
        self.comboBox3.addItem("일")
        for day in range(1, 32):
            self.comboBox3.addItem(str(day))

        self.pushButton = QPushButton("확인")
        self.pushButton.setFont(self.systemFont)
        self.pushButton.setFixedHeight(50)
        self.pushButton.setFixedWidth(100)
        self.pushButton.clicked.connect(self.aboutPushButton)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label, alignment=Qt.AlignHCenter)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.comboBox1)
        hbox2.addWidget(self.comboBox2)
        hbox2.addWidget(self.comboBox3)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.pushButton)

        vbox = QVBoxLayout(self.centralwidget)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        return vbox

    def aboutPushButton(self):
        inputData.append(self.comboBox1.currentText())
        inputData.append(self.comboBox2.currentText())
        inputData.append(self.comboBox3.currentText())

class UIFourth(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 720, 480)

        self.centralwidget = QWidget(MainWindow)

        self.systemFont = QFont('Arial', 30)
        self.layoutFourth = self.createLayoutFourth()  # 네 번째 화면, 최대 출발 기간 입력

        MainWindow.setCentralWidget(self.centralwidget)

    def createLayoutFourth(self):
        self.label = QLabel("최대 출발 기한")
        self.label.setFont(self.systemFont)
        self.label.setFixedHeight(50)

        self.comboBox1 = QComboBox()
        self.comboBox1.setFixedHeight(30)
        self.comboBox1.setFixedWidth(100)
        self.comboBox1.addItem("년")
        for year in range(2020, 2022):
            self.comboBox1.addItem(str(year))

        self.comboBox2 = QComboBox()
        self.comboBox2.setFixedHeight(30)
        self.comboBox2.setFixedWidth(100)
        self.comboBox2.addItem("월")
        for month in range(1, 13):
            self.comboBox2.addItem(str(month))

        self.comboBox3 = QComboBox()
        self.comboBox3.setFixedHeight(30)
        self.comboBox3.setFixedWidth(100)
        self.comboBox3.addItem("일")
        for day in range(1, 32):
            self.comboBox3.addItem(str(day))

        self.pushButton = QPushButton("확인")
        self.pushButton.setFont(self.systemFont)
        self.pushButton.setFixedHeight(50)
        self.pushButton.setFixedWidth(100)
        self.pushButton.clicked.connect(self.aboutPushButton)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label, alignment=Qt.AlignHCenter)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.comboBox1)
        hbox2.addWidget(self.comboBox2)
        hbox2.addWidget(self.comboBox3)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.pushButton)

        vbox = QVBoxLayout(self.centralwidget)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        return vbox

    def aboutPushButton(self):
        inputData.append(self.comboBox1.currentText())
        inputData.append(self.comboBox2.currentText())
        inputData.append(self.comboBox3.currentText())

class UIFifth(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 720, 480)

        self.centralwidget = QWidget(MainWindow)

        self.systemFont = QFont('Arial', 30)
        self.layoutFourth = self.createLayoutFifth()  # 다섯 번째 화면, 왕복일 경우 여행 기간 입력

        MainWindow.setCentralWidget(self.centralwidget)

    def createLayoutFifth(self):
        self.lineEdit = QLineEdit("여행 기간 입력 (숫자만, 단위 : 일)")
        self.lineEdit.setFont(self.systemFont)

        self.pushButton = QPushButton("확인")
        self.pushButton.setFont(self.systemFont)
        self.pushButton.clicked.connect(self.aboutPushButton)

        hbox = QHBoxLayout(self.centralwidget)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.pushButton)
        return hbox

    def aboutPushButton(self):
        inputData.append(self.lineEdit.text())

class UISixth(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 720, 480)

        self.centralwidget = QWidget(MainWindow)

        self.systemFont = QFont('Arial', 30)
        self.layoutSixth = self.createLayoutSixth()  # 여섯 번째 화면, 탑승 인원 입력

        MainWindow.setCentralWidget(self.centralwidget)

    def createLayoutSixth(self):
        self.label = QLabel("탑승 인원")
        self.label.setFont(self.systemFont)
        self.label.setFixedHeight(50)

        self.comboBox1 = QComboBox()
        self.comboBox1.setFont(self.systemFont)
        self.comboBox1.setFixedHeight(50)
        self.comboBox1.setFixedWidth(100)
        self.comboBox1.addItem("유아")
        for i in range(0, 11):
            self.comboBox1.addItem(str(i) + "명")

        self.comboBox2 = QComboBox()
        self.comboBox2.setFont(self.systemFont)
        self.comboBox2.addItem("청소년")
        self.comboBox2.setFixedHeight(50)
        self.comboBox2.setFixedWidth(100)
        for i in range(0, 11):
            self.comboBox2.addItem(str(i) + "명")

        self.comboBox3 = QComboBox()
        self.comboBox3.setFont(self.systemFont)
        self.comboBox3.addItem("성인")
        self.comboBox3.setFixedHeight(50)
        self.comboBox3.setFixedWidth(100)
        for i in range(0, 11):
            self.comboBox3.addItem(str(i) + "명")

        self.pushButton = QPushButton("확인")
        self.pushButton.setFont(self.systemFont)
        self.pushButton.setFixedHeight(50)
        self.pushButton.setFixedWidth(100)
        self.pushButton.clicked.connect(self.aboutPushButton)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label, alignment=Qt.AlignHCenter)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.comboBox1)
        hbox2.addWidget(self.comboBox2)
        hbox2.addWidget(self.comboBox3)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.pushButton)

        vbox = QVBoxLayout(self.centralwidget)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        return vbox

    def aboutPushButton(self):
        inputData.append(self.comboBox1.currentText())
        inputData.append(self.comboBox2.currentText())
        inputData.append(self.comboBox3.currentText())
        print(inputData)

class UISeventh(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 720, 480)

        self.centralwidget = QWidget(MainWindow)

        self.systemFont = QFont('Arial', 30)
        self.layoutSeventh = self.createLayoutSeventh()  # 일곱 번째 화면, 결과 출력

        MainWindow.setCentralWidget(self.centralwidget)

    def createLayoutSeventh(self):

        vbox = QVBoxLayout(self.centralwidget)

        return vbox

class InputData():
    def returnData(self):
        return inputData

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())