import datetime
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from pymysql import *


class Ui_InsertReturnAndBorrow(object):
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()


    def setupUi(self, Form):
        self.priority = 0
        Form.setObjectName("Form")
        Form.resize(593, 409)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 300, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(110, 250, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(310, 250, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(100, 70, 291, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.return_2 = QtWidgets.QLabel(self.widget)
        self.return_2.setObjectName("return_2")
        self.gridLayout.addWidget(self.return_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)




        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_3.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.radioButton.clicked.connect(lambda:self.Choose_borrow())
        self.radioButton_2.clicked.connect(lambda: self.Choose_return())
        self.pushButton_2.clicked.connect(lambda: self.insert_borrowAndReturn())


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Clear"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
        self.pushButton_3.setText(_translate("Form", "Exit"))
        self.radioButton.setText(_translate("Form", "Borrow"))
        self.radioButton_2.setText(_translate("Form", "Return"))
        self.return_2.setText(_translate("Form", "Reader ID"))
        self.label_2.setText(_translate("Form", "ISBN"))


    def insert_borrowAndReturn(self):
        borrow_time = datetime.datetime.now().strftime("%Y-%m-%d")
        reader_id = self.lineEdit.text()
        ISBN = self.lineEdit_2.text()

        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')
                          
        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)
        if self.priority is 0:
            self.statusbar.showMessage("Please select", 2000)
            print("capzuo")
        elif self.priority is 1:

            sql = "insert into borrow(BorrowTime, ReaderID, ISBN) values('%s','%d','%s')" % (
                borrow_time, int(reader_id), ISBN)
            self.execute_sql(sql)
        else:
            return_time = datetime.datetime.now().strftime("%Y-%m-%d")

            sql = "insert into returnofbook(returntime, readerid, isbn)  values('%s', '%s','%s')" % (
                return_time, int(reader_id), ISBN)
            self.execute_sql(sql)


    def Choose_borrow(self):
        self.priority = 1 #  Borrow
        self.statusbar.showMessage("借书", 2000)
    def Choose_return(self):
        self.priority = 2 # Return
        self.statusbar.showMessage("还书", 2000)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    test_ui = Ui_InsertReturnAndBorrow()
    test_ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
