import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import json

from user_window import *
from admin_window import  *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)

        self.priority_flag = 2  # User Level
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 150, 231, 133))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 70, 151, 61))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 520, 211, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(lambda: self.check_user(MainWindow))
        self.statusbar.showMessage("Welcome to Library Control System", 5000)
        self.radioButton.clicked.connect(lambda: self.admin_login())
        self.radioButton_2.clicked.connect(lambda: self.user_login())
        self.pushButton.setShortcut('enter')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Control System"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.radioButton.setText(_translate("MainWindow", "Manager"))
        self.radioButton_2.setText(_translate("MainWindow", "User"))
        self.label_3.setText(_translate("MainWindow", "Library Control System"))
        self.label_4.setText(_translate("MainWindow", "Database Design"))

    def check_user(self, MainWindow):
        """Read account info from json"""
        #user_ui = User_MainWindow()
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(account)
        print("Role_Flag:"+str(self.priority_flag))

        file_name_1 = r"admin.txt"
        file_name_2 = r"employee.txt"
        with open(file_name_1, "r") as f:
            js = f.read()
            bookshop_admin = json.loads(js)
        f.close()
        print(bookshop_admin)
        with open(file_name_2, "r") as f:
            js = f.read()
            bookshop_employee = json.loads(js)

        if self.priority_flag == 0:
            if account in bookshop_admin.keys():
                if bookshop_admin[account] == password:
                    self.statusbar.showMessage("Manager login successfully", 2000)
                    admin.show()
                    MainWindow.close()
                elif len(password) == 0:
                    self.statusbar.showMessage("Please enter password", 2000)
                else:
                    self.statusbar.showMessage("Wrong password", 2000)
            elif len(account) == 0:
                self.statusbar.showMessage("Please enter username", 2000)
            else:
                self.statusbar.showMessage("Username does not exist", 2000)

        elif self.priority_flag == 1:
            if account in bookshop_employee.keys():
                if bookshop_employee[account] == password:
                    self.statusbar.showMessage("Employee login successfully", 2000)
                    user.show()
                    MainWindow.close()
                elif len(password) == 0:
                    self.statusbar.showMessage("Please enter password", 2000)
                else:
                    self.statusbar.showMessage("Wrong password", 2000)
            elif len(account) == 0:
                self.statusbar.showMessage("Please enter password", 2000)
            else:
                self.statusbar.showMessage("Username does not exist", 2000)

        else:
            self.statusbar.showMessage("Please choose User level", 2000)


    def admin_login(self):
        print("admin choosed")
        self.priority_flag = 0

    def user_login(self):
        print("employee chosed")
        self.priority_flag = 1


class login_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)


class userWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_user_window()
        self.UI.setupUi(self)

class adminWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_adminWindow()
        self.UI.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = login_window()
    user = userWindow()
    admin = adminWindow()
    login.show()
    sys.exit(app.exec_())