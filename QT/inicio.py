#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from PySide.QtGui import *
import manejoUsuarios
import ventanaCredenciales
import visual


class Principal(QtGui.QWidget, ventanaCredenciales.Ui_ventanaCredenciales):

    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.move(450, 200)
        self.buttonAceptar.clicked.connect(self.sesion)
        self.buttonRegistro.clicked.connect(self.registro)
        self.main_layout = QtGui.QVBoxLayout(self)
        self.show()

    def sesion(self):
        nombre = self.lineNombre.text()
        usuarios = manejoUsuarios.existe(nombre)
        contrasenia = self.lineContrasenia.text()
        if (usuarios == []):
            msgbox = QMessageBox()
            msgbox.setText("Usuario/Contrasenia invalidos, para registrarse presione el boton 'Registrarse'")
            msgbox.exec_()
        else:
            if (usuarios[0][2] == contrasenia):
                msgbox = QMessageBox()
                msgbox.setText("Bienvenido" + nombre)
                msgbox.exec_()
                self.close()
            else:
                msgbox = QMessageBox()
                msgbox.setText("Usuario/Contrasenia invalidos, para registrarse presione el boton 'Registrarse'")
                msgbox.exec_()

    def registro(self):
        self.buttonRegistro.hide()
        self.setWindowTitle("Registro")


def run():
    app = QtGui.QApplication(sys.argv)
    form = Principal()
    form.show()
    app.exec_()

if __name__ == '__main__':
    run()