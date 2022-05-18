# ~ Escribir un programa que guarde en un diccionario los precios de las frutas
# ~ segun la tabla de abajo.
# ~ El programa debe preguntar a un usuario por una fruta y un numero de kilos.
# ~ El programa debe mostrar por pantalla el precio de ese numero de kilos de fruta.
# ~ Si la fruta no esta en el diccionario debe mostrar un mensaje que no hay stock de esa fruta.

# ~ Fruta		precio
# ~ Banana		100
# ~ Manzana		130
# ~ Pera		120
# ~ Naranja		110
# ~ Mandarina	90

# fruta in diccionario {"Banana":100, "Manzana":130......}

frutas =  {"Banana":100, "Manzana":130, "Pera": 120, "Naranja": 110, "Mandarina": 90}


nombre_fruta = input("Ingrese la fruta a comprar: ")
cantidad_kilos = float(input("Ingrese la cantidad de kilos a comprar: "))

if nombre_fruta in frutas:
	print(cantidad_kilos, "kilos de", nombre_fruta, "cuesta", cantidad_kilos * frutas[nombre_fruta] )
else:
	print("No hay stock de esa fruta")


