# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Jun 27 11:56:40 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(600, 10, 271, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_add.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_edit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_edit.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.btn_delete = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_delete.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 49, 861, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.search.setMinimumSize(QtCore.QSize(450, 25))
        self.search.setMaximumSize(QtCore.QSize(450, 25))
        self.search.setText("")
        self.search.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setMinimumSize(QtCore.QSize(180, 25))
        self.label.setMaximumSize(QtCore.QSize(180, 25))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.searchBox = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.searchBox.setMinimumSize(QtCore.QSize(200, 0))
        self.searchBox.setMaximumSize(QtCore.QSize(200, 25))
        self.searchBox.setObjectName("searchBox")
        self.horizontalLayout_2.addWidget(self.searchBox)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 90, 861, 462))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.table = QtGui.QWidget(self.horizontalLayoutWidget_3)
        self.table.setMinimumSize(QtCore.QSize(500, 460))
        self.table.setMaximumSize(QtCore.QSize(500, 460))
        self.table.setObjectName("table")
        self.horizontalLayout_3.addWidget(self.table)
        self.showInfo = QtGui.QWidget(self.horizontalLayoutWidget_3)
        self.showInfo.setMaximumSize(QtCore.QSize(350, 460))
        self.showInfo.setObjectName("showInfo")
        self.horizontalLayout_3.addWidget(self.showInfo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add.setText(QtGui.QApplication.translate("MainWindow", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("MainWindow", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.search.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Buscar animal", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Buscar por tipo:", None, QtGui.QApplication.UnicodeUTF8))

