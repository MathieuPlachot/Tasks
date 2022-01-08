import sys
import time

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
)
from PyQt5.QtGui import (
    QIcon, QFont
)

from ui.pomoWindowUi import Ui_MainWindow

class pomoWindow(QMainWindow, Ui_MainWindow):



    def __init__(self, mainApp, parent=None):
        super().__init__(parent)
        self.mainApp = mainApp
        self.setupUi(self)
        self.connectSignalsSlots()
        self.refreshDataDisplay()
        # self.setColumnsSizes()
        self.tableWidget.resizeEvent = self.myResize
        self.hideEditTab()
        self.editedTaskID = 0

        # Build the calendar
        headerLabels = []
        headerLabels.append("Task Title")
        for i in range(28):
            col = i + 1
            headerLabels.append(str(i-7))
            self.planningTable.insertColumn(col)
        self.planningTable.setHorizontalHeaderLabels(headerLabels)

    def allCheckBoxClicked(self):
        if self.allCheckBox.isChecked():
            self.openCheckBox.setChecked(True)
            self.closedCheckBox.setChecked(True)
            self.refreshDataDisplay()

    def handleCheckBoxChange(self):
        if not self.openCheckBox.isChecked() or not self.closedCheckBox.isChecked():
            self.allCheckBox.setChecked(False)
        self.refreshDataDisplay()

    def myResize(self, arg):
        # print("resize")
        self.setColumnsSizes()

    def hideEditTab(self):
        self.tabWidget.setTabEnabled(3,False)
        self.tabWidget.setTabText(3,"")
    

    def openTaskEdition(self, taskID):
        self.editedTaskID = taskID
        self.tabWidget.setTabEnabled(3,True)
        self.tabWidget.setTabText(3,"Edit: " + str(self.mainApp.getTaskNameByID(taskID)))
        self.titleText.setText(str(self.mainApp.getTaskNameByID(taskID)))
        self.decriptionText.setPlainText(str(self.mainApp.getTaskDescriptionByID(taskID)))
        self.notesText.setPlainText(str(self.mainApp.getTaskNotesByID(taskID)))
        self.tabWidget.setCurrentWidget(self.tabWidget.widget(3))

    def connectSignalsSlots(self):
        # print("Nothing to connect")
        # self.action_Exit.triggered.connect(self.close)
        # self.action_Find_Replace.triggered.connect(self.findAndReplace)
        # self.action_About.triggered.connect(self.about)
        self.lineEdit.returnPressed.connect(self.addQuickTask)
        self.tableWidget.cellDoubleClicked.connect(self.taskDoubleClick)
        self.mainApp.socketDataReceived.connect(self.handleSocketData)
        self.tableWidget.cellClicked.connect(self.handleCellClicked)
        self.applyButton.clicked.connect(self.applyTaskEdition)
        self.cancelButton.clicked.connect(self.cancelEdition)
        self.closedCheckBox.clicked.connect(self.handleCheckBoxChange)
        self.openCheckBox.clicked.connect(self.handleCheckBoxChange)
        self.allCheckBox.clicked.connect(self.allCheckBoxClicked)
        # self.tableWidget.show.connect(self.setColumnsSizes)

    def applyTaskEdition(self):
        newTaskTitle = self.titleText.text()
        newTaskDesc = self.decriptionText.toPlainText()
        newTaskNotes = self.notesText.toPlainText()
        self.mainApp.setTaskTitle(self.editedTaskID, newTaskTitle)
        self.mainApp.setTaskDescription(self.editedTaskID, newTaskDesc)
        self.mainApp.setTaskNotes(self.editedTaskID, newTaskNotes)
        self.hideEditTab()

    def cancelEdition(self):
        self.hideEditTab()

    def handleSocketData(self):
        self.refreshDataDisplay()

    def taskDoubleClick(self):
        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row,0)
        taskID = int(item.text())
        self.startTimer(5, (taskID))

    def handleCellClicked(self,row,col):
        self.setColumnsSizes()
        # Find which action the user wants to do
        taskID = int(self.tableWidget.item(row,0).text())

        if col == 6:
            self.startTimer(1500,taskID)
        if col == 7:
            self.openTaskEdition(taskID)
        if col == 8:
            self.mainApp.completeTask(taskID)
        if col == 9:
            self.mainApp.deleteTask(taskID)


    def setColumnsSizes(self):
        # Get the width of the tablewidget
        tableWitdh = self.tableWidget.width() * 0.99
        # print("width " + str(tableWitdh))

        # Give each column 1/10 of the width
        self.tableWidget.setColumnHidden(0,True)
        print(0.48*tableWitdh)
        self.tableWidget.setColumnWidth(1,0.48*tableWitdh)
        self.tableWidget.setColumnWidth(2,0.1*tableWitdh)
        self.tableWidget.setColumnWidth(3,0.1*tableWitdh)
        self.tableWidget.setColumnWidth(4,0.1*tableWitdh)
        self.tableWidget.setColumnWidth(5,0.1*tableWitdh)
        self.tableWidget.setColumnWidth(6,0.03*tableWitdh)
        self.tableWidget.setColumnWidth(7,0.03*tableWitdh)
        self.tableWidget.setColumnWidth(8,0.03*tableWitdh)
        self.tableWidget.setColumnWidth(9,0.03*tableWitdh)

        taskTitleRatio = 0.3
        dayRatio = (1-taskTitleRatio) / 28
        print("Task " + str(taskTitleRatio))
        print("Day " + str(dayRatio))
        self.planningTable.setColumnWidth(0,taskTitleRatio*tableWitdh)
        for i in range(28):
            self.planningTable.setColumnWidth(i+1,dayRatio*tableWitdh)

        # Prevent resizing of last 3 columns and set their width
        # self.tableWidget.horizontalHeader().setSectionResizeMode(self.tableWidget.horizontalHeader().logicalIndex(6),2)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(self.tableWidget.horizontalHeader().logicalIndex(7),2)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(self.tableWidget.horizontalHeader().logicalIndex(8),2)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(self.tableWidget.horizontalHeader().logicalIndex(9),2)
        # self.tableWidget.setColumnWidth(6,20)
        # self.tableWidget.setColumnWidth(7,20)
        # self.tableWidget.setColumnWidth(8,20)
        # self.tableWidget.setColumnWidth(9,20)
            

    def refreshDataDisplay(self):
        # Clear any existing rows
        self.tableWidget.setRowCount(0)

        # Deactivate sorting
        sortingBefore = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        # Get the data from the main app
        tasksDataSet = []
        if self.openCheckBox.isChecked() and self.closedCheckBox.isChecked():
            tasksDataSet = self.mainApp.getTasksDataSet()
        elif self.openCheckBox.isChecked():
            tasksDataSet = self.mainApp.getAllOpenTasks()
        elif self.closedCheckBox.isChecked():
            tasksDataSet = self.mainApp.getAllClosedTasks()

        print(self.openCheckBox.isChecked())
        print(self.closedCheckBox.isChecked())
        for taskInfo in tasksDataSet:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            taskID = taskInfo[0]
            # print(taskID)
            
            taskIDItem = QTableWidgetItem(str(taskID))
            taskTitleItem = QTableWidgetItem(taskInfo[1])
            taskOpenDateItem = QTableWidgetItem(taskInfo[3])
            taskLoggedTimeItem = QTableWidgetItem(self.mainApp.calculateTaskLoggedTime(taskID))
            taskStatusItem = QTableWidgetItem(taskInfo[7])
            taskStatusItem.setTextAlignment(4)

            self.tableWidget.setItem(self.tableWidget.rowCount()-1,0,taskIDItem)
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,1,taskTitleItem)
            if taskInfo[7] == "DONE":
                # print("setfont")
                f = self.tableWidget.item(self.tableWidget.rowCount()-1,1).font()
                f.setStrikeOut(True)
                self.tableWidget.item(self.tableWidget.rowCount()-1,1).setFont(f)
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,2,taskOpenDateItem)
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,4,taskLoggedTimeItem)
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,5,taskStatusItem)
            # Create icons for QTableWidget
            tablePomoIconWidget = QTableWidgetItem()
            pomoIcon = QIcon("ui/icons/pomo_icon.png") 
            tablePomoIconWidget.setIcon(pomoIcon)
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,6,tablePomoIconWidget)
            # print("pomo icon for " + taskInfo[1])

            tableEditIconWidget = QTableWidgetItem()
            EditIcon = QIcon("ui/icons/edit_icon.png") 
            tableEditIconWidget.setIcon(EditIcon)
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,7,tableEditIconWidget)

            tableCompleteIconWidget = QTableWidgetItem()
            CompleteIcon = QIcon("ui/icons/complete_icon.png") 
            tableCompleteIconWidget.setIcon(CompleteIcon)
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,8,tableCompleteIconWidget)

            tableDeleteIconWidget = QTableWidgetItem()
            deleteIcon = QIcon("ui/icons/delete_icon.png") 
            tableDeleteIconWidget.setIcon(deleteIcon)
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,9,tableDeleteIconWidget)

        # Re-enable sorting
        self.tableWidget.setSortingEnabled(sortingBefore)
            
        # Refresh daily stats
        self.dailyFocusTimeLabel.setText("Focus Time: " + str(self.mainApp.getDailyFocusTime()))
        self.dailyTimersLabel.setText("Timers: " + str(self.mainApp.getDailyTimers()))

        # Refresh the calendar
        
            


        self.textBrowser.setText(self.mainApp.log())
            

    def addQuickTask(self):
        if self.lineEdit.text() != "":
            self.mainApp.addQuickTask(self.lineEdit.text())
            self.lineEdit.setText("")
            self.refreshDataDisplay()

    def startTimer(self, duration, taskID):
        self.mainApp.timerWindow.setDuration(duration, taskID)
        self.mainApp.timerWindow.show()

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )
