from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QPalette, QColor

import threading
import socket
import datetime
import atexit

# from mainScreen import mainScreen

import sys

from dbHandler import dbHandler
from pomoWindow import pomoWindow
from pomoTimerWindow import pomoTimerWindow

# v1.0
# Display task list (use testingManagementScreen renamed as mainScreen)
# Add task
# Close task
# launch pomodoro session

# TBD:
# Come back to main and refresh after editing properties
# Set the stoptime when timer is finished even if window is not closed
# Start on the correct tab


class PomoApp(QObject):

    socketDataReceived = pyqtSignal(str)

    def getAllTasksProfile(self, profile):
        return self.myDBHandler.getAllTasksProfile(profile)

    def addQuickTask(self, title, profile):
        self.myDBHandler.addTask(title, profile)

    def incrementLoggedTime(self, taskID, increment):
        self.myDBHandler.incrementLoggedTime(taskID, increment)
        self.maimWindow.refreshDataDisplay()

    def getDailyFocusTime(self):
        sessions = self.myDBHandler.getDailySessions()
        # print("Daily Sessions :" + str(sessions))
        totalDuration = datetime.timedelta(0)
        for session in sessions:
            start = session[1]
            date_start = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
            stop = session[2]
            date_stop = datetime.datetime.strptime(stop, "%Y-%m-%d %H:%M:%S.%f")
            duration = date_stop - date_start
            totalDuration = totalDuration + duration
        return str(totalDuration).split(".")[0]

    def getDailyTimers(self):
        sessions = self.myDBHandler.getDailySessions()
        return len(sessions)

    def getTaskNameByID(self, taskID):
        return self.myDBHandler.getTaskNameByID(taskID)

    def getTaskDescriptionByID(self, taskID):
        return self.myDBHandler.getTaskDescriptionByID(taskID)

    def getTaskNotesByID(self, taskID):
        return self.myDBHandler.getTaskNotesByID(taskID)

    def setTaskTitle(self, taskID, title):
        self.myDBHandler.setTaskTitle(taskID, title)

    def setTaskDescription(self, taskID, description):
        self.myDBHandler.setTaskDescription(taskID, description)

    def setTaskNotes(self, taskID, notes):
        self.myDBHandler.setTaskNotes(taskID, notes)

    def deleteTask(self, taskID):
        self.myDBHandler.deleteTask(taskID)
        self.maimWindow.refreshDataDisplay()

    def addSession(self, taskID, startTime, stopTime):
        self.myDBHandler.addSession(taskID, startTime, stopTime)

    def getAllSessionsOnDate(self,date):
        return self.myDBHandler.getAllSessionsOnDate(date)


    def getFilteredTasks(self, profile, status):
        return self.myDBHandler.getFilteredTasks(profile, status)

    def calculateTaskLoggedTime(self,taskID):
        taskSessions = self.myDBHandler.getAllTaskSessions(taskID)
        # print(taskSessions)
        totalDuration = datetime.timedelta(0)
        for session in taskSessions:
            start = session[1]
            date_start = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
            stop = session[2]
            date_stop = datetime.datetime.strptime(stop, "%Y-%m-%d %H:%M:%S.%f")
            duration = date_stop - date_start
            totalDuration = totalDuration + duration
        return str(totalDuration).split(".")[0]

    def completeTask(self, taskID):
        self.myDBHandler.completeTask(taskID)
        self.maimWindow.refreshDataDisplay()

    def log(self):
        sessions = self.myDBHandler.getAllSessionsDecreasing()
        result = ""
        prevDateStr = ""
        for session in sessions:
            sessionDate = datetime.datetime.strptime(session[1], "%Y-%m-%d %H:%M:%S.%f")
            sessionDateStr = datetime.datetime.strftime(sessionDate, "%A %B %d")
            if sessionDateStr != prevDateStr:
                prevDateStr = sessionDateStr
                result = result + "[" + str(sessionDateStr) + "]\n" 
                sessionsOnThisDate = self.getAllSessionsOnDate(str(sessionDate))
                for sessionOnThisDate in sessionsOnThisDate:
                    taskID = sessionOnThisDate[0]
                    # print("id " + str(taskID))
                    startDateTime = datetime.datetime.strptime(sessionOnThisDate[1],"%Y-%m-%d %H:%M:%S.%f")
                    stopDateTime = datetime.datetime.strptime(sessionOnThisDate[2],"%Y-%m-%d %H:%M:%S.%f")
                    duration = stopDateTime - startDateTime
                    result = result + self.getTaskNameByID(taskID) + ": " + str(duration)[:-7] + "\n"
                result = result + "\n\n"
        return str(result)

    def listenSocket(self):

        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        data = data.decode('utf-8')
                        if data:
                            taskData = data.split(";")
                            print(taskData)
                            self.addQuickTask(taskData[0])
                            # self.maimWindow.refreshDataDisplay()
                            self.socketDataReceived.emit(data)
                        if not data:
                            break

    def __init__(self):
        super().__init__()
        self.myDBHandler = dbHandler()
        # Run socket listening thread for external task add request
        myThread = threading.Thread(target=self.listenSocket)
        myThread.start()
        app = QApplication(sys.argv)
        self.maimWindow = pomoWindow(self)
        self.timerWindow = pomoTimerWindow(self)
        self.maimWindow.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    myPomoApp = PomoApp()