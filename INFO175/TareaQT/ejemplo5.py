#!/usr/bin/python
# -*- coding: utf-8 -*-
#Nombre archivo: Ejemplo_5.py    ****QLineEdit****

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QtGui.QLabel(self)
        qle = QtGui.QLineEdit(self)
        qle.move(60, 100)
        self.lbl.move(60, 40)
        #Se conecta la señal textChanged al método onChanged de la clase
        #La señal envía un string al método con que se conecta
        qle.textChanged[str].connect(self.onChanged)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QtGui.QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#se ejecuta solo si se invoca directamente este archivo
if __name__ == '__main__' :
    main()

