#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import controller
import sys
import view_form
from PySide import QtGui, QtCore
from mainwindow import Ui_MainWindow
from table import Ui_Table

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_listeners()
        #self.show()
        #durr


    def delete(self):
    #Calls on controller to delete a product row on the database
        print "estoy eliminando"


    def set_listeners(self):
    #Sets up button listeners
        self.ui.btn_delete.triggered.connect(self.delete)
        self.ui.add.triggered.connect(self.show_add_form)
        self.ui.edit.triggered.connect(self.show_edit_form)
        self.ui.quit.triggered.connect(self.close)


    def show_add_form(self):
    #Displays the add products screen
        form = view_form.Form(self)
        form.exec_()


    def show_edit_form(self):
    #Displays the edit products screen
        form = view_form.Form(self)
        form.exec_()



def run():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    run()
