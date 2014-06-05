#!/usr/bin/python
# -*- coding: utf-8 -*-
#Nombre archivo: Ejemplo_2.py

import sys
from PySide import QtGui
#Clase que hereda las propiedades de QWidget

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()  # invocamos al constructor de QWidget
        self.init_ui()  #Método que construye los componentes gráficos

    def init_ui(self):
    #Método de la clase que construye los componentes gráficos de la pantalla
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QtGui.QPushButton('Button', self)
        btn.move(50, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()
        btn.clicked.connect(self.action)

    def action(self):
        print "Ha presionado el botón"

#Notar que esta función no es parte de la clase Example (fijarse en la
# identación)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#se ejecuta solo si se invoca directamente este archivo
if __name__ == '__main__' :
    main()