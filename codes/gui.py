#encoding='utf-8-sig'

import csv
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QHBoxLayout, QRadioButton, QCheckBox, QPushButton, QMenu,
                             QGridLayout, QVBoxLayout, QLabel, QCalendarWidget, QLineEdit, QLayout, QComboBox,
                             QMainWindow)
from PyQt5.QtCore import QDate

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
        self.layoutFirst = self.createLayoutSecond()  # 첫 번째 화면, 목적지 입력

        MainWindow.setCentralWidget(self.centralwidget)

    def createLayoutSecond(self):
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
        hbox.addWidget(self.pushButton)

        return hbox

    def aboutPushButton(self):
        print(self.comboBox.currentText()[-3:])

    def csvRead(self, path):
        fR = open(path, 'r', encoding='utf-8-sig', newline='\n')
        rdr = csv.reader(fR)
        return rdr

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())