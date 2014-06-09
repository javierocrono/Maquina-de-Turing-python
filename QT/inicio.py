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
        self.buttonCancelar.clicked.connect(self.cancelar)
        self.main_layout = QtGui.QVBoxLayout(self)

        self.enRegistro = False
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
                msgbox.setText("Bienvenido " + nombre)
                msgbox.exec_()
                self.close()
            else:
                msgbox = QMessageBox()
                msgbox.setText("Usuario/Contrasenia invalidos, para registrarse presione el boton 'Registrarse'")
                msgbox.exec_()

    def registro(self):
        if (self.enRegistro is False):
            self.buttonAceptar.hide()
            self.buttonRegistro.move(170,230)
            self.setWindowTitle("Registro")
            self.enRegistro =True
        else:
            nombre = self.lineNombre.text()
            if (nombre != ""):
                usuarios = manejoUsuarios.existe(nombre)
                contrasenia = self.lineContrasenia.text()
                if (usuarios == []):
                    msgbox = QMessageBox()
                    msgbox.setText("Usuario Valido")
                    msgbox.exec_()
                    if (contrasenia != ""):
                        manejoUsuarios.crear(nombre, contrasenia)
                        msgbox.setText("Usuario exitosamente Registrado")
                        msgbox.exec_()
                        self.buttonRegistro.move(30,230)
                        self.buttonAceptar.show()
                        self.enRegistro = False
                        self.setWindowTitle("Inicio de Sesion")
                else:
                    msgbox = QMessageBox()
                    msgbox.setText("Usuario Invalido")
                    msgbox.exec_()
            else:
                msgbox = QMessageBox()
                msgbox.setText("Usuario Invalido")
                msgbox.exec_()

    def cancelar(self):
        if (self.enRegistro is False):
            if (self.lineNombre.text() != "" or self.lineContrasenia.text() != ""):
                self.lineNombre.setText("")
                self.lineContrasenia.setText("")
            else:
                self.close()
        else:
            if (self.lineNombre.text() != "" or self.lineContrasenia.text() != ""):
                self.lineNombre.setText("")
                self.lineContrasenia.setText("")
            else:
                self.buttonRegistro.move(30, 230)
                self.buttonAceptar.show()
                self.enRegistro = False
                self.setWindowTitle("Inicio de Sesion")

def run():
    app = QtGui.QApplication(sys.argv)
    form = Principal()
    form.show()
    app.exec_()

if __name__ == '__main__':
    run()