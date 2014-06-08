# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaRegistro.ui'
#
# Created: Thu Jun  5 12:01:30 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ventanaRegistro(object):
    def setupUi(self, ventanaRegistro):
        ventanaRegistro.setObjectName("ventanaRegistro")
        ventanaRegistro.resize(400, 243)
        self.lineNombre = QtGui.QLineEdit(ventanaRegistro)
        self.lineNombre.setGeometry(QtCore.QRect(170, 50, 161, 27))
        self.lineNombre.setObjectName("lineNombre")
        self.lineContrasenia = QtGui.QLineEdit(ventanaRegistro)
        self.lineContrasenia.setGeometry(QtCore.QRect(170, 110, 161, 27))
        self.lineContrasenia.setObjectName("lineContrasenia")
        self.buttonNombre = QtGui.QPushButton(ventanaRegistro)
        self.buttonNombre.setGeometry(QtCore.QRect(30, 50, 98, 27))
        self.buttonNombre.setObjectName("buttonNombre")
        self.buttoContrasenia = QtGui.QPushButton(ventanaRegistro)
        self.buttoContrasenia.setGeometry(QtCore.QRect(30, 110, 98, 27))
        self.buttoContrasenia.setObjectName("buttoContrasenia")
        self.pushButton = QtGui.QPushButton(ventanaRegistro)
        self.pushButton.setGeometry(QtCore.QRect(260, 200, 98, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ventanaRegistro)
        QtCore.QMetaObject.connectSlotsByName(ventanaRegistro)

    def retranslateUi(self, ventanaRegistro):
        ventanaRegistro.setWindowTitle(QtGui.QApplication.translate("ventanaRegistro", "Registro", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonNombre.setText(QtGui.QApplication.translate("ventanaRegistro", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.buttoContrasenia.setText(QtGui.QApplication.translate("ventanaRegistro", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ventanaRegistro", "Registrar", None, QtGui.QApplication.UnicodeUTF8))

