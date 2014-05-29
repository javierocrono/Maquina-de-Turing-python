x = input("ingrese primer numero: ")
y = input("Ingrese el segundo numero: ")
z = input("Ingrese el tercer numero: ")
if x == y & y == z:
    print "Los 3 numeros son iguales"
elif x != y & y != z:
    print "Los 3 numeros son distintos"
elif x == y:
    print "Solo", x, "y ", y, "son iguales"