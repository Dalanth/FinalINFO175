#!/usr/bin/python
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
		print "agrego animal"

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
