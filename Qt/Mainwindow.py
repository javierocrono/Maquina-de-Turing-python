# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Thu Jun 19 04:28:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 550)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 461, 341))
        self.widget.setObjectName("widget")
        self.line_inicial = QtGui.QLineEdit(self.widget)
        self.line_inicial.setGeometry(QtCore.QRect(190, 250, 113, 27))
        self.line_inicial.setObjectName("line_inicial")
        self.line_final = QtGui.QLineEdit(self.widget)
        self.line_final.setGeometry(QtCore.QRect(190, 300, 113, 27))
        self.line_final.setObjectName("line_final")
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 250, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 300, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 111, 17))
        self.label_3.setObjectName("label_3")
        self.text_transiciones = QtGui.QTextEdit(self.widget)
        self.text_transiciones.setGeometry(QtCore.QRect(30, 40, 411, 181))
        self.text_transiciones.setObjectName("text_transiciones")
        self.btn_ingresar = QtGui.QPushButton(self.widget)
        self.btn_ingresar.setGeometry(QtCore.QRect(340, 270, 98, 27))
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(500, 30, 291, 311))
        self.widget_2.setObjectName("widget_2")
        self.tableView = QtGui.QTableView(self.widget_2)
        self.tableView.setGeometry(QtCore.QRect(15, 40, 261, 251))
        self.tableView.setObjectName("tableView")
        self.label_6 = QtGui.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 111, 17))
        self.label_6.setObjectName("label_6")
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(30, 390, 711, 121))
        self.widget_3.setObjectName("widget_3")
        self.line_palabra = QtGui.QLineEdit(self.widget_3)
        self.line_palabra.setGeometry(QtCore.QRect(90, 40, 571, 27))
        self.line_palabra.setObjectName("line_palabra")
        self.label_4 = QtGui.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.label_4.setObjectName("label_4")
        self.btn_verificar = QtGui.QPushButton(self.widget_3)
        self.btn_verificar.setGeometry(QtCore.QRect(300, 80, 98, 27))
        self.btn_verificar.setObjectName("btn_verificar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulador M.Turing 1Cinta", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Estado Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Estado Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Transiciones:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ingresar.setText(QtGui.QApplication.translate("MainWindow", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "MT Resultante:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Palabra de entrada", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_verificar.setText(QtGui.QApplication.translate("MainWindow", "Verificar", None, QtGui.QApplication.UnicodeUTF8))

