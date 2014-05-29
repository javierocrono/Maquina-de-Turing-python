#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
# Nombre archivo: ejemplo_2.py
import sys
from PySide import QtGui
#Clase que hereda la propiedades de QWidget
class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__() #Invocamos al constructor de QWidget
        self.init_ui() # Método que construye los componentes gráficos
    #Método de la clase que construye los componentes gráficos de la pantalla
    def init_ui(self):
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()
        btn.clicked.connect(self.action)
    def action(self):
        print u"Ha presionado el botón"


#Se ejecuta sólo si se invoca directamente este archivo.
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())