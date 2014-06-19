import MTuring1Cinta
from CreaMT import *

x = "q0,0,q1,x,D;q1,0,q1,0,D;q2,0,q2,0,I;q1,1,q2,y,I;q2,x,q0,x,D;q0,y,q3,y,D;q1,y,q1,y,D;q2,y,q2,y,I;q3,y,q3,y,D;q3,b,q4,b,D"
(estados, alfabeto) = obtEstadosAlfabeto(x)
transiciones = llenarTransiciones(estados, alfabeto, x)
mt = MTuring1Cinta.MTuring1Cinta(transiciones, estados, alfabeto)
mt.mostrar()
