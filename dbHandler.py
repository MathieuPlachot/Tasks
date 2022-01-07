import sqlite3 as lite
import datetime

class dbHandler:

    def getAllTasks(self):
        request = 'SELECT * FROM Task'
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result

    def getAllOpenTasks(self):
        request = 'SELECT * FROM Task WHERE Status="OPEN"'
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result

    def getAllClosedTasks(self):
        request = 'SELECT * FROM Task WHERE Status="DONE"'
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

        getAllSessionsOnDate

    def getDailySessions(self):
        request = "SELECT * FROM Session WHERE date(Start)=date('now','localtime')"
        self.cur.execute(request)
        result = self.cur.fetchall()
        return result

    def addTask(self, taskTitle):
        request = 'INSERT INTO Task(Title, Description) VALUES (?,?)'
        values = (taskTitle,"")
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

    def getDBVersionAndTimestamp(self):
        request = 'SELECT * FROM DBInfo'
        self.cur.execute(request)
        result = self.cur.fetchall()
        if len(result)>0:
            return result[0]

    def getBaselines(self):
        request = 'SELECT * FROM Baseline'
        self.cur.execute(request)
        result = self.cur.fetchall()
        returnTable = []
        for baseline in result:
            returnTable.append(baseline[0])
        return returnTable



    def saveNewStepStatus(self, reportName, stepID, status, value, comment, baseline, dateTime, ncr):
        print("save step to db")
        # request = "UPDATE TestStep SET Status = '" + status + "', UserEntry = '" + value + "', UserComment = '" + comment + "', Baseline = '" + baseline + "', StatusTimeStamp = '" + dateTime + "' WHERE TestSheetName = '" + reportName + "' AND TestSheetPosition = '" + str(stepID) + "';"
        request = "UPDATE TestStep SET Status = ?, UserEntry = ?, UserComment = ?, Baseline = ?, StatusTimeStamp = ?, NCR = ? WHERE TestSheetName = ? AND TestSheetPosition = ?"
        self.cur.execute(request,(status,value,comment,baseline,dateTime,ncr,reportName,str(stepID)))
        self.con.commit()

    # Get info for equipment by name
    def getEqtInfo(self, eqtName):
        # print("Getting info for report : " + reportName)
        request = 'SELECT * FROM Equipment WHERE Name==\"'+eqtName+'"'
        self.cur.execute(request)
        return self.cur.fetchall()[0]

    # Get info of the LAST version of reportName
    def getReportInfo(self, reportName):
        # print("Getting info for report : " + reportName)
        request = 'SELECT * FROM TestReport WHERE Name==\"'+reportName+'\"'
        self.cur.execute(request)
        return self.cur.fetchall()[0]

    def getReportRevisionData(self, reportName):
        # print("Getting info for report : " + reportName)
        request = 'SELECT * FROM Events WHERE Object==\"'+reportName+'\"'
        self.cur.execute(request)
        return self.cur.fetchall()

    # Get steps of the LAST version of reportName
    def getReportSteps(self, reportName):
        request = 'SELECT * FROM TestStep WHERE TestSheetName==\"'+reportName+'\"'
        self.cur.execute(request)
        return self.cur.fetchall()

    def prettyPrintNCR(self, ncrID):
        ncrString = "[NCR_" + ncrID + "]"
        ncrString = ncrString + "[" + self.getNCRProperty(ncrID, "Location") + "]"
        ncrString = ncrString + "[" + self.getNCRProperty(ncrID, "Location") + "]"
        ncrString = ncrString + "[" + self.getNCRProperty(ncrID, "Subgroup") + "]"
        ncrString = ncrString + "[" + self.getNCRProperty(ncrID, "Ssy") + "]"
        ncrString = ncrString + " " + self.getNCRProperty(ncrID, "Description")
        return ncrString

    def getNCRProperty(self, ncrID, propertyName):
        # print("get prop " + propertyName + " of ncr " + ncrID)
        request = 'SELECT ' + propertyName + ' FROM NCR WHERE ID==\"'+ncrID+'"'
        self.cur.execute(request)
        return self.cur.fetchall()[0][0]

    # Get steps of the LAST version of reportName
    def getReportStepsBySheet(self, reportName, sheetName):
        request = 'SELECT * FROM TestStep WHERE TestSheetName==\"'+reportName+'\" and TestSheet==\"' + sheetName + '\"'
        self.cur.execute(request)
        return self.cur.fetchall()



    def createNCR(self, ncrReportName, ncrId,ncrType,ncrSubgroup,ncrSsy,ncrEqtName,ncrDescription,ncrStatus,ncrLocation,ncrRoom,ncrStage,ncrEventReference,ncrOpenDate,ncrCategory,ncrOtherParties,ncrNCRelated,ncrSafetyRelated,ncrIssuedBy,ncrSolvedBy,ncrTargetDate,ncrTargetPhase,ncrActualDate,ncrActionTaken,ncrClosedBy,ncrAckDateOtherParty,ncrAckDatePIC,ncrRemarks):
        print("Create NCR " + str(ncrId))
        request = 'INSERT INTO NCR VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        self.cur.execute(request, (ncrReportName, ncrId,ncrType,ncrSubgroup,ncrSsy,ncrEqtName,ncrDescription,ncrStatus,ncrLocation,ncrRoom,ncrStage,ncrEventReference,ncrOpenDate,ncrCategory,ncrOtherParties,ncrNCRelated,ncrSafetyRelated,ncrIssuedBy,ncrSolvedBy,ncrTargetDate,ncrTargetPhase,ncrActualDate,ncrActionTaken,ncrClosedBy,ncrAckDateOtherParty,ncrAckDatePIC,ncrRemarks))
        self.con.commit()

    def getAvailableToolsInfo(self):
        # print("Getting info for report : " + reportName)
        request = 'SELECT * FROM Tools'
        self.cur.execute(request)
        return self.cur.fetchall()

    def getNCRDetails(self, ncrID):
        # print("Getting info for report : " + reportName)
        request = 'SELECT * FROM NCR WHERE ID==\"'+ncrID+'"'
        self.cur.execute(request)
        return self.cur.fetchall()[0]

    def getReportHeaders(self):
        request = 'PRAGMA table_info(TestReport)'
        self.cur.execute(request)
        return self.cur.fetchall()

    def getStepHeaders(self):
        request = 'PRAGMA table_info(TestStep)'
        self.cur.execute(request)
        return self.cur.fetchall()

    def getTablePropertyCol(self, table, property):
        request = 'PRAGMA table_info(' + table + ')'
        # print(request)
        self.cur.execute(request)
        for header in self.cur.fetchall():
            # print(header)
            if header[1] == property:
                return header[0]

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

    
