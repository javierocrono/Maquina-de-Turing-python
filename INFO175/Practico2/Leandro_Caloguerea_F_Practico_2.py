# Practico 2 por Leandro Caloguerea Farias

class Auto:

#    Bencina: Atributo float que representa los litros iniciales del auto
#    kms: Atributo que indica el estado inicial del kilometraje del auto
#    rendimiento: Atributo que indica cuantos kilometros rinde por litro
#        dicho auto
#    estado: Variable booleana que indica False si el auto esta apagado
#        o True si este esta encendido

    def __init__(self, bencina, kms, rendimiento):
        self.bencina = float(bencina)
        self.estado = False
        self.kms = kms
        self.rendimiento = float(rendimiento)
        print "tenemos" , bencina , "litros"

    def encender(self):
        if self.bencina > 0:
            self.estado = True
            print "Enciende"
        else:
            print "No Enciende"

#    Se utilizo el cast float para evitar obtener valores errados en la
#    Operacion de restar al combustible inicial el producto de kilometros por
#    Rendimiento traducido a litros consumidos en la funcion mover

    def mover (self, cant):
        self.cant = float(cant)
        if (self.bencina > 0) & (self.bencina*self.rendimiento >= self.cant):
            self.bencina -= (float(cant)/(float(self.bencina*self.rendimiento)))
            self.kms += cant
            print "Quedan",self.bencina," litros"
        else:
            print "No se mueve..."

    def apagar(self):
        if (self.estado == False):
            print "El vehiculo ya estaba sin contacto"
        elif(self.estado == True):
            self.estado = False
            print "El vehiculo se ha apagado"

    def obtKms(self): #funcion que obtiene el kilometraje actual del auto
        print (self.kms), " Kilometros recorridos"

    def crgrCmbstble(self,cantcomb):
        self.cantcomb = float(cantcomb) # Cantcomb : Cantidad de combustible
        if self.estado == True:         # a cargar
            print "Apague el motor antes de cargar combustible"
        else:
            self.bencina += cantcomb
            print "Se han cargado ", cantcomb, "litros a su vehiculo"
            print "La cantidad actual de combustible es: ", self.bencina




mi_auto = Auto(5,7,15)
mi_auto.encender()
mi_auto.mover(10)
mi_auto.obtKms()
mi_auto.apagar()
mi_auto.crgrCmbstble(12)

