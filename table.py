# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created: Thu Jun 27 11:55:21 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 460)
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 480, 440))
        self.tableView.setMinimumSize(QtCore.QSize(480, 440))
        self.tableView.setMaximumSize(QtCore.QSize(480, 440))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

