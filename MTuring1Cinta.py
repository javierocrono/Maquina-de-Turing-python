class MTuring1Cinta:

    def __init__(self, transiciones, estados, alfabeto):
        self.inicial = ""  # estado inicial
        self.final = ""  # estado final
        self.estados = estados  # arreglo de estados
        self.transiciones = transiciones  # arreglo de transiciones
        self.alfabeto = alfabeto  # alfabeto

    def agregaEstIni(self, estIni):
        if(estIni != ""):
            if (estIni in self.estados):
                self.inicial = estIni
                salida = "Estado Final agregado"
            else:
                salida = "Ingrese un estado Inicial Valido"
        else:
            salida = "Ingrese algun estado Inicial"
            return salida

    def agregaEstFin(self, estFin):
        if(estFin != ""):
            if (estFin in self.estados):
                self.final = estFin
                salida = "Estado Final agregado"
            else:
                salida = "Ingrese un estado Final Valido"
        else:
            salida = "Ingrese algun estado Final"
        return salida

    def aceptaPalabra(self, palabra):
        correcto = True
        for i in range(palabra.length()):
            if (palabra[i] not in self.alfabeto):
                correcto = False
        if (correcto):
            simboloCinta = palabra[0]
            posSimbolo = self.alfabeto.find(simboloCinta)
            estadoActual = self.inicial
            posEstadoActual = self.estados.find(estadoActual)
            transicion = self.transiciones[posEstadoActual][posSimbolo]
            escribo = ""
            while (estadoActual != self.final or transicion == ""):
                pass
            if(estadoActual == self.final):
                salida = "Palabra Aceptada"
            else:
                salida = "Palabra Rechazada"
        else:
            salida = "La Palabra contiene un simbolo No reconocido por la MT"
        return salida

    def mostrar(self):
        for i in self.alfabeto:
            print i, " ",
