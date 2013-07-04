#!/usr/bin/pythonss
# ­*­ coding: utf­8 ­*­
from PySide import QtGui, QtCore 
import controller
import controller_form
from form import Ui_Form

class Form(QtGui.QDialog):

    def __init__(self, parent=None, common_name=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui.Form()
        self.ui.setupUi(self)
        if common_name is None:
            self.ui.btn_done.clicked.connect(self.add)
        else:
            self.setWindowTitle(u"Editar animal")
            self.ui.btn_add.clicked.connect(self.edit)
        self.ui.btn_cancel.clicked.connect(self.cancel)


	def add(self):
		#Add a new animal
		print "agregar animal"
		Name = self.ui.common_name.toPlainText()
        CiName = self.ui.cientific_name.toPlainText()
        datos=self.ui.data.toPlainText()
        tipo=controller_form.get_id_type(self.ui.typeBox.currentText())
        result = controller.add_animal(Name, CiName, datos, tipo)
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
