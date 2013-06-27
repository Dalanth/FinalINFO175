# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created: Thu Jun 27 12:32:03 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Table(object):
    def setupUi(self, Table):
        Table.setObjectName("Table")
        Table.resize(500, 460)
        self.tableView = QtGui.QTableView(Table)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 480, 440))
        self.tableView.setMinimumSize(QtCore.QSize(480, 440))
        self.tableView.setMaximumSize(QtCore.QSize(480, 440))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Table)
        QtCore.QMetaObject.connectSlotsByName(Table)

    def retranslateUi(self, Table):
        Table.setWindowTitle(QtGui.QApplication.translate("Table", "Form", None, QtGui.QApplication.UnicodeUTF8))

