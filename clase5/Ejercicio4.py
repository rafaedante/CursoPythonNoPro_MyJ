#Matrices: es un tipo de lista

# ~ matriz = [[10, 20, 30],[40]]
# ~ print(type(matriz))
# ~ print(matriz)

# ~ matriz [0][1] = 10

# ------------ Ejercicio --------------

# ~ Dada la matriz de mas abajo escribir un programa que le pida al usuario
# ~ un numero de fila y un numero de columna

# ~ y mostrar el valor del elemento en esa posicion

# ~ Controlar que se trate de una fila valida y de una columna valida.

# ~ Si son valores no validos indicar un mensaje que los valores ingrsados
# ~ son incorrectos.

# ~ matriz = [[10, 20, 30, 5],[40, 33, 66, 88]]

matriz=[[10,20,30,5],[40,33,66,88]]

nlista=int(input("Ingresar el numero de la lista solicitada: "))
posicion=int(input("Ingresar el numero de la posicion : "))

#if nlista<= len(matriz[0]) and posicion<= len(matriz[1]):
if (nlista == 0 or nlista == 1) and (posicion >= 0 and posicion <= 3):
	print(matriz[nlista][posicion])
else:
	print("opcion elegida fuera de rango")
