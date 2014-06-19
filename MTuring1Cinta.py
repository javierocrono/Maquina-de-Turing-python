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

    def aceptaPalabra(self, pala):
        palabra = list(pala)
        print palabra
        correcto = True
        for i in palabra:
            if (i not in self.alfabeto):
                correcto = False
        if (correcto):
            self.inicial = 'q0'
            self.final = 'q4'
            print correcto
            i = 0
            simboloCinta = palabra[i]
            estadoActual = self.inicial
            posSimbolo = self.alfabeto.index(simboloCinta)
            posEstadoActual = self.estados.index(estadoActual)
            transicion = self.transiciones[posEstadoActual][posSimbolo]
            while (estadoActual != self.final and transicion != "**************"):
                print simboloCinta
                print "transicion"
                print transicion
                estadoSiguiente = transicion[0]
                escribo = transicion[1]
                direccionAvance = transicion[2]
                palabra[i] = escribo
                print palabra
                estadoActual = estadoSiguiente
                print estadoActual
                if (direccionAvance == 'D'):
                    i = i + 1
                else:
                    i = i - 1
                if (i < len(palabra)):
                    simboloCinta = palabra[i]
                posSimbolo = self.alfabeto.index(simboloCinta)
                posEstadoActual = self.estados.index(estadoActual)
                transicion = self.transiciones[posEstadoActual][posSimbolo]
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
