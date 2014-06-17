def agregaEstIni(estIni):
    if(estIni != ""):
        if (estIni in estados):
            self.inicial = estIni
        else:
            salida = "Ingrese un estado Inicial Valido"
    else:
        salida = "Ingrese algun estado Inicial"
        return salida


def agregaEstFin(estFin):
    if(estIni != ""):
        if (estIni in estados):
            self.inicial = estIni
            salida = "Estado Final agregado"
        else:
            salida = "Ingrese un estado Final Valido"
    else:
        salida = "Ingrese algun estado Final"
    return salida


def aceptaPalabra(palabra):
    correcto = True
    for (int i =0, i<palabra.length(), i++):
        if (palabra[i] not in self.alfabeto):
            correcto = False
    if (correcto):
        simboloCinta = palabra[0]
        posSimbolo = self.alfabeto.find(simbolocinta)
        estadoActual = self.inicial
        posEstadoActual = self.estados.find(estadoactual)
        transicion = self.transiciones[posEstadoActual][posSimbolo]
        escribo=""
        while (estadoActual != self.final or transicion == ""):
            pass
        if(estadoActual == self.final):
            salida = "Palabra Aceptada"
        else:
            salida = "Palabra Rechazada"
    else:
        salida = "La Palabra contiene un simbolo No reconocido por la MT"
    return salida