import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Merge import *


class MyMainWindow(QMainWindow, Ui_btnMerge):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMsg)

    def showMsg(self):
        print("pushButton")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
