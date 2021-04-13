
import sys

from PyQt5.QtWidgets import QApplication
from pymysql import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class Ui_searchBorrowInfo(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(801, 577)
        self.searchborrow = QtWidgets.QTableView(Form)
        self.searchborrow.setGeometry(QtCore.QRect(80, 230, 531, 271))
        self.searchborrow.setObjectName("searchborrow")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(140, 170, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 170, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(100, 30, 491, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(630, 30, 111, 141))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton_3.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)
        self.priority = 0
        self.radioButton.clicked.connect(lambda: self.borrow_choosed())
        self.radioButton_2.clicked.connect(lambda: self.return_choosed())
        self.pushButton_2.clicked.connect(lambda: self.getInfo())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Search Lending Info"))
        self.radioButton.setText(_translate("Form", "Borrow Record"))
        self.radioButton_2.setText(_translate("Form", "Return Record"))
        self.label_2.setText(_translate("Form", "Reader ID"))
        self.label.setText(_translate("Form", "ISBN"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
        self.pushButton.setText(_translate("Form", "Clear"))
        self.pushButton_3.setText(_translate("Form", "Exit"))

    def getInfo(self):
        if self.priority == 0:
            self.statusbar.showMessage("Please select")
        elif self.priority == 1:
            self.searchBorrowInfo()
            # self.pushButton_2.clicked.connect(lambda: self.searchBorrowInfo())
        elif self.priority == 2:
            self.searchReturnInfo()

    def searchBorrowInfo(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')
        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)
        ISBN = self.lineEdit.text()
        print(ISBN)
        readerID = self.lineEdit_2.text()
        flag = False
        if len(ISBN) == 0 and len(readerID) == 0:
            self.statusbar.showMessage("Please enter information")
        elif len(ISBN) != 0 and len(readerID) == 0:
            sql = "select * from borrow where isbn = '%s' " % ISBN
            flag = True
        elif len(ISBN) == 0 and len(readerID) != 0:
            sql = "select * from borrow where readerid = '%d' " % int(readerID)
            flag = True
        elif len(ISBN) != 0 and len(readerID) != 0:
            sql = "select * from borrow where read ='%d' and isbn = '%s' " %(int(readerID), ISBN)
            flag = True
        if flag:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print(data)
            self.model = QtSql.QSqlTableModel()
            self.searchborrow.setModel(self.model)
            row = len(data)
            model = QtGui.QStandardItemModel(row, len(data[0]))
            col = len(data[0])
            for i in range(row):
                for j in range(len(data[0])):
                    if j == 3:
                        model.setItem(i, j, QtGui.QStandardItem(data[i][j]))
                    elif j == 1:
                        model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
                    elif j == 0 or j == 2:
                        if data[i][j] == None:
                            model.setItem(i, j, QtGui.QStandardItem(str(0)))
                        else:
                            model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
            self.cursor.close()
            model.setHorizontalHeaderLabels(['BorrowId', 'BorrowDate', 'ReaderId', 'ISBN'])
            self.searchborrow.setModel(model)

            self.statusbar.showMessage("Query success！ Total " + str(row) + "data", 2000)

    def searchReturnInfo(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')

        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)
        ISBN = self.lineEdit.text()
        print(ISBN)
        readerID = self.lineEdit_2.text()
        flag = False
        if len(ISBN) == 0 and len(readerID) == 0:
            self.statusbar.showMessage("Please enter information")
        elif len(ISBN) != 0 and len(readerID) == 0:
            sql = "select * from returnofbook where isbn = '%s' " % ISBN
            flag = True
        elif len(ISBN) == 0 and len(readerID) != 0:
            sql = "select * from returnofbook where readerid = '%d' " % int(readerID)
            flag = True
        elif len(ISBN) != 0 and len(readerID) != 0:
            sql = "select * from returnofbook where read ='%d' and isbn = '%s' " % (int(readerID), ISBN)
            flag = True
        if flag:
            self.cursor.execute(sql)

            data = self.cursor.fetchall()
            print(data)
            self.model = QtSql.QSqlTableModel()
            self.searchborrow.setModel(self.model)
            row = len(data)
            model = QtGui.QStandardItemModel(row, len(data[0]))
            col = len(data[0])
            for i in range(row):
                for j in range(len(data[0])):
                    if j == 3:
                        model.setItem(i, j, QtGui.QStandardItem(data[i][j]))
                    elif j == 1:
                        model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
                    elif j == 0 or j == 2:
                        if data[i][j] == None:
                            model.setItem(i, j, QtGui.QStandardItem(str(0)))
                        else:
                            model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
            self.cursor.close()
            model.setHorizontalHeaderLabels(['ReturnId', 'ReturnDate', 'ReaderId', 'ISBN'])
            self.searchborrow.setModel(model)

            self.statusbar.showMessage("Query success！ Total " + str(row) + "data", 2000)

    def borrow_choosed(self):
        self.priority = 1

    def return_choosed(self):
        self.priority = 2
