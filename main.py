#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import controller
import sys
import view_form
from PySide import QtGui, QtCore
from mainwindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_listeners()
        self.load_animals()


    def delete(self):
    #Calls on controller to delete a product row on the database
        print "estoy eliminando"


    def load_animals(self, animals=None):
        if animals is None:
            animals = controller.get_animals()
        self.model = QtGui.QStandardItemModel(len(animals), 1)        
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Animal"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Imágenes"))
        r = 0
        for row in animals:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['nombre_comun'])
            r = r+1
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnWidth(0, 150)
        self.ui.tableView.setColumnWidth(1, 330)


    def set_listeners(self):
    #Sets up button listeners
        self.ui.btn_delete.triggered.connect(self.delete)
        self.ui.add.triggered.connect(self.show_add_form)
        self.ui.edit.triggered.connect(self.show_edit_form)
        self.ui.quit.triggered.connect(self.close)
        self.ui.tableView.clicked.connect(self.display_data)


    def show_add_form(self):
    #Displays the add products screen
        form = view_form.Form(self)
        form.exec_()


    def show_edit_form(self):
    #Displays the edit products screen
        form = view_form.Form(self)
        form.exec_()
        self.ui.success.setText("Agregado")

    def display_data(self):
        model=self.ui.tableView.model()
        index=self.ui.tableView.currentIndex()
        data=model.index(index.row(), 0, QtCore.QModelIndex()).data()
        animal=controller.get_animal(data)
        tipo=controller.get_type(data)
        self.ui.common.setText(animal[1])
        self.ui.cientific.setText(animal[2])
        self.ui.type.setText(tipo[0])
        self.ui.data.setText(animal[3])
        


def run():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    run()
