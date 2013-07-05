#!/usr/bin/pythonss
# ­*­ coding: utf­8 ­*­
from PySide import QtGui, QtCore 
import controller
import controller_form
from form import Ui_Form
from PySide.QtCore import QDir, QCoreApplication

class Form(QtGui.QDialog):

    def __init__(self, parent=None, common_name=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        types = controller.get_types()
        for tipo in types:
            self.ui.typeBox.addItem(tipo["nombre"], tipo["id_tipo"])
        if common_name is None:
            self.ui.btn_done.clicked.connect(self.add)
        else:
            self.setWindowTitle(u"Editar animal")
            self.ui.btn_add.clicked.connect(self.edit)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_open.clicked.connect(self.abrir)
        self.directory = QDir()
        self.directory.currentPath()
        self.directory.mkdir("Imagenes")
        

    def add(self):
        #Add a new animal
        common = self.ui.common_name.toPlainText()
        cientific = self.ui.cientific_name.toPlainText()
        other = self.ui.data.toPlainText()
        tipo = self.ui.typeBox.currentText()
        id_type = controller_form.get_id_type(tipo)
        result = controller.add_animal(common, cientific, other, id_type)
        if result:
            self.reject()
        else:
            self.ui.message.setText("Hubo un problema al intentar agregar el animal")

    def edit(self):
        #Edit an existent animal in the database
        print "edito animal"


    def cancel(self):
        #Cancel the operation on the ui form
        self.reject()
    def abrir(self):
        #abre ventana para buscar imagen en el directorio
        NameImage = QtGui.QFileDialog . getOpenFileName (self,"Abrir imagen" , "/ home" , "*.png *.jpg *.bmp")
        print NameImage
        print "abrir imagen"

