# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datos.ui'
#
# Created: Thu Jun 27 12:31:25 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Datos(object):
    def setupUi(self, Datos):
        Datos.setObjectName("Datos")
        Datos.resize(350, 460)
        self.label = QtGui.QLabel(Datos)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Datos)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Datos)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Datos)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.label_4.setObjectName("label_4")
        self.nom = QtGui.QLabel(Datos)
        self.nom.setGeometry(QtCore.QRect(180, 10, 161, 16))
        self.nom.setObjectName("nom")
        self.nomc = QtGui.QLabel(Datos)
        self.nomc.setGeometry(QtCore.QRect(180, 30, 161, 16))
        self.nomc.setObjectName("nomc")
        self.tipo = QtGui.QLabel(Datos)
        self.tipo.setGeometry(QtCore.QRect(180, 50, 161, 16))
        self.tipo.setObjectName("tipo")
        self.datos = QtGui.QLabel(Datos)
        self.datos.setGeometry(QtCore.QRect(10, 90, 331, 131))
        self.datos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.datos.setObjectName("datos")
        self.graphicsView = QtGui.QGraphicsView(Datos)
        self.graphicsView.setGeometry(QtCore.QRect(10, 240, 331, 211))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Datos)
        QtCore.QMetaObject.connectSlotsByName(Datos)

    def retranslateUi(self, Datos):
        Datos.setWindowTitle(QtGui.QApplication.translate("Datos", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Datos", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Datos", "Nombre cientifico:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Datos", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Datos", "Datos:", None, QtGui.QApplication.UnicodeUTF8))
        self.nom.setText(QtGui.QApplication.translate("Datos", "Derp", None, QtGui.QApplication.UnicodeUTF8))
        self.nomc.setText(QtGui.QApplication.translate("Datos", "Durr", None, QtGui.QApplication.UnicodeUTF8))
        self.tipo.setText(QtGui.QApplication.translate("Datos", "Herp", None, QtGui.QApplication.UnicodeUTF8))
        self.datos.setText(QtGui.QApplication.translate("Datos", "HEUAHEAUHEAUEHAUHEAEHA", None, QtGui.QApplication.UnicodeUTF8))

