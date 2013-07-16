#!/usr/bin/pythonss
# ­*­ coding: utf­8 ­*­
from PySide import QtGui, QtCore 
import controller
import controller_form
from form import Ui_Form
from PySide.QtCore import QDir, QCoreApplication, QFileInfo
from PySide.QtGui import *
import shutil

class Form(QtGui.QDialog):


    def __init__(self, parent=None, common_name=None, image=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        types = controller.get_types()
        self.directory = QDir.root()
        self.display = QGraphicsView()
        self.ui.scrollArea.setWidget(self.display)
        for tipo in types:
            self.ui.typeBox.addItem(tipo["nombre"], tipo["id_tipo"])

        if common_name is None:
            self.ui.btn_done.clicked.connect(self.add)
            if image is None:
                self.ui.image.setPlainText(image)
        else:
            self.setWindowTitle(u"Editar animal")
            self.common = common_name
            animal_data = controller.get_animal(common_name)
            self.ui.common_name.setPlainText(animal_data["nombre_comun"])
            self.ui.cientific_name.setText(animal_data["nombre_cientifico"])
            self.ui.data.setText(animal_data["datos"])
            tipo = self.ui.typeBox.currentText()
            id_type = controller_form.get_id_type(tipo)

            id_animal = controller_form.get_id_animal(common_name)
            self.image = controller_form.get_image(id_animal)
            if self.image:
				"""Muestra la imagen y la reduce"""
                self.path = QDir.currentPath() + "/images/" + self.image[0] + self.image[1]
                self.ui.image.setPlainText(self.path)
                Ifile = QFileInfo(self.path)
                pixImage = controller_form.get_root_image(self.path)
                item = QGraphicsPixmapItem(pixImage.scaled(100,100))
                scene = QGraphicsScene()
                scene.addItem(item)
                self.display.setScene(scene)
                self.ui.image.setPlainText(self.path)
            else:
                noimage = controller_form.no_image()
                item = QGraphicsPixmapItem(noimage.scaled(100,100))
                scene = QGraphicsScene()
                scene.addItem(item)
                self.display.setScene(scene)
                scene = QGraphicsScene()
                scene.addItem(item)
                self.display.setScene(scene)
                self.path = ""
                self.ui.image.setPlainText(self.path)

            self.ui.btn_done.clicked.connect(self.edit)
        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_open.clicked.connect(self.open)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        
    def add(self):
        """Add a new animal"""
        common = self.ui.common_name.toPlainText()
        if common == "":
            self.ui.msgBox = QtGui.QMessageBox.information(self, u'Atención!',
                                    u"Debe ingresar al menos el nombre común")
        else:
            cientific = self.ui.cientific_name.toPlainText()
            other = self.ui.data.toPlainText()
            tipo = self.ui.typeBox.currentText()
            id_type = controller_form.get_id_type(tipo)
            result = controller_form.add_animal(common, cientific, other, id_type)
            path = self.ui.image.toPlainText()
            if path != "":
                """Agrega la imagen solo si existe una direccion"""
                id_animal = controller_form.get_id_animal(common)
                shutil.copy(path,(self.directory.currentPath()+"/images/"))
                Ifile = QFileInfo(path)
                controller_form.add_image_dir(id_animal,Ifile.fileName())
            else:
                noimage = controller_form.no_image()
                item = QGraphicsPixmapItem(noimage.scaled(100,100))
                self.scene = QGraphicsScene()
                self.ui.graphicsView.setSceneRect(0,0,100,100)
                self.ui.graphicsView.setScene(self.scene)
                self.scene.addItem(item)
            if result:
                self.reject()
            else:
                self.ui.msgBox = QtGui.QMessageBox.information(self, u'Atención!',
                                    u"Hubo un problema al intentar agregar el animal")

    def cancel(self):
        """Cancela la operación"""
        self.reject()

    def edit(self):
        """Edit an existent animal in the database"""
        id_animal = controller_form.get_id_animal(self.common)
        common = self.ui.common_name.toPlainText()
        if common == "":
            self.ui.msgBox = QtGui.QMessageBox.information(self, u'Atención!',
                                    u"El nombre común no puede estar en blanco")
        else:
            cientific = self.ui.cientific_name.toPlainText()
            other = self.ui.data.toPlainText()
            tipo = self.ui.typeBox.currentText()
            id_type = controller_form.get_id_type(tipo)
            path = self.ui.image.toPlainText()
            result = controller_form.edit_animal(id_animal,common,cientific,other,id_type)
            if path != "":
                pixImage = controller_form.get_root_image(path)
                item = QGraphicsPixmapItem(pixImage.scaled(100,100))
                scene = QGraphicsScene()
                scene.addItem(item)
                self.display.setScene(scene)
                self.ui.image.setPlainText(path)
                Ifile = QFileInfo(path)
                if controller_form.search_image(id_animal,Ifile.fileName()):
                    controller_form.add_image_dir(id_animal,Ifile.fileName())
                    result = True
                else:
                    result = False
            else:
                noimage = controller_form.no_image()
                item = QGraphicsPixmapItem(noimage.scaled(100,100))
                scene = QGraphicsScene()
                scene.addItem(item)
                self.display.setScene(scene)
                self.ui.image.setPlainText(path)

            if result:
                self.reject()
            else:
                self.ui.msgBox = QtGui.QMessageBox.information(self, u'Atención!',
                                        u"Hubo un problema al intentar editar el animal, intentelo de nuevo")

    def open(self):
        """abre ventana para buscar imagen en el directorio"""
        dialog = QtGui.QFileDialog()
        imagen = dialog.getOpenFileName(self,"Abrir imagen" , "?" , "Image Files (*.png *.jpg *.bmp)")
        Ifile = QFileInfo(imagen[0])
        pixImage = controller_form.get_root_image(imagen[0])
        item = QGraphicsPixmapItem(pixImage.scaled(100,100))
        scene = QGraphicsScene()
        scene.addItem(item)
        scene.setSceneRect(0, 0, 100, 100)
        self.display.setScene(scene)
        if imagen[0] != "":
            self.ui.image.setPlainText(imagen[0])

    def delete(self):
	"""borra la imagen del animal, cuando se preciona Quitar"""
        path = self.ui.image.toPlainText()
        Ifile = QFileInfo(path)
        success = controller_form.del_image(Ifile.fileName())
        if not success:
            self.ui.errorMessageDialog = QtGui.QMessageBox.information(self, 'Error',
                                            u"Dirección incorrecta",
                                            QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        self.ui.image.setPlainText("")

