from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import *

class Ui_delreader(object):
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 351)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 220, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 220, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(120, 110, 341, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton_3.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(lambda: self.delreader())
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Delete User"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
        self.pushButton_3.setText(_translate("Form", "Exit"))
        self.label.setText(_translate("Form", "User Id"))
        self.pushButton.setText(_translate("Form", "Clear"))

    def delreader(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')
        self.cursor = self.db.cursor()

        sql = "use Library"
        self.cursor.execute(sql)

        sql = "SELECT * FROM reader"
        self.cursor.execute(sql)
        
        data = self.cursor.fetchall()
        original_row = len(data)
        id = self.lineEdit.text()
        sql = "delete from reader where ReaderID = '%d' " % int(id)
        self.execute_sql(sql)
        sql = "SELECT * FROM reader"

        self.cursor.execute(sql)
        new_data = self.cursor.fetchall()
        new_row = len(new_data)
        if new_row == original_row+1:
             self.statusbar.showMessage("Success，Please refresh", 2000)
        else:
            self.statusbar.showMessage("Fail，Please retry", 2000)
        self.cursor.close()
