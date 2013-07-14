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
        for tipo in types:
            self.ui.typeBox.addItem(tipo["nombre"], tipo["id_tipo"])
        if common_name is None:
            self.ui.btn_done.clicked.connect(self.add)
            if image is None:
                self.ui.btn_open.clicked.connect(self.open)
                self.ui.image.setPlainText(image)
        else:
            self.setWindowTitle(u"Editar animal")
            self.ui.btn_add.clicked.connect(self.edit)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.directory = QDir.root()
        self.display = QGraphicsView()
        self.ui.scrollArea.setWidget(self.display)
        #print (self.directory.currentPath()+"/Imagenes/")
        
    def add(self):
        #Add a new animal
        common = self.ui.common_name.toPlainText()
        cientific = self.ui.cientific_name.toPlainText()
        other = self.ui.data.toPlainText()
        tipo = self.ui.typeBox.currentText()
        id_type = controller_form.get_id_type(tipo)
        result = controller.add_animal(common, cientific, other, id_type)
        image = self.ui.image.toPlainText()
        #print image
        if image != "":
            #Agrega la imagen solo si existe una direccion
            id_animal = controller_form.get_id_animal(common)
            shutil.copy(image,(self.directory.currentPath()+"/Imagenes/"))
            Ifile = QFileInfo(image)
            controller_form.add_image_dir(id_animal,Ifile.fileName())

        if result:
            self.reject()
        else:
            self.ui.message.setText("Hubo un problema al intentar agregar el animal")

    def cancel(self):
        #Cancela la operación
        self.reject()

    def edit(self):
        #Edit an existent animal in the database
        print "edito animal"

    def open(self):
        #abre ventana para buscar imagen en el directorio
        dialog = QtGui.QFileDialog()
        imagen = dialog.getOpenFileName(self,"Abrir imagen" , "?" , "Image Files (*.png *.jpg *.bmp)")
        Ifile = QFileInfo(imagen[0])
        #print Ifile
        #print imagen[0]
        pix = controller_form.get_root_image(imagen[0])
        scene = QGraphicsScene()
        scene.addItem(pix)
        self.display.setScene(scene)
        self.ui.image.setPlainText(imagen[0])
