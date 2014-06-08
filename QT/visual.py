#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from PySide.QtGui import *
import Taller
import bd


class Principal(QtGui.QWidget, Taller.Ui_Dialog):

    def __init__(self,parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.filtro = "all"
        self.main_layout = QtGui.QVBoxLayout(self)
        self.render_table()
        self.load()
        self.show()


    def render_table(self):
        self.table = self.tableView
        self.table.setFixedWidth(750)
        self.table.setFixedHeight(300)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.main_layout.addWidget(self.table)

    def filtrar(self, index):
        self.comboBox.activated[int].connect()
        fk = self.ui.comboBox.itemData("fk_id_marca")
        self.filtro = fk
        self.load()
#

    def load(self):
        productos = bd.obtener(self.filtro)
        self.model = QtGui.QStandardItemModel(len(productos), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descrp"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Fk"))
        r = 0
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['Codigo'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['Nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['Descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['Color'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['Precio'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['Fk_id_marca'])
            r = r + 1
        self.table.setModel(self.model)




def run():
    app= QtGui.QApplication(sys.argv)
    form=Principal()
    form.show()
    app.exec_()

if __name__ == '__main__':
    run()