#!/usr/bin/python
# -*- coding: utf-8 -*-

#Estructura Estado_Actual;Simbolo_Actual_Del_Cabezal;Estado_Siguiente;
#Simbolo_a_Escribir;Direccion_De_Avance
#D: movimiento derecha - I: Movimiento izquierda


def llenarTransiciones(transiciones, fil, col, ent):
    mTrans = transiciones
    nFil = fil
    nCol = col
    pos1 = 0
    pos2 = 0
    aux = separaTupla(ent)
    for i in aux:
        aux2 = separaElem(i)
        cont1 = 0
        cont2 = 0
        for a in nFil:  # Obteniendo posiciones de cada transicion
            if aux2[0] == a:
                pos1 = cont1
            cont1 = cont1 + 1
        for b in nCol:
            if aux2[1] == b:
                pos2 = cont2
            cont2 = cont2 + 1
        mTrans[pos1][pos2] = aux2[2], aux2[3], aux2[4]  # Agregando a la matriz
    for w in mTrans:
        print w


def dimTransiciones(entrada0):
    n = 5
    m = 0
    dim = ""
    aux = separaTupla(entrada0)
    for i in aux:
        aux2 = separaElem(i)
        if dim < aux2[2]:
            dim = aux2[2]
        m = int(dim[1])
    transiciones = [["**************" for x in xrange(n)] for x in xrange(m+1) ]
    estados = [0 for x in xrange(m+1) ]
    alfabeto = [0 for x in xrange(n)]
    c1 = 0
    c2 = 0
    for j in aux:
        aux2 = separaElem(j)
        if aux2[2] not in estados:  # llenando estados sin repeticiones
            estados[c1] = aux2[2]
            c1 = c1 + 1
        if aux2[1] not in alfabeto:  # Llenando alfabeto sin repeticiones
            alfabeto[c2] = aux2[1]
            c2 = c2 + 1
    estados.sort()  # ordenando estados
    return (transiciones, estados, alfabeto)


def separaTupla(entrada1):
    separaTupla = entrada1.split(';')
    return (separaTupla)


def separaElem(entrada2):
    separaElem = entrada2.split(',')
    return (separaElem)

#Turing1 = Turing()
x = "q0,0,q1,x,D;q1,0,q1,0,D;q2,0,q2,0,I;q1,1,q2,y,I;q2,x,q0,x,D;q0,y,q3,y,D;q1,y,q1,y,D;q2,y,q2,y,I;q3,y,q3,y,D;q3,b,q4,b,D"
(dim, filas, columnas) = dimTransiciones(x)
llenarTransiciones(dim, filas, columnas, x)


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

