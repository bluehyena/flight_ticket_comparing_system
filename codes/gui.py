#encoding='utf-8-sig'

import csv
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QHBoxLayout, QRadioButton, QCheckBox, QPushButton, QMenu,
                             QGridLayout, QVBoxLayout, QLabel, QCalendarWidget, QLineEdit, QLayout, QComboBox,
                             QMainWindow)
from PyQt5.QtCore import QDate

inputData = []

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiFirst = UIFirst()
        self.uiSecond = UISecond()
        self.startUIFirst()

    def startUIFirst(self):
        self.uiFirst.setupUI(self)
        self.uiFirst.pushButton.clicked.connect(self.startUISecond)
        self.show()

    def startUISecond(self):
        self.uiSecond.setupUI(self)
        self.show()

class UIFirst(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 480, 320)

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
        print(self.comboBox.currentText()[-3:])
        inputData.append(self.comboBox.currentText()[-3:])

    def csvRead(self, path):
        fR = open(path, 'r', encoding='utf-8-sig', newline='\n')
        rdr = csv.reader(fR)
        return rdr

class UISecond(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle('항공권 비교 분석기')
        MainWindow.setGeometry(300, 300, 480, 320)

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
        print("편도")
        inputData.append("편도")

    def aboutPushButton2(self):
        print("왕복")
        inputData.append("왕복")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())