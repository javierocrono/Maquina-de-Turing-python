from auto import *

class Camion(Auto):

    def __init__(self, bencina, kms, rendimiento, peso, ruedas, acoplado):
        self.peso = float(peso)
        self.acoplado = ruedas
        self.acoplado = acoplado
        self.bencina = float(bencina)
        self.estado = False
        self.kms = kms
        self.rendimiento = float(rendimiento)
        print "tenemos" , bencina , "litros"

    def agregar_a(self,n):
        self.acoplado += n
        print "se han agregado ", n, " acomplados"

    def quitar_a(self,n):
        self.acoplado -= n


    def obtener_a(self):
        print self.acoplado, " acoplados actuales"


mi_camion = Camion(1,2,3,4,5,6)
mi_camion.agregar_a(2)
mi_camion.obtener_a()
mi_camion.encender()
mi_camion.crgrCmbstble(12)
mi_camion.mover(5)