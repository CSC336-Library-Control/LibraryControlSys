# -*- coding: utf-8 -*-

import sys
from pymysql import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_InputBookinfo(object):
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()

    def setupUi(self, InputBookinfo):
        InputBookinfo.setObjectName("InputBookinfo")
        InputBookinfo.resize(516, 326)
        self.pushButton_2 = QtWidgets.QPushButton(InputBookinfo)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 64, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(InputBookinfo)
        self.widget.setGeometry(QtCore.QRect(80, 230, 301, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.widget1 = QtWidgets.QWidget(InputBookinfo)
        self.widget1.setGeometry(QtCore.QRect(90, 60, 291, 151))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.statusbar = QtWidgets.QStatusBar(InputBookinfo)
        self.statusbar.setObjectName("statusbar")
        InputBookinfo.setStatusBar(self.statusbar)

        self.retranslateUi(InputBookinfo)
        self.pushButton_2.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_3.clicked.connect(InputBookinfo.close)
        QtCore.QMetaObject.connectSlotsByName(InputBookinfo)

        self.pushButton.clicked.connect(lambda: self.get_book_info())

    def retranslateUi(self, InputBookinfo):
        _translate = QtCore.QCoreApplication.translate
        InputBookinfo.setWindowTitle(_translate("InputBookinfo", "Add Book"))
        self.pushButton_2.setText(_translate("InputBookinfo", "Clear"))
        self.pushButton.setText(_translate("InputBookinfo", "Submit"))
        self.pushButton_3.setText(_translate("InputBookinfo", "Exit"))
        self.label.setText(_translate("InputBookinfo", "Enter ISBN"))
        self.label_2.setText(_translate("InputBookinfo", "Book Name"))
        self.label_3.setText(_translate("InputBookinfo", "Author"))
        self.label_4.setText(_translate("InputBookinfo", "Price"))

    def get_book_info(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')

        self.cursor = self.db.cursor()
        sql = "use library"
        self.cursor.execute(sql)
        ISBN = self.lineEdit.text()
        bookName = self.lineEdit_2.text()
        author = self.lineEdit_3.text()
        price = self.lineEdit_4.text()
        sql = "SELECT * FROM book"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        original_row = len(data)
        try:
            sql = "insert into book(ISBN, bookname, author, price) values('%s','%s','%s','%d')" % (
                ISBN, bookName, author, int(price))
            self.execute_sql(sql)
        except Exception as err:
            print("err: " + err)
        sql = "SELECT * FROM book"
        self.cursor.execute(sql)

        data = self.cursor.fetchall()
        changed_row = len(data)
        if changed_row == original_row+1:
             self.statusbar.showMessage("Success，Please refresh", 2000)
        else:
            self.statusbar.showMessage("Fail，Please retry", 2000)
        self.cursor.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    test_ui = Ui_InputBookinfo()
    test_ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
