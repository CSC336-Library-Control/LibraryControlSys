from LoginUI import *
from LoginUI import userWindow
from user_window import User_MainWindow
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_MainWindow()
        user = userWindow()
        self.UI.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Login()
    mainWindow.show()
    sys.exit(app.exec_())
