# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Taller.ui'
#
# Created: Sun Jun  8 15:14:34 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 582)
        self.NewP = QtGui.QPushButton(Dialog)
        self.NewP.setGeometry(QtCore.QRect(372, 30, 141, 26))
        self.NewP.setObjectName("NewP")
        self.Edit = QtGui.QPushButton(Dialog)
        self.Edit.setGeometry(QtCore.QRect(530, 30, 103, 26))
        self.Edit.setObjectName("Edit")
        self.Del = QtGui.QPushButton(Dialog)
        self.Del.setGeometry(QtCore.QRect(660, 30, 103, 26))
        self.Del.setObjectName("Del")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 311, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(340, 70, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(540, 80, 191, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(390, 80, 151, 20))
        self.label.setObjectName("label")
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setEnabled(True)
        self.tableView.setGeometry(QtCore.QRect(30, 120, 711, 431))
        self.tableView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.NewP.setText(QtGui.QApplication.translate("Dialog", "Nuevo producto", None, QtGui.QApplication.UnicodeUTF8))
        self.Edit.setText(QtGui.QApplication.translate("Dialog", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.Del.setText(QtGui.QApplication.translate("Dialog", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Dialog", " Que producto esta buscando?", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Marcas", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Nike", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "HP", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Dialog", "Dell", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Dialog", "Puma", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Dialog", "Samsung", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Seleccione una marca", None, QtGui.QApplication.UnicodeUTF8))

