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
        self.load_types()


    def delete(self):
    #Elimina un animal de la base de datos mediante el controlador
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        if index.row() == -1: #No hay fila seleccionada
            self.ui.errorMessageDialog = QtGui.QMessageBox.information(self, 'Error',
                                            u"Debe seleccionar el animal que desea eliminar",
                                            QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return False
        else:
            self.ui.confirmMessage = QtGui.QMessageBox.question(self, 'Eliminar animal',
                                    u"Está seguro que desea eliminar el animal seleccionado?",
                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if self.ui.confirmMessage == QtGui.QMessageBox.Yes:#Pide confirmacion
                animal = model.index(index.row(), 0, QtCore.QModelIndex()).data()
                if (controller.delete(animal)):
                    self.load_animals()
                    self.ui.msgBox = QtGui.QMessageBox.information(self, u'Atención',
                                    u"El animal fue eliminado con éxito")
                    return True
                else:
                    self.ui.errorMessageDialog = QtGui.QMessageBox.information(self, 'Error',
                                            u"Error al eliminar el animal",
                                            QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    return False


    def load_types(self):
        #Carga los tipos de animales en el combobox
        types = controller.get_types()
        self.ui.searchBox.addItem("Todos", -1)
        for type1 in types: #Agrega los tipos al combobox
            self.ui.searchBox.addItem(type1["nombre"], type1["id_tipo"])
        self.ui.searchBox.setEditable(False)


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


    def load_products_by_search(self):
        word = self.ui.search.text()
        animalslist = controller.get_animals_name()
        animals = controller.search_animal(word)
        self.load_animals(animals)
        completer = QtGui.QCompleter(animalslist, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setCompletionMode(QtGui.QCompleter.InlineCompletion)
        self.ui.search.setCompleter(completer)


    def load_animals_by_type(self):
        id_tipo = self.ui.searchBox.itemData(self.ui.searchBox.currentIndex())
        if id_tipo == -1: #si la opcion seleccionada es "todos", muestra todos los animales
            animals = controller.get_animals()
        else: #carga los animales por tipo
            animals = controller.get_animals_by_type(id_tipo)
        self.load_animals(animals)


    def set_listeners(self):
    #Sets up button listeners
        self.ui.btn_delete.triggered.connect(self.delete)
        self.ui.add.triggered.connect(self.show_add_form)
        self.ui.edit.triggered.connect(self.show_edit_form)
        self.ui.quit.triggered.connect(self.close)
        self.ui.tableView.clicked.connect(self.display_data)
        self.ui.searchBox.activated[int].connect(self.load_animals_by_type)
        self.ui.search.textChanged.connect(self.load_products_by_search)


    def show_add_form(self):
    #Muestra la ventana de agregar animales
        form = view_form.Form(self)
        form.rejected.connect(self.load_animals)
        form.exec_()
        self.ui.success.setText("Agregado")


    def show_edit_form(self):
    #Muestra la ventana de editar productos
        form = view_form.Form(self)
        form.exec_()
        self.ui.success.setText("Agregado")


    def display_data(self):
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        data = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        animal = controller.get_animal(data)
        tipo = controller.get_type(data)
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
