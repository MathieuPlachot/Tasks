import sqlite3 as lite
import datetime

class dbHandler:

    def getAllProfiles(self):
        allProfiles = []
        for task in self.getFilteredTasks(None, None):
            if not task[10] in  allProfiles:
                allProfiles.append(task[10])
        return allProfiles

    def getFilteredTasks(self, profile, status):

        if not profile:
            profile = "Profile"
        if not status:
            status = "Status"

        request = 'SELECT * FROM Task WHERE Status="' + status + '" and Profile = "' + profile + '"'
        print(request)
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result

    def getTaskNameByID(self, taskID):
        request = 'SELECT Title FROM Task WHERE ID=' + str(taskID)
        # print(request)
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result[0][0]

    def getTaskDescriptionByID(self, taskID):
        request = 'SELECT Description FROM Task WHERE ID=' + str(taskID)
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result[0][0]

    def getTaskNotesByID(self, taskID):
        request = 'SELECT Notes FROM Task WHERE ID=' + str(taskID)
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result[0][0]

    def getTaskOutlookMailIDByID(self, taskID):
        request = 'SELECT OutlookMailID FROM Task WHERE ID=' + str(taskID)
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result[0][0]

    def getAllTaskSessions(self, taskID):
        request = 'SELECT * FROM Session WHERE TaskID=' + str(taskID)
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result

    def getAllSessionsDecreasing(self):
        request = 'SELECT * FROM Session ORDER BY Start DESC'
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result

    def getAllSessionsOnDate(self, date):
        request = 'SELECT * FROM Session WHERE date(Start)=date("' + date + '") ORDER BY Start ASC'
        # print(request)
        self.cur.execute(request)
        result = self.cur.fetchall()
        # print(result)
        return result

    def getDailySessions(self):
        request = "SELECT * FROM Session WHERE date(Start)=date('now','localtime')"
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result

    def addTask(self, taskTitle, profile):
        request = 'INSERT INTO Task(Title, Description, Profile) VALUES (?,?,?)'
        values = (taskTitle,"",profile)
        self.cur.execute(request, values)
        self.con.commit()

    def deleteTask(self, taskID):
        request = 'DELETE FROM Task WHERE ID=' + str(taskID)
        self.cur.execute(request)
        self.con.commit()
        request = 'DELETE FROM Session WHERE TaskID=' + str(taskID)
        self.cur.execute(request)
        self.con.commit()

    def completeTask(self, taskID):
        request = 'UPDATE Task SET Status = "DONE", CloseDate = datetime("now","localtime")  WHERE ID=' + str(taskID)
        self.cur.execute(request)
        self.con.commit()

    def setTaskTitle(self, taskID, title):
        request = 'UPDATE Task SET Title = "' + title + '" WHERE ID=' + str(taskID)
        self.cur.execute(request)
        self.con.commit()

    def setTaskDescription(self, taskID, description):
        request = 'UPDATE Task SET Description = "' + description + '" WHERE ID=' + str(taskID)
        self.cur.execute(request)
        self.con.commit()

    def setTaskNotes(self, taskID, notes):
        request = 'UPDATE Task SET Notes = "' + notes + '" WHERE ID=' + str(taskID)
        self.cur.execute(request)
        self.con.commit()

    def addSession(self, taskID, startTime, stopTime):
        request = 'INSERT INTO Session(TaskID, Start, Stop) VALUES (?,?,?)'
        values = (taskID,startTime,stopTime)
        self.cur.execute(request, values)
        self.con.commit()        
    
    def displayDBEntries(self, type, fields):
        # print("Entries for " + type + " with : " + str(fields))
        if fields != "*":
            selection = ', '.join(fields)
        else:
            selection = "*"
        request = 'SELECT ' + str(selection) + ' FROM ' + str(type)
        self.cur.execute(request)
        return self.cur.fetchall()

    def disconnect(self):
        self.con.close()

    def reconnect(self):
        self.con = None
        self.con = lite.connect('TC_Database/TCDataBase.db')
        self.cur = self.con.cursor()
        self.connection = self.con

    def __init__(self):
        # print("Initializing DB Handler")
        self.con = None
        self.con = lite.connect("DB/Tasks.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.connection = self.con

    
