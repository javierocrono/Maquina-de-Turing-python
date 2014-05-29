x = input("ingrese primer numero: ")
y = input("Ingrese el segundo numero: ")
r = x / y
s = x % y
print "el resultado de la division es: ", r
#print s Prueba de salida "resto"
if(s == 0):
    print "La division es exacta"
else:
    print "La division no es exacta"
