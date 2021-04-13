import json
import sys
from pymysql import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMainWindow, QApplication
from insert_employee import *
from deleteEmployee import *


class Ui_adminWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.operator_2 = QtWidgets.QFrame(self.centralwidget)
        self.operator_2.setGeometry(QtCore.QRect(240, 40, 591, 331))
        self.operator_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.operator_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.operator_2.setObjectName("operator_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.operator_2)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 60, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.operator_2)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 110, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.radioButton = QtWidgets.QRadioButton(self.operator_2)
        self.radioButton.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.operator_2)
        self.radioButton_2.setGeometry(QtCore.QRect(310, 230, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.widget = QtWidgets.QWidget(self.operator_2)
        self.widget.setGeometry(QtCore.QRect(80, 50, 291, 91))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.emoloyee = QtWidgets.QFrame(self.centralwidget)
        self.emoloyee.setGeometry(QtCore.QRect(244, 37, 611, 361))
        self.emoloyee.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emoloyee.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emoloyee.setObjectName("emoloyee")
        self.pushButton_4 = QtWidgets.QPushButton(self.emoloyee)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 20, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.emoloyee)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 70, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        # self.pushButton_7 = QtWidgets.QPushButton(self.emoloyee)
        # self.pushButton_7.setGeometry(QtCore.QRect(470, 120, 93, 28))
        # self.pushButton_7.setObjectName("pushButton_7")
        # self.pushButton_8 = QtWidgets.QPushButton(self.emoloyee)
        # self.pushButton_8.setGeometry(QtCore.QRect(470, 170, 93, 28))
        # self.pushButton_8.setObjectName("pushButton_8")
        self.tableView = QtWidgets.QTableView(self.emoloyee)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 441, 301))
        self.tableView.setObjectName("tableView")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(90, 60, 101, 65))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.add_operator = QtWidgets.QPushButton(self.widget1)
        self.add_operator.setObjectName("add_operator")
        self.gridLayout.addWidget(self.add_operator, 0, 0, 1, 1)
        self.showEmployeeInfo = QtWidgets.QPushButton(self.widget1)
        self.showEmployeeInfo.setObjectName("showEmployeeInfo")
        self.gridLayout.addWidget(self.showEmployeeInfo, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.emoloyee.setVisible(False)
        self.retranslateUi(MainWindow)
        self.add_operator.clicked.connect(self.operator_2.show)
        self.add_operator.clicked.connect(self.emoloyee.hide)
        self.showEmployeeInfo.clicked.connect(self.operator_2.hide)
        self.showEmployeeInfo.clicked.connect(self.emoloyee.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.priority = 0
        childwindow_insertEmployee = child_insertEmployee()
        childwindow_delEmployee = child_delEmployee()

        self.radioButton.clicked.connect(lambda: self.choose_admin())
        self.radioButton_2.clicked.connect(lambda: self.choose_employee())
        self.pushButton_3.clicked.connect(lambda: self.add_operator_method())
        self.pushButton_5.clicked.connect(lambda:self.del_operator())
        self.showEmployeeInfo.clicked.connect(lambda:self.get_empolyee_info())
        self.pushButton_4.clicked.connect(lambda:childwindow_insertEmployee.show())
        self.pushButton_6.clicked.connect(lambda: childwindow_delEmployee.show())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manager"))
        self.pushButton_3.setText(_translate("MainWindow", "AddUser"))
        self.pushButton_5.setText(_translate("MainWindow", "DeleteUser"))
        self.radioButton.setText(_translate("MainWindow", "Manager"))
        self.radioButton_2.setText(_translate("MainWindow", "User"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton_4.setText(_translate("MainWindow", "AddEmployee"))
        self.pushButton_6.setText(_translate("MainWindow", "DeleteEmployee"))
      #  self.pushButton_7.setText(_translate("MainWindow", "SearchEmployee"))
      #  self.pushButton_8.setText(_translate("MainWindow", "ChangeProfile"))
        self.add_operator.setText(_translate("MainWindow", "Staff"))
        self.showEmployeeInfo.setText(_translate("MainWindow", "StaffProfile"))

    def add_operator_method(self):
        if self.priority is 0:
            self.statusbar.showMessage("Choose UserLevel")
        elif self.priority is 1:
            print(1)
            self.addOperator_admin()
        elif self.priority is 2:
            self.addOperator_employee()

    def del_operator(self):
        if self.priority is 0:
            self.statusbar.showMessage("Choose UserLevel")
        elif self.priority is 1:
            self.delOperator_admin()
        elif self.priority is 2:
            self.delOperator_employee()


    def addOperator_admin(self):
        file_name_1 = r"admin.txt"
        with open(file_name_1, "r") as f:
            js = f.read()
            admin = json.loads(js)
        f.close()
        id = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if id in admin.keys():
            self.statusbar.showMessage("Username already existed", 2000)
        else:
            admin[id] = pwd

            self.statusbar.showMessage("Success！",2000)
            jsOBJ = json.dumps(admin)
            with open(file_name_1, "w") as f:
                f.write(jsOBJ)
            f.close()

    def addOperator_employee(self):
        file_name_2 = r"employee.txt"
        with open(file_name_2, "r") as f:
            js = f.read()
            employee = json.loads(js)
        f.close()
        id = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if id in employee.keys():
            self.statusbar.showMessage("Username already exist", 2000)
        else:
            employee[id] = pwd
            self.statusbar.showMessage("Added Successfully！", 2000)
            jsOBJ = json.dumps(employee)
            with open(file_name_2, "w") as f:
                f.write(jsOBJ)
            f.close()

    def delOperator_admin(self):
        file_name_1 = r"admin.txt"
        with open(file_name_1, "r") as f:
            js = f.read()
            admin = json.loads(js)
        f.close()
        id = self.lineEdit.text()
        if id not in admin.keys():
            self.statusbar.showMessage("Username does not exist", 2000)
        else:
            del admin[id]
            self.statusbar.showMessage("Deleted successfully！", 2000)
            jsOBJ = json.dumps(admin)
            with open(file_name_1, "w") as f:
                f.write(jsOBJ)
            f.close()


    def delOperator_employee(self):
        file_name_2 = r"employee.txt"
        with open(file_name_2, "r") as f:
            js = f.read()
            employee = json.loads(js)
        f.close()
        id = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if id in employee.keys():
            self.statusbar.showMessage("Username does not exist", 2000)
        else:
            del employee[id]
            self.statusbar.showMessage("Deleted successfully！", 2000)
            jsOBJ = json.dumps(employee)
            with open(file_name_2, "w") as f:
                f.write(jsOBJ)
            f.close()

    def get_empolyee_info(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')

        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)
        sql = "select * from employee;"
        self.cursor.execute(sql)
        # data[i][j]
        data = self.cursor.fetchall()
        print(data)
        self.model = QtSql.QSqlTableModel()
        self.tableView.setModel(self.model)
        row = len(data)
        model = QtGui.QStandardItemModel(row, len(data[0]))
        col = len(data[0])
        for i in range(row):
            for j in range(len(data[0])):
                if j is 1 or j is 2 or j is 4:
                    model.setItem(i, j, QtGui.QStandardItem(data[i][j]))
                elif j is 0 or j is 3 or j is 5:
                    if data[i][j] is None:
                        model.setItem(i, j, QtGui.QStandardItem(str(0)))
                    else:
                        model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
        self.cursor.close()
        model.setHorizontalHeaderLabels(['EmployeeId', 'Name', 'Sex', 'Age', 'Tel', 'Salary'])
        self.tableView.setModel(model)

        self.statusbar.showMessage("Query Success！Total" + str(row) + "data", 2000)

    def choose_admin(self):
        self.priority = 1

    def choose_employee(self):
        self.priority = 2


class parentWindow_admin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_adminWindow()
        self.UI.setupUi(self)

class child_insertEmployee(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_insert_employee()
        self.UI.setupUi(self)

class child_delEmployee(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_Form()
        self.UI.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow_admin()
    window.show()
    sys.exit(app.exec_())
