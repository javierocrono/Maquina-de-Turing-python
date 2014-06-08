# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaCredenciales.ui'
#
# Created: Thu Jun  5 12:01:03 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ventanaCredenciales(object):
    def setupUi(self, ventanaCredenciales):
        ventanaCredenciales.setObjectName("ventanaCredenciales")
        ventanaCredenciales.resize(400, 276)
        self.buttonCancelarAceptar = QtGui.QDialogButtonBox(ventanaCredenciales)
        self.buttonCancelarAceptar.setGeometry(QtCore.QRect(30, 210, 341, 32))
        self.buttonCancelarAceptar.setOrientation(QtCore.Qt.Horizontal)
        self.buttonCancelarAceptar.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonCancelarAceptar.setObjectName("buttonCancelarAceptar")
        self.lineNombre = QtGui.QLineEdit(ventanaCredenciales)
        self.lineNombre.setGeometry(QtCore.QRect(180, 50, 161, 27))
        self.lineNombre.setObjectName("lineNombre")
        self.labelNombre = QtGui.QLabel(ventanaCredenciales)
        self.labelNombre.setGeometry(QtCore.QRect(30, 50, 131, 17))
        self.labelNombre.setObjectName("labelNombre")
        self.labelContrasenia = QtGui.QLabel(ventanaCredenciales)
        self.labelContrasenia.setGeometry(QtCore.QRect(30, 110, 131, 17))
        self.labelContrasenia.setObjectName("labelContrasenia")
        self.lineContrasenia = QtGui.QLineEdit(ventanaCredenciales)
        self.lineContrasenia.setGeometry(QtCore.QRect(180, 110, 161, 27))
        self.lineContrasenia.setObjectName("lineContrasenia")
        self.buttonRegistro = QtGui.QPushButton(ventanaCredenciales)
        self.buttonRegistro.setGeometry(QtCore.QRect(40, 210, 98, 27))
        self.buttonRegistro.setObjectName("buttonRegistro")

        self.retranslateUi(ventanaCredenciales)
        QtCore.QObject.connect(self.buttonCancelarAceptar, QtCore.SIGNAL("accepted()"), ventanaCredenciales.accept)
        QtCore.QObject.connect(self.buttonCancelarAceptar, QtCore.SIGNAL("rejected()"), ventanaCredenciales.reject)
        QtCore.QMetaObject.connectSlotsByName(ventanaCredenciales)

    def retranslateUi(self, ventanaCredenciales):
        ventanaCredenciales.setWindowTitle(QtGui.QApplication.translate("ventanaCredenciales", "Inicio de sesion", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNombre.setText(QtGui.QApplication.translate("ventanaCredenciales", "Nombre de Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.labelContrasenia.setText(QtGui.QApplication.translate("ventanaCredenciales", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonRegistro.setText(QtGui.QApplication.translate("ventanaCredenciales", "Registrarse", None, QtGui.QApplication.UnicodeUTF8))

