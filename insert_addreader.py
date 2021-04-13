from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import *


class Ui_addreader(object):
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(701, 431)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 320, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 320, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(160, 70, 311, 191))
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
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.lineEdit_3.clear)
        self.pushButton.clicked.connect(self.lineEdit_4.clear)
        self.pushButton.clicked.connect(self.lineEdit_5.clear)
        self.pushButton_3.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(lambda: self.insertreader())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Clear"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
        self.pushButton_3.setText(_translate("Form", "Exit"))
        self.label.setText(_translate("Form", "Reader ID"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Sex"))
        self.label_4.setText(_translate("Form", "Age"))
        self.label_5.setText(_translate("Form", "Tel"))

    def insertreader(self):
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
        name = self.lineEdit_2.text()
        sex = self.lineEdit_3.text()
        age = self.lineEdit_4.text()
        tel = self.lineEdit_5.text()
        print(id,name,sex,age,tel)
        sql ="insert into reader(readerid, readername, sex, age, tel) values ('%d','%s','%s','%d','%s')" % \
             (int(id),name,sex,int(age),tel)
        self.cursor.execute(sql)
        sql = "SELECT * FROM reader"
        self.cursor.execute(sql)
        self.cursor.connection.commit()

        new_data = self.cursor.fetchall()
        print(new_data)
        new_row = len(new_data)
        if new_row == original_row+1:
             self.statusbar.showMessage("Success，Please refresh", 2000)
        else:
            self.statusbar.showMessage("Fail，Please retry", 2000)
        self.cursor.close()







