a = 1
while a < 10:
	print(a)
	a = a + 1
	
	
print("---------------------------------")

# ~ for i in [1,2,3,4,5,6,7,8,9,10,11,12.....101]:
	# ~ print(i)
	
# ~ for con range()
# range(valor_inicio, valor_final, cantidad_pasos)

# ~ for variable_iteracion in range(valor_inicio, valor_final, cantidad_pasos):
	# ~ bloque codigo
	
for i in range(100,70,-3):
	print(i)


# Ejemplo for con input

cantidad = int(input("Ingrese cantidad de nombres de alumnos: "))

for al in range(0, cantidad):
	nombre = input("Ingrese el nombre " + str(al) + ": ")
	print("Bienvenido", nombre)
