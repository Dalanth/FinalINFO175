#!/usr/bin/pythonss
# ­*­ coding: utf­8 ­*­
from PySide import QtGui, QtCore 
import controller
from form import Ui_Form

class Form(QtGui.QDialog):

	def __init__(self, parent=None, common_name=None):
        
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_Form()
		self.ui.setupUi(self)
		if common_name is None:
			self.ui.btn_done.clicked.connect(self.add)
		else:
			self.setWindowTitle(u"Editar animal")
			self.ui.btn_add.clicked.connect(self.edit)
		self.ui.btn_open.clicked.connect(self.abrir)
		self.ui.btn_cancel.clicked.connect(self.cancel)


	def add(self):
		#Add a new animal
		print "agregar animal"
		Name = self.ui.common_name.toPlainText()
                CiName = self.ui.cientific_name.toPlainText()
                datos=self.ui.data.toPlainText()
                tipo=None
                result = controller.add_animal(Name, CiName, datos, tipo)
                if result:
                        self.reject()
                        print "se agrego el agrego animal exitosamente"
                else:
                        self.ui.message.setText("Hubo un problema al intentar agregar el animal")

        def edit(self):
                #Edit an existent animal in the database
                print "edito animal"
        def abrir(self):
                #abre ventana para buscar imagen en el directorio
                NameImage  =  QtGui.QFileDialog . getOpenFileName (self,"Abrir imagen" , "/ home" , "*.png *.jpg *.bmp")
                print NameImage
                print "abrir imagen"

        def cancel(self):
                #Cancel the operation on the ui form
                self.reject()

        def load_types(self):
                #Carga los tipos de animales en el combobox
                types = controller.get_types()
                self.ui.typeBox.addItem("Todos", -1)
                for type1 in types: #Agrega los tipos al combobox
                    self.ui.typeBox.addItem(type1["nombre"], type1["id_tipo"])
                self.ui.typeBox.setEditable(False)
