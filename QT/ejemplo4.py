#!/usr/bin/python
# -*- coding: utf-8 -*-
#Nombre archivo: Ejemplo_4.py ****layouts****

import sys
from PySide import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")
        hbox = QtGui.QHBoxLayout()  # Iniciamos un layout horizontal
        hbox.addStretch(1)
        #Agregamos elementos al layout
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox = QtGui.QVBoxLayout()  # Creamos un layout vertical
        vbox.addStretch(1)
        #Al layout vertical le agregamos el layout horizontal
        vbox.addLayout(hbox)
        #Le asignamos a la pantalla principal el layout vertical
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#se ejecuta solo si se invoca directamente este archivo
if __name__ == '__main__' :
    main()