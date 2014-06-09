# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar.ui'
#
# Created: Sun Jun  8 22:53:06 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddP(object):
    def setupUi(self, AddP):
        AddP.setObjectName("AddP")
        AddP.resize(414, 369)
        self.textNom = QtGui.QLineEdit(AddP)
        self.textNom.setGeometry(QtCore.QRect(190, 130, 113, 25))
        self.textNom.setObjectName("textNom")
        self.textDesc = QtGui.QLineEdit(AddP)
        self.textDesc.setGeometry(QtCore.QRect(190, 160, 113, 25))
        self.textDesc.setObjectName("textDesc")
        self.textColor = QtGui.QLineEdit(AddP)
        self.textColor.setGeometry(QtCore.QRect(190, 190, 113, 25))
        self.textColor.setObjectName("textColor")
        self.textPrecio = QtGui.QLineEdit(AddP)
        self.textPrecio.setGeometry(QtCore.QRect(190, 220, 113, 25))
        self.textPrecio.setObjectName("textPrecio")
        self.textCodigo = QtGui.QLineEdit(AddP)
        self.textCodigo.setGeometry(QtCore.QRect(190, 100, 113, 25))
        self.textCodigo.setObjectName("textCodigo")
        self.textFk2 = QtGui.QLineEdit(AddP)
        self.textFk2.setGeometry(QtCore.QRect(190, 250, 113, 25))
        self.textFk2.setObjectName("textFk2")
        self.label = QtGui.QLabel(AddP)
        self.label.setGeometry(QtCore.QRect(40, 10, 351, 51))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(AddP)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 91, 17))
        self.label_2.setObjectName("label_2")
        self.Cdg = QtGui.QLabel(AddP)
        self.Cdg.setGeometry(QtCore.QRect(130, 100, 51, 17))
        self.Cdg.setObjectName("Cdg")
        self.Nom = QtGui.QLabel(AddP)
        self.Nom.setGeometry(QtCore.QRect(120, 130, 61, 17))
        self.Nom.setObjectName("Nom")
        self.Desc = QtGui.QLabel(AddP)
        self.Desc.setGeometry(QtCore.QRect(100, 160, 81, 20))
        self.Desc.setObjectName("Desc")
        self.Color = QtGui.QLabel(AddP)
        self.Color.setGeometry(QtCore.QRect(140, 190, 41, 17))
        self.Color.setObjectName("Color")
        self.Precio = QtGui.QLabel(AddP)
        self.Precio.setGeometry(QtCore.QRect(130, 220, 41, 17))
        self.Precio.setObjectName("Precio")
        self.Fk2 = QtGui.QLabel(AddP)
        self.Fk2.setGeometry(QtCore.QRect(160, 250, 21, 17))
        self.Fk2.setObjectName("Fk2")
        self.addOk = QtGui.QPushButton(AddP)
        self.addOk.setGeometry(QtCore.QRect(100, 320, 103, 26))
        self.addOk.setObjectName("addOk")
        self.addCancel = QtGui.QPushButton(AddP)
        self.addCancel.setGeometry(QtCore.QRect(220, 320, 103, 26))
        self.addCancel.setObjectName("addCancel")

        self.retranslateUi(AddP)
        QtCore.QMetaObject.connectSlotsByName(AddP)

    def retranslateUi(self, AddP):
        AddP.setWindowTitle(QtGui.QApplication.translate("AddP", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddP", "Para agregar un nuevo producto llene los campos a", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddP", "continuacion", None, QtGui.QApplication.UnicodeUTF8))
        self.Cdg.setText(QtGui.QApplication.translate("AddP", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.Nom.setText(QtGui.QApplication.translate("AddP", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.Desc.setText(QtGui.QApplication.translate("AddP", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.Color.setText(QtGui.QApplication.translate("AddP", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.Precio.setText(QtGui.QApplication.translate("AddP", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.Fk2.setText(QtGui.QApplication.translate("AddP", "Fk", None, QtGui.QApplication.UnicodeUTF8))
        self.addOk.setText(QtGui.QApplication.translate("AddP", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.addCancel.setText(QtGui.QApplication.translate("AddP", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

