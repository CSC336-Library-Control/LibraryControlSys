# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from pymysql import *

class Ui_insertpurchase(object):

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()

    def setupUi(self, insertpurchase):
        insertpurchase.setObjectName("insertpurchase")
        insertpurchase.resize(589, 447)
        self.pushButton = QtWidgets.QPushButton(insertpurchase)
        self.pushButton.setGeometry(QtCore.QRect(460, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(insertpurchase)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 360, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(insertpurchase)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 360, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(insertpurchase)
        self.widget.setGeometry(QtCore.QRect(100, 120, 311, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.retranslateUi(insertpurchase)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_3.clicked.connect(insertpurchase.close)
        QtCore.QMetaObject.connectSlotsByName(insertpurchase)

        self.pushButton_2.clicked.connect(lambda: self.insert_purchase())

    def retranslateUi(self, insertpurchase):
        _translate = QtCore.QCoreApplication.translate
        insertpurchase.setWindowTitle(_translate("insertpurchase", "Buy Book"))
        self.pushButton.setText(_translate("insertpurchase", "Clear"))
        self.pushButton_2.setText(_translate("insertpurchase", "Submit"))
        self.pushButton_3.setText(_translate("insertpurchase", "Exit"))
        self.label.setText(_translate("insertpurchase", "ISBN"))
        self.label_2.setText(_translate("insertpurchase", "Quantity"))
        self.label_3.setText(_translate("insertpurchase", "Price"))

    def insert_purchase(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')

        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)

        isbn = self.lineEdit.text()
        price = self.lineEdit_2.text()
        purchase_num = self.lineEdit_3.text()

        print(isbn,price,purchase_num)
        sql = "insert into purchasebook(isbn, price, purchasenum) values('%s','%d','%d')" % \
              (isbn, int(price), int(purchase_num))
        self.execute_sql(sql)
        self.cursor.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    test_ui = Ui_insertpurchase()
    test_ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
