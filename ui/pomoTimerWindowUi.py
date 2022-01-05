# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './pomoTimerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pomoTimer(object):
    def setupUi(self, pomoTimer):
        pomoTimer.setObjectName("pomoTimer")
        pomoTimer.resize(262, 110)
        pomoTimer.setWindowOpacity(0.5)
        self.label = QtWidgets.QLabel(pomoTimer)
        self.label.setGeometry(QtCore.QRect(10, -1, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Alstom")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pauseButton = QtWidgets.QPushButton(pomoTimer)
        self.pauseButton.setGeometry(QtCore.QRect(10, 76, 121, 30))
        self.pauseButton.setObjectName("pauseButton")
        self.stopButton = QtWidgets.QPushButton(pomoTimer)
        self.stopButton.setGeometry(QtCore.QRect(130, 76, 121, 30))
        self.stopButton.setObjectName("stopButton")
        self.widget = QtWidgets.QWidget(pomoTimer)
        self.widget.setGeometry(QtCore.QRect(10, 30, 241, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hoursLCD = QtWidgets.QLCDNumber(self.widget)
        self.hoursLCD.setDigitCount(2)
        self.hoursLCD.setObjectName("hoursLCD")
        self.horizontalLayout.addWidget(self.hoursLCD)
        self.mimutesLCD = QtWidgets.QLCDNumber(self.widget)
        self.mimutesLCD.setDigitCount(2)
        self.mimutesLCD.setObjectName("mimutesLCD")
        self.horizontalLayout.addWidget(self.mimutesLCD)
        self.secondsLCD = QtWidgets.QLCDNumber(self.widget)
        self.secondsLCD.setDigitCount(2)
        self.secondsLCD.setObjectName("secondsLCD")
        self.horizontalLayout.addWidget(self.secondsLCD)

        self.retranslateUi(pomoTimer)
        QtCore.QMetaObject.connectSlotsByName(pomoTimer)

    def retranslateUi(self, pomoTimer):
        _translate = QtCore.QCoreApplication.translate
        pomoTimer.setWindowTitle(_translate("pomoTimer", "Pomodoro Timer"))
        self.label.setText(_translate("pomoTimer", "TextLabel"))
        self.pauseButton.setText(_translate("pomoTimer", "Pause"))
        self.stopButton.setText(_translate("pomoTimer", "Stop"))
