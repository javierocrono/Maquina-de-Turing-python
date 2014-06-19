#!/usr/bin/python
# -*- coding: utf-8 -*-

#Estructura Estado_Actual;Simbolo_Actual_Del_Cabezal;Estado_Siguiente;
#Simbolo_a_Escribir;Direccion_De_Avance
#D: movimiento derecha - I: Movimiento izquierda


def llenarTransiciones(estados, alfabeto, ent):
    n = len(estados)
    m = len(alfabeto)  # incluye el blanco
    transVacia = [["**************" for x in xrange(n)] for x in xrange(m)]
    transiciones = transVacia
    posFil = 0
    posCol = 0
    aux = separaTupla(ent)
    for i in aux:
        aux2 = separaElem(i)
        cont1 = 0
        cont2 = 0
        for a in estados:  # Obteniendo posiciones de cada transicion
            if aux2[0] == a:
                posFil = cont1
            cont1 = cont1 + 1
        for b in alfabeto:
            if aux2[1] == b:
                posCol = cont2
            cont2 = cont2 + 1
        transiciones[posFil][posCol] = aux2[2], aux2[3], aux2[4]  # Agrego a la matriz
    print "Matriz de Transiciones:"
    for w in transiciones:
        print w
    return transiciones


def obtEstadosAlfabeto(entrada0):
    tuplas = separaTupla(entrada0)
    stringEstados = ""
    stringAlfabeto = ""
    for i in tuplas:
        tupla = separaElem(i)
        estadoActual = tupla[0]
        if (stringEstados.find(estadoActual) == -1):
            stringEstados += estadoActual
            if (i != tuplas[len(tuplas) - 1]):
                stringEstados += ','
        estadoSiguiente = tupla[2]
        if (stringEstados.find(estadoSiguiente) == -1):
            stringEstados += estadoSiguiente
            if (i != tuplas[len(tuplas) - 1]):
                stringEstados += ','
        simboloActual = tupla[1]
        if (stringAlfabeto.find(simboloActual) == -1):
            stringAlfabeto += simboloActual
            if (i != tuplas[len(tuplas) - 1]):
                stringAlfabeto += ','
    estados = stringEstados.split(',')
    alfabeto = stringAlfabeto.split(',')
    print "Vector Estados:"
    print estados
    print "Vector Alfabeto:"
    print alfabeto
    print "\n"
    return (estados, alfabeto)


def separaTupla(entrada1):
    separaTupla = entrada1.split(';')
    return (separaTupla)


def separaElem(entrada2):
    separaElem = entrada2.split(',')
    return (separaElem)


x = "q0,0,q1,x,D;q1,0,q1,0,D;q2,0,q2,0,I;q1,1,q2,y,I;q2,x,q0,x,D;q0,y,q3,y,D;q1,y,q1,y,D;q2,y,q2,y,I;q3,y,q3,y,D;q3,b,q4,b,D"
(estados, alfabeto) = obtEstadosAlfabeto(x)
transiciones = llenarTransiciones(estados, alfabeto, x)


#Javier: si haras algo con este archivo respaldalo xD
#Basicamente lo que hace es q segun esa gigantesca cadena determinar las tuplas
#y a que corresponde cada dato
#Una forma facil de comprobar que la transiciones de Transiciones funciona,
#basta con cambiar cualquier estado inicial de una tupla
#(ya que ese indica la fila a la que corresponde y al ejecutarlo te
#mostrara la 3tupla en la fila que indicaste
#Ejemplo que en la 4ta 5tupla cambie el q1 inicial por q4 y lo ejecute :B
#Aviso: si cambias estado y lo que lee tienes que verificar que estas
#destinando a un espacio disponible de la transiciones ya que si no
#la transicion se movera reemplazando la existente...3tupla
#Me voy al sobre xD
#PD: no es mucho el codigo pero PUTA que fue webeo hacerlo funcionar sin
# que crasheara xD
#cosa de cachar la hora a la que vine a terminar jajaa xD

