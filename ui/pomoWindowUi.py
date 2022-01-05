# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './pomoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1444, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Alstom")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Alstom")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.openCheckBox.setObjectName("openCheckBox")
        self.horizontalLayout.addWidget(self.openCheckBox)
        self.closedCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.closedCheckBox.setObjectName("closedCheckBox")
        self.horizontalLayout.addWidget(self.closedCheckBox)
        self.allCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.allCheckBox.setObjectName("allCheckBox")
        self.horizontalLayout.addWidget(self.allCheckBox)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_5.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dailyTimersLabel = QtWidgets.QLabel(self.groupBox_5)
        self.dailyTimersLabel.setObjectName("dailyTimersLabel")
        self.horizontalLayout_3.addWidget(self.dailyTimersLabel)
        self.dailyFocusTimeLabel = QtWidgets.QLabel(self.groupBox_5)
        self.dailyFocusTimeLabel.setObjectName("dailyFocusTimeLabel")
        self.horizontalLayout_3.addWidget(self.dailyFocusTimeLabel)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 1, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_6.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.weeklyTimersLabel = QtWidgets.QLabel(self.groupBox_6)
        self.weeklyTimersLabel.setObjectName("weeklyTimersLabel")
        self.horizontalLayout_4.addWidget(self.weeklyTimersLabel)
        self.weeklyFocusTimeLabel = QtWidgets.QLabel(self.groupBox_6)
        self.weeklyFocusTimeLabel.setObjectName("weeklyFocusTimeLabel")
        self.horizontalLayout_4.addWidget(self.weeklyFocusTimeLabel)
        self.verticalLayout_12.addWidget(self.groupBox_6)
        self.gridLayout_2.addLayout(self.verticalLayout_12, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setFamily("Alstom")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Task ID")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setItalic(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_13.addWidget(self.textBrowser)
        self.gridLayout_3.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.planningTable = QtWidgets.QTableWidget(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Alstom")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.planningTable.setFont(font)
        self.planningTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.planningTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.planningTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.planningTable.setAlternatingRowColors(True)
        self.planningTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.planningTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.planningTable.setGridStyle(QtCore.Qt.DashLine)
        self.planningTable.setObjectName("planningTable")
        self.planningTable.setColumnCount(1)
        self.planningTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.planningTable.setHorizontalHeaderItem(0, item)
        self.planningTable.horizontalHeader().setCascadingSectionResizes(True)
        self.planningTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.planningTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.titleText = QtWidgets.QLineEdit(self.groupBox_2)
        self.titleText.setObjectName("titleText")
        self.verticalLayout_9.addWidget(self.titleText)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout_11.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.decriptionText = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.decriptionText.setObjectName("decriptionText")
        self.verticalLayout_8.addWidget(self.decriptionText)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.verticalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.notesText = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.notesText.setObjectName("notesText")
        self.verticalLayout_10.addWidget(self.notesText)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.verticalLayout_11.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.applyButton = QtWidgets.QPushButton(self.tab_4)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_2.addWidget(self.applyButton)
        self.cancelButton = QtWidgets.QPushButton(self.tab_4)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1444, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro Todo"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Add Task ..."))
        self.groupBox.setTitle(_translate("MainWindow", "Filter"))
        self.openCheckBox.setText(_translate("MainWindow", "Open"))
        self.closedCheckBox.setText(_translate("MainWindow", "Done"))
        self.allCheckBox.setText(_translate("MainWindow", "All"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Today"))
        self.dailyTimersLabel.setText(_translate("MainWindow", "Timers:"))
        self.dailyFocusTimeLabel.setText(_translate("MainWindow", "Focus Time:"))
        self.groupBox_6.setTitle(_translate("MainWindow", "This Week"))
        self.weeklyTimersLabel.setText(_translate("MainWindow", "Timers:"))
        self.weeklyFocusTimeLabel.setText(_translate("MainWindow", "Focus Time:"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Task Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Open Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Due Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Logged Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Log"))
        self.planningTable.setSortingEnabled(True)
        item = self.planningTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Task Title"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Plannning"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Title"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Description"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Notes"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Edit: "))
