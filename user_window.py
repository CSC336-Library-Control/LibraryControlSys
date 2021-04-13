from pymysql import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication,QInputDialog, QLineEdit, QMainWindow, QWidget
import sys
from Insertbook import *
from Insertpurchase import *
from Insertsell import *
from Insertdel import *
from searchbook import *
from insert_addreader import *
from Insert_delreader import *
from searchreader import *
from Insert_return import *
from searchborrowAndreturn import *

class Ui_user_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 111, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.see_book_info = QtWidgets.QPushButton(self.layoutWidget)
        self.see_book_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_book_info.setObjectName("see_book_info")
        self.verticalLayout.addWidget(self.see_book_info)
        self.see_reader_info = QtWidgets.QPushButton(self.layoutWidget)
        self.see_reader_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_reader_info.setObjectName("see_reader_info")
        self.verticalLayout.addWidget(self.see_reader_info)
        self.see_borrow_info = QtWidgets.QPushButton(self.layoutWidget)
        self.see_borrow_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_borrow_info.setObjectName("see_borrow_info")
        self.verticalLayout.addWidget(self.see_borrow_info)
        self.exit = QtWidgets.QPushButton(self.layoutWidget)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setObjectName("exit")
        self.verticalLayout.addWidget(self.exit)
        self.borrow = QtWidgets.QFrame(self.centralwidget)
        self.borrow.setGeometry(QtCore.QRect(210, 40, 701, 411))
        self.borrow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.borrow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.borrow.setObjectName("borrow")
        self.pushButton_3 = QtWidgets.QPushButton(self.borrow)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 60, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_6 = QtWidgets.QPushButton(self.borrow)
        # self.pushButton_6.setGeometry(QtCore.QRect(570, 130, 93, 28))
        # self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.borrow)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 210, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.borrow_info = QtWidgets.QTableView(self.borrow)
        self.borrow_info.setGeometry(QtCore.QRect(50, 40, 481, 311))
        self.borrow_info.setObjectName("borrow_info")
        # self.pushButton_8 = QtWidgets.QPushButton(self.borrow)
        # self.pushButton_8.setGeometry(QtCore.QRect(570, 280, 93, 28))
        # self.pushButton_8.setObjectName("pushButton_8")
        self.label_3 = QtWidgets.QLabel(self.borrow)
        self.label_3.setGeometry(QtCore.QRect(250, 10, 72, 15))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.borrow)
        self.radioButton.setGeometry(QtCore.QRect(180, 370, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.borrow)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 370, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.book = QtWidgets.QWidget(self.centralwidget)
        self.book.setEnabled(True)
        self.book.setGeometry(QtCore.QRect(198, 40, 700, 411))
        self.book.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.book.setObjectName("book")
        self.label = QtWidgets.QLabel(self.book)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(270, 10, 91, 20))
        self.label.setObjectName("label")
        self.layoutWidget1 = QtWidgets.QWidget(self.book)
        self.layoutWidget1.setGeometry(QtCore.QRect(580, 20, 101, 371))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.del_book = QtWidgets.QPushButton(self.layoutWidget1)
        self.del_book.setObjectName("del_book")
        self.verticalLayout_2.addWidget(self.del_book)
        self.purchasebook = QtWidgets.QPushButton(self.layoutWidget1)
        self.purchasebook.setObjectName("purchasebook")
        self.verticalLayout_2.addWidget(self.purchasebook)
        self.sellbook = QtWidgets.QPushButton(self.layoutWidget1)
        self.sellbook.setEnabled(True)
        self.sellbook.setObjectName("sellbook")
        self.verticalLayout_2.addWidget(self.sellbook)
        self.search_book = QtWidgets.QPushButton(self.layoutWidget1)
        self.search_book.setObjectName("search_book")
        self.verticalLayout_2.addWidget(self.search_book)
        self.book_info = QtWidgets.QTableView(self.book)
        self.book_info.setGeometry(QtCore.QRect(30, 40, 531, 351))
        self.book_info.setObjectName("book_info")
        self.reader = QtWidgets.QFrame(self.centralwidget)
        self.reader.setGeometry(QtCore.QRect(190, 40, 761, 411))
        self.reader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reader.setObjectName("reader")
        self.pushButton_2 = QtWidgets.QPushButton(self.reader)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 50, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.reader)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 140, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.reader)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 240, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.readerInfo = QtWidgets.QTableView(self.reader)
        self.readerInfo.setGeometry(QtCore.QRect(20, 50, 541, 311))
        self.readerInfo.setObjectName("readerInfo")
        self.label_2 = QtWidgets.QLabel(self.reader)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1315, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #
        self.reader.setVisible(False)
        self.borrow.setVisible(False)
        self.retranslateUi(MainWindow)
        self.exit.clicked.connect(MainWindow.close)
        self.see_book_info.clicked.connect(self.book.show)
        self.see_book_info.clicked.connect(self.reader.hide)
        self.see_book_info.clicked.connect(self.borrow.hide)
        self.see_reader_info.clicked.connect(self.reader.show)
        self.see_reader_info.clicked.connect(self.borrow.hide)
        self.see_borrow_info.clicked.connect(self.borrow.show)
        self.see_borrow_info.clicked.connect(self.reader.hide)
        self.see_borrow_info.clicked.connect(self.book.hide)
        self.see_reader_info.clicked.connect(self.book.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """pushbutton"""
        self.see_book_info.clicked.connect(lambda: self.get_book_info())
        self.see_reader_info.clicked.connect(lambda: self.get_reader_info())
        self.radioButton.clicked.connect(lambda: self.get_borrow_info())
        self.radioButton_2.clicked.connect(lambda: self.get_return_info())
        
        childwindow_addbook = child_addbok()
        childwindow_insertpurchase = child_purchase_book()
        childwindow_insertsell = child_sellbook()
        childwindow_insertdel = child_delbook()
        childwindow_searchbook = child_searchbook()
        childwindow_addreader = child_addreader()
        childwindow_delreader = child_delreader()
        childwindow_searchreader = child_searchreader()
        childwindow_insertReturnAndBorrow = child_insertReturnAndBorrow()
        childwindow_searchBorrowAndReturn = child_searchReturnAndBorrow()

        self.pushButton.clicked.connect(lambda: childwindow_addbook.show())
        self.purchasebook.clicked.connect(lambda: childwindow_insertpurchase.show())
        self.sellbook.clicked.connect(lambda: childwindow_insertsell.show())
        self.del_book.clicked.connect(lambda: childwindow_insertdel.show())
        self.search_book.clicked.connect(lambda: childwindow_searchbook.show())
        self.pushButton_2.clicked.connect(lambda: childwindow_addreader.show())
        self.pushButton_4.clicked.connect(lambda: childwindow_delreader.show())
        self.pushButton_5.clicked.connect(lambda: childwindow_searchreader.show())
        self.pushButton_3.clicked.connect(lambda: childwindow_insertReturnAndBorrow.show())
        self.pushButton_7.clicked.connect(lambda:childwindow_searchBorrowAndReturn.show())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Control System"))
        self.see_book_info.setText(_translate("MainWindow", "Book Info"))
        self.see_reader_info.setText(_translate("MainWindow", "Reader Info"))
        self.see_borrow_info.setText(_translate("MainWindow", "Lending Info"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.pushButton_3.setText(_translate("MainWindow", "Issue Book"))
        # self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_7.setText(_translate("MainWindow", "Lending Record"))
        # self.pushButton_8.setText(_translate("MainWindow", "Return Record"))
        self.label_3.setText(_translate("MainWindow", "Lending Info"))

        self.label.setText(_translate("MainWindow", "Book Info"))
        self.pushButton.setText(_translate("MainWindow", "Add Book"))
        self.del_book.setText(_translate("MainWindow", "Delete Book"))
        self.purchasebook.setText(_translate("MainWindow", "Buyin Buok"))
        self.sellbook.setText(_translate("MainWindow", "Sell Book"))
        self.search_book.setText(_translate("MainWindow", "Search Book"))
        self.pushButton_2.setText(_translate("MainWindow", "Add User"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete User"))
        self.pushButton_5.setText(_translate("MainWindow", "Search User"))
        self.label_2.setText(_translate("MainWindow", "User Profile"))

    def get_borrow_info(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')

        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)
        sql = "select * from borrow;"
        self.cursor.execute(sql)

        data = self.cursor.fetchall()
        print(data)
        self.model = QtSql.QSqlTableModel()
        self.borrow_info.setModel(self.model)
        row = len(data)
        model = QtGui.QStandardItemModel(row, len(data[0]))
        col = len(data[0])
        for i in range(row):
            for j in range(len(data[0])):
                if j is 3:
                    model.setItem(i, j, QtGui.QStandardItem(data[i][j]))
                elif j is 1:
                    model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
                elif j is 0 or j is 2:
                    if data[i][j] is None:
                        model.setItem(i, j, QtGui.QStandardItem(str(0)))
                    else:
                        model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
        self.cursor.close()
        model.setHorizontalHeaderLabels(['BorrowId', 'BorrowDate', 'UserId', 'ISBN'])
        self.borrow_info.setModel(model)

        self.statusbar.showMessage("Query success！ Total " + str(row) + "data", 2000)


    def get_return_info(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')

        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)
        sql = "select * from returnofbook;"
        self.cursor.execute(sql)

        data = self.cursor.fetchall()
        print(data)
        self.model = QtSql.QSqlTableModel()
        self.borrow_info.setModel(self.model)
        row = len(data)
        model = QtGui.QStandardItemModel(row, len(data[0]))
        col = len(data[0])
        for i in range(row):
            for j in range(len(data[0])):
                if j is 3:
                    model.setItem(i, j, QtGui.QStandardItem(data[i][j]))
                elif j is 1:
                    model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
                elif j is 0 or j is 2:
                    if data[i][j] is None:
                        model.setItem(i, j, QtGui.QStandardItem(str(0)))
                    else:
                        model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
        self.cursor.close()
        model.setHorizontalHeaderLabels(['ReturnId', 'ReturnDate', 'UserId', 'ISBN'])
        self.borrow_info.setModel(model)

        self.statusbar.showMessage("Query success！ Total " + str(row) + "data", 2000)

    def get_book_info(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')
        print(123)

        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)
        self.model = QtSql.QSqlTableModel()
        self.book_info.setModel(self.model)
        sql = "SELECT * FROM book"
        self.cursor.execute(sql)

        data = self.cursor.fetchall()
        print(data)
        sql = " select ISBN,TotalNum from collectionofbook;"
        self.cursor.execute(sql)
        booknum_data = self.cursor.fetchall()
        print(booknum_data)

        row = len(data)
        col = len(data[0])
        flag = False
        currentLocation = 0
        MergedList = [[] for x in range(row)]
        for i in range(row):
            for j in range(len(booknum_data)):
                if booknum_data[j][0] == data[i][0]:
                    flag = True
                    currentLocation = j
                    break
            if flag is True:
                for x in range(col):
                    MergedList[i].append(data[i][x])
                MergedList[i].append(booknum_data[currentLocation][1])
            else:
                for x in range(col):
                    MergedList[i].append(data[i][x])
                MergedList[i].append(0)
            flag = False
        print(MergedList)

        model = QtGui.QStandardItemModel(row, len(MergedList[0]))

        for i in range(row):
            for j in range(len(MergedList[0])):
                if j is not 3 and j is not 4:
                    model.setItem(i, j, QtGui.QStandardItem(MergedList[i][j]))
                else:
                    model.setItem(i, j, QtGui.QStandardItem(str(MergedList[i][j])))

        model.setHorizontalHeaderLabels(['ISBN', "Book Name", "Author", "Price", "Stock"])
        self.book_info.setModel(model)
        self.statusbar.showMessage("Query success！ Total " + str(row) + "data", 2000)

    def get_reader_info(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')

        self.cursor = self.db.cursor()
        self.model_1 = QtSql.QSqlTableModel()
        self.readerInfo.setModel(self.model_1)
        sql = "use Library"
        self.cursor.execute(sql)
        sql = "select * from reader"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        row = len(data)
        col = len(data[0])
        print(data)
        model = QtGui.QStandardItemModel(row, col)
        for i in range(row):
            for j in range(col):
                if j is not 0 and j is not 3:
                    model.setItem(i, j, QtGui.QStandardItem(data[i][j]))
                else:
                    model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
        model.setHorizontalHeaderLabels(['ReaderID', "Name", "Sex", "Age", "Tel"])
        self.readerInfo.setModel(model)
        self.statusbar.showMessage("Query success！ Total " + str(row) + "data", 2000)



class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_user_window()
        self.UI.setupUi(self)


class child_addbok(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_InputBookinfo()
        self.UI.setupUi(self)

class child_purchase_book(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UI = Ui_insertpurchase()
        self.UI.setupUi(self)


class child_sellbook(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UI = Ui_Insertsell()
        self.UI.setupUi(self)

class child_delbook(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UI = Ui_delbook()
        self.UI.setupUi(self)

class child_searchbook(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_searchbook()
        self.UI.setupUi(self)

class child_addreader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_addreader()
        self.UI.setupUi(self)


class child_delreader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_delreader()
        self.UI.setupUi(self)

class child_searchreader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_searchreader()
        self.UI.setupUi(self)

class child_insertReturnAndBorrow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_InsertReturnAndBorrow()
        self.UI.setupUi(self)


class child_searchReturnAndBorrow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_searchBorrowInfo()
        self.UI.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    childwindow = child_addbok()


    window.show()
    sys.exit(app.exec_())