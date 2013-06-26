# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Tue Jun 25 21:28:31 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(440, 457)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 218, 15))
        self.label.setObjectName("label")
        self.common_name = QtGui.QTextEdit(Form)
        self.common_name.setGeometry(QtCore.QRect(20, 40, 400, 25))
        self.common_name.setMinimumSize(QtCore.QSize(400, 25))
        self.common_name.setMaximumSize(QtCore.QSize(400, 25))
        self.common_name.setObjectName("common_name")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 218, 15))
        self.label_2.setObjectName("label_2")
        self.cientific_name = QtGui.QTextEdit(Form)
        self.cientific_name.setGeometry(QtCore.QRect(20, 90, 400, 25))
        self.cientific_name.setMinimumSize(QtCore.QSize(400, 25))
        self.cientific_name.setMaximumSize(QtCore.QSize(400, 25))
        self.cientific_name.setObjectName("cientific_name")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 218, 15))
        self.label_3.setObjectName("label_3")
        self.other = QtGui.QTextEdit(Form)
        self.other.setGeometry(QtCore.QRect(20, 140, 400, 100))
        self.other.setMinimumSize(QtCore.QSize(400, 100))
        self.other.setMaximumSize(QtCore.QSize(400, 100))
        self.other.setObjectName("other")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 152, 21))
        self.label_4.setObjectName("label_4")
        self.btn_open = QtGui.QPushButton(Form)
        self.btn_open.setGeometry(QtCore.QRect(20, 260, 81, 27))
        self.btn_open.setObjectName("btn_open")
        self.btn_delete = QtGui.QPushButton(Form)
        self.btn_delete.setGeometry(QtCore.QRect(110, 260, 81, 27))
        self.btn_delete.setObjectName("btn_delete")
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(20, 290, 401, 111))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btn_done = QtGui.QPushButton(Form)
        self.btn_done.setGeometry(QtCore.QRect(230, 410, 88, 27))
        self.btn_done.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_done.setObjectName("btn_done")
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(330, 410, 88, 27))
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Nombre común:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nombre científico:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Datos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Imagenes:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_open.setText(QtGui.QApplication.translate("Form", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("Form", "Quitar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_done.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

