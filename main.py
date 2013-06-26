# -*- coding: utf-8 -*-

import sqlite3
import Controller
import sys
from PySide import QtGui, QtCore
from mainwindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        #derp

def run():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__=='__main__':
    run()
