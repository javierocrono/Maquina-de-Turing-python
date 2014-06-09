# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaCredenciales.ui'
#
# Created: Sun Jun  8 22:19:11 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ventanaCredenciales(object):
    def setupUi(self, ventanaCredenciales):
        ventanaCredenciales.setObjectName("ventanaCredenciales")
        ventanaCredenciales.resize(400, 300)
        self.buttonAceptar = QtGui.QPushButton(ventanaCredenciales)
        self.buttonAceptar.setGeometry(QtCore.QRect(170, 230, 98, 27))
        self.buttonAceptar.setObjectName("buttonAceptar")
        self.buttonCancelar = QtGui.QPushButton(ventanaCredenciales)
        self.buttonCancelar.setGeometry(QtCore.QRect(280, 230, 98, 27))
        self.buttonCancelar.setObjectName("buttonCancelar")
        self.lineNombre = QtGui.QLineEdit(ventanaCredenciales)
        self.lineNombre.setGeometry(QtCore.QRect(170, 40, 141, 27))
        self.lineNombre.setObjectName("lineNombre")
        self.lineContrasenia = QtGui.QLineEdit(ventanaCredenciales)
        self.lineContrasenia.setGeometry(QtCore.QRect(170, 100, 141, 27))
        self.lineContrasenia.setObjectName("lineContrasenia")
        self.label = QtGui.QLabel(ventanaCredenciales)
        self.label.setGeometry(QtCore.QRect(50, 40, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ventanaCredenciales)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 81, 17))
        self.label_2.setObjectName("label_2")
        self.buttonRegistro = QtGui.QPushButton(ventanaCredenciales)
        self.buttonRegistro.setGeometry(QtCore.QRect(30, 230, 98, 27))
        self.buttonRegistro.setObjectName("buttonRegistro")

        self.retranslateUi(ventanaCredenciales)
        QtCore.QMetaObject.connectSlotsByName(ventanaCredenciales)

    def retranslateUi(self, ventanaCredenciales):
        ventanaCredenciales.setWindowTitle(QtGui.QApplication.translate("ventanaCredenciales", "Inicio de sesion", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAceptar.setText(QtGui.QApplication.translate("ventanaCredenciales", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancelar.setText(QtGui.QApplication.translate("ventanaCredenciales", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ventanaCredenciales", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ventanaCredenciales", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonRegistro.setText(QtGui.QApplication.translate("ventanaCredenciales", "Registrarse", None, QtGui.QApplication.UnicodeUTF8))

