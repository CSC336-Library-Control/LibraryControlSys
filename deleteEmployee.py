from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import *


class Ui_Form(object):
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()
            print("Excute SQL failed，err：", err)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(422, 269)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 70, 61, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 70, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda:self.delEmployee())
        self.pushButton_2.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DeleteEmployee"))
        self.label.setText(_translate("Form", "EmployeeId"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.pushButton_2.setText(_translate("Form", "Exit"))

    def delEmployee(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')
        self.cursor = self.db.cursor()

        sql = "use Library;"
        self.cursor.execute(sql)
        if len(self.lineEdit.text()) is 0:
            self.statusbar.showMessage("Enter Id", 1500)
        else:
            sql = "select * from employee"
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            row = len(data)
            num = self.lineEdit.text()
            sql = "delete from employee where employeeId = %d ;" % int(num)
            self.execute_sql(sql)
            sql = "select * from employee"
            self.execute_sql(sql)
            data = self.cursor.fetchall()
            changed_row = len(data)
            if changed_row == row - 1:
                self.statusbar.showMessage("Deleted Successfuly，Please go back and refresh", 1500)
            else:
                self.statusbar.showMessage("Delete failed", 1500)
