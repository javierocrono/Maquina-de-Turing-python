#!/usr/bin/python
# -*- coding: utf-8 -*-
#Nombre archivo: Ejemplo_6.py      ****Listas****

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.iniUI()

    def iniUI(self):
        self.lbl = QtGui.QLabel("Seleccionado", self)
        self.combo = QtGui.QComboBox(self)
        brands =