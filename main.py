#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import controller
import controller_form
import sys
import view_form
import os
from PySide import QtGui, QtCore
from PySide.QtCore import QDir, QFileInfo
from PySide.QtGui import *
from mainwindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):


    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_listeners()
        self.load_animals()
        self.load_types()
        self.create_folder()

    def about(self):
        """
        Ventana con los integrantes del grupo
        """
        message = u'Integrantes: \n- Nicolas Aravena\n- Sebastian Matamala\n- Arturo Reyes'
        self.ui.aboutUs = QtGui.QMessageBox.information(self, 'Acerca de Animales', message)

    def delete(self):
    	"""
        Elimina un animal de la base de datos mediante el controlador
        """
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        if index.row() == -1: 
            self.ui.errorMessageDialog = QtGui.QMessageBox.information(self, 'Error',
                                            u"Debe seleccionar el animal que desea eliminar",
                                            QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return False
        else:
            self.ui.confirmMessage = QtGui.QMessageBox.question(self, 'Eliminar animal',
                                    u"Está seguro que desea eliminar el animal seleccionado?",
                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if self.ui.confirmMessage == QtGui.QMessageBox.Yes:
                animal = model.index(index.row(), 1, QtCore.QModelIndex()).data()
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

    def create_folder(self):
    	"""
        Crea carpeta de imagenes si no existe
        """
        self.directory = QDir.root()
        if not os.path.exists(self.directory.currentPath()+"/images"):
            os.makedirs(self.directory.currentPath()+"/images")

    def load_types(self):
        """
        Carga los tipos de animales en el comboBox
        """
        types = controller.get_types()
        self.ui.searchBox.addItem("Todos", -1)
        for type1 in types: 
            self.ui.searchBox.addItem(type1["nombre"], type1["id_tipo"])
        self.ui.searchBox.setEditable(False)

    def load_animals(self, animals=None):
        """
        Carga los animales en pantalla
        """
        if animals is None:
            animals = controller.get_animals()
        self.model = QtGui.QStandardItemModel(len(animals), 1)        
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Imagen"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Animal"))
        r = 0
        self.display = QGraphicsView()
        for row in animals:
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre_comun'])

            index = self.model.index(r, 0, QtCore.QModelIndex())
            id_animal = controller_form.get_id_animal(animals[r][1])
            self.image = controller_form.get_image(id_animal)
            if self.image:
                self.path = QDir.currentPath() + "/images/" + self.image[0] + self.image[1]
                Ifile = QFileInfo(self.path)
                pixImage = controller_form.get_root_image(self.path)
                item = QGraphicsPixmapItem(pixImage.scaled(25,25))
                scene = QGraphicsScene()
                scene.addItem(item)
                self.display.setScene(scene)
                self.model.setData(index, self.display.setScene(scene))
            else:
                noimage = controller_form.no_image()
                item = QGraphicsPixmapItem(noimage.scaled(25,25))
                scene = QGraphicsScene()
                scene.addItem(item)
                self.display.setScene(scene)
                self.model.setData(index, self.display.setScene(scene))
            r += 1
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnWidth(0, 105)
        self.ui.tableView.setColumnWidth(1, 325)

    def load_products_by_search(self):
        """
        Carga los animales despues de aplicar un filtro
        """
        word = self.ui.search.text()
        animalslist = controller.get_animals_name()
        animals = controller.search_animal(word)
        self.load_animals(animals)
        completer = QtGui.QCompleter(animalslist, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setCompletionMode(QtGui.QCompleter.InlineCompletion)
        self.ui.search.setCompleter(completer)

    def load_animals_by_type(self):
        """
        Carga los animales por tipo
        """ 
        id_tipo = self.ui.searchBox.itemData(self.ui.searchBox.currentIndex())
        if id_tipo == -1: 
            animals = controller.get_animals()
        else: 
            animals = controller.get_animals_by_type(id_tipo)
        self.load_animals(animals)

    def set_listeners(self):
    	"""
        Sets up button listeners
        """
        self.ui.btn_delete.triggered.connect(self.delete)
        self.ui.add.triggered.connect(self.show_add_form)
        self.ui.edit.triggered.connect(self.show_edit_form)
        self.ui.quit.triggered.connect(self.close)
        self.ui.tableView.clicked.connect(self.display_data)
        self.ui.searchBox.activated[int].connect(self.load_animals_by_type)
        self.ui.search.textChanged.connect(self.load_products_by_search)
        self.ui.actionAcerca_de.triggered.connect(self.about)

    def show_add_form(self):
    	"""
        Muestra la ventana de agregar animales
        """
        form = view_form.Form(self)
        form.rejected.connect(self.load_animals)
        form.exec_()

    def show_edit_form(self):
    	"""
        Muestra la ventana de editar productos
        """
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        if index.row() == -1: 
            self.ui.msgBox = QtGui.QMessageBox.information(self, u'Error',
                                    u"Debe seleccionar el animal que desea editar")
            return False
        else:
            animal = model.index(index.row(), 1, QtCore.QModelIndex()).data()
            form = view_form.Form(self, animal)
            form.rejected.connect(self.load_animals)
            form.exec_()

    def display_data(self):
        """
        Modificado display para que muestre la imagen que se solicita
        """
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        data = model.index(index.row(),1,QtCore.QModelIndex()).data()
        animal = controller.get_animal(data)
        tipo = controller.get_type(data)
        id_animal = controller_form.get_id_animal(animal[1])
        pixImage = controller_form.get_image_pix(id_animal)
        self.ui.common.setText(animal[1])
        self.ui.cientific.setText(animal[2])
        self.ui.type.setText(tipo[0])
        self.ui.data.setWordWrap(True)
        self.ui.data.setText(animal[3])
        if pixImage:
            item = QGraphicsPixmapItem(pixImage.scaled(375,285))
            self.scene = QGraphicsScene()
            self.ui.graphicsView.setSceneRect(0,0,375,285)
            self.ui.graphicsView.setScene(self.scene)
            self.scene.addItem(item)
        else:
            noimage = controller_form.no_image()
            item = QGraphicsPixmapItem(noimage.scaled(375,285))
            self.scene = QGraphicsScene()
            self.ui.graphicsView.setSceneRect(0,0,375,285)
            self.ui.graphicsView.setScene(self.scene)
            self.scene.addItem(item)

def run():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    run()
