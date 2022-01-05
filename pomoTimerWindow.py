import sys
import threading
import time
import datetime
from playsound import playsound


from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
)
from PyQt5.QtCore import Qt, pyqtSignal

from ui.pomoTimerWindowUi import Ui_pomoTimer

class pomoTimerWindow(QDialog, Ui_pomoTimer):

    timerEnd = pyqtSignal(str)

    def __init__(self, mainApp, parent=None):
        super().__init__(parent)
        self.mainApp = mainApp
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.connectSignalsSlots()
        self.remainingTimeSeconds = 10
        self.counting = False
        self.runningTaskID = 0
        self.startTime = 0
        self.stopTime = 0
        self.mousReleased = False
        self.mouseOriginalPos = 0
        self.mouseFinalPos = 0


    def connectSignalsSlots(self):
        print("Nothing to connect")
        self.finished.connect(self.onClose)
        self.stopButton.clicked.connect(self.stopClicked)
        self.timerEnd.connect(self.onTimerExpired)
        # self.mousePressEvent.connect(self.mouseGrabber)
        # self.action_Exit.triggered.connect(self.close)
        # self.action_Find_Replace.triggered.connect(self.findAndReplace)
        # self.action_About.triggered.connect(self.about)

    def stopClicked(self):
        self.close()

    def mousePressEvent(self, event):
        print("mouse is pressed at :" + str(event.pos()))
        self.mouseOriginalPos = event.pos()

    def mouseReleaseEvent(self, event):
        print("mouse is released at :" + str(event.pos()))
        self.mouseFinalPos = event.pos()
        posDiff = self.mouseFinalPos - self.mouseOriginalPos
        print(posDiff)
        self.move(self.pos()+posDiff)


    def onClose(self, event):
        if self.counting:
            self.counting = False
            self.stopTime = datetime.datetime.now()
            print("stop at " + str(self.stopTime))
            duration = self.stopTime - self.startTime
            print(duration)
            self.mainApp.addSession(self.runningTaskID, self.startTime, self.stopTime)
            self.mainApp.maimWindow.refreshDataDisplay()

    def onTimerExpired(self):
        if self.counting:
            self.counting = False
            self.stopTime = datetime.datetime.now()
            print("stop at " + str(self.stopTime))
            duration = self.stopTime - self.startTime
            print(duration)
            self.mainApp.addSession(self.runningTaskID, self.startTime, self.stopTime)
            self.mainApp.maimWindow.refreshDataDisplay()
            


    def setDuration(self, duration, taskID):
        self.remainingTimeSeconds = duration
        self.updateTimeDisplay()
        self.counting = True
        self.runningTaskID = taskID
        self.startTime = datetime.datetime.now()
        # print("start at :" + str(self.startTime))
        self.label.setText(self.mainApp.getTaskNameByID(taskID))
        myThread = threading.Thread(target=self.countingThread)
        myThread.start()
        print("thread launched")

    def updateTimeDisplay(self):
        totalSeconds = self.remainingTimeSeconds
        remainingHours = int(totalSeconds/3600)
        totalSeconds = totalSeconds - remainingHours * 3600
        remainingMinuts = int(totalSeconds/60)
        totalSeconds = totalSeconds - remainingMinuts * 60
        remainingSeconds = totalSeconds
        self.hoursLCD.display(str(remainingHours).zfill(2))
        self.mimutesLCD.display(str(remainingMinuts).zfill(2))
        self.secondsLCD.display(str(remainingSeconds).zfill(2))

    def countingThread(self):
        while self.counting:
            print(self.remainingTimeSeconds)
            if self.remainingTimeSeconds>0:
                time.sleep(1)
                self.remainingTimeSeconds = self.remainingTimeSeconds - 1
                self.updateTimeDisplay()
            else:
                print("Emit signal")
                # self.counting = False
                # self.updateTimeDisplay()
                self.timerEnd.emit(None)
                playsound('ui/sounds/endTimer.wav')
            
            



    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )
