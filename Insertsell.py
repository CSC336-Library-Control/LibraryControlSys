from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import *


class Ui_Insertsell(object):
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()

    def setupUi(self, Insertsell):
        Insertsell.setObjectName("Insertsell")
        Insertsell.resize(605, 362)
        self.pushButton = QtWidgets.QPushButton(Insertsell)
        self.pushButton.setGeometry(QtCore.QRect(460, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Insertsell)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 270, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Insertsell)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 270, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(Insertsell)
        self.widget.setGeometry(QtCore.QRect(120, 100, 281, 121))
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

        self.retranslateUi(Insertsell)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_3.clicked.connect(Insertsell.close)
        QtCore.QMetaObject.connectSlotsByName(Insertsell)

        self.pushButton_2.clicked.connect(lambda: self.insertsell())

    def retranslateUi(self, Insertsell):
        _translate = QtCore.QCoreApplication.translate
        Insertsell.setWindowTitle(_translate("Insertsell", "Sell Book"))
        self.pushButton.setText(_translate("Insertsell", "Clear"))
        self.pushButton_2.setText(_translate("Insertsell", "Submit"))
        self.pushButton_3.setText(_translate("Insertsell", "Exit"))
        self.label.setText(_translate("Insertsell", "ISBN"))
        self.label_2.setText(_translate("Insertsell", "Price"))
        self.label_3.setText(_translate("Insertsell", "Quantity"))

    def insertsell(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')
        self.cursor = self.db.cursor()
        sql = "use library"
        self.cursor.execute(sql)

        isbn = self.lineEdit.text()
        price = self.lineEdit_2.text()
        sell_num = self.lineEdit_3.text()

        print(isbn, price, sell_num)
        sql = "insert into sell(isbn, price, AlreadySold)  values('%s','%d','%d')" % \
              (isbn, int(price), int(sell_num))
        self.execute_sql(sql)
        self.cursor.close()
