# ~ Ingrese el número de la operación que desea ejecutar:
# ~ 1 - Ver la lista de alumnos.
# ~ 2 - Añadir un alumno a la lista.
# ~ 3 - Salir.

alumnos = []

# ~ Como deberia quedar la informacion en la lista

# ~ alumnos = [["Juan", 4],["Ana", 6],["Jose", 5]]

# Pablo - 3 cursos


#opcion = 0
#while opcion =! 3:
while True:
	print("Ingrese el número de la operación que desea ejecutar:")
	print("1 - Ver la lista de alumnos.")
	print("2 - Añadir un alumno a la lista.")
	print("3 - Salir.")
	
	opcion = int(input("Ingrese un numero de opcion: "))
	
	if opcion == 1:
		if len(alumnos) > 0:
			print("Lista de alumnos:")
			for al in alumnos:
				nombre = al[0]
				cursos = al[1]
				print(nombre + " - " + str(cursos) + " cursos")
				#print(al[0] + " - " + str(al[1]) + " cursos")
		else:
			print("No hay alumnos cargados")
	elif opcion == 2:
		nombre = input("Ingrese el nombre del alumno: ")
		cursos = int(input("Ingrese la cantidad de cursos: "))
		if nombre == "":
			print("Error!!!, ingreso un nombre no valido")
		else:
			alumnos.append([nombre, cursos])
			print("¡El alumno fue añadido a la lista!")
	elif opcion == 3:		
		break
	else:
		print("La opción ingresada no es correcta, vuelva a intentarlo")
		
print("¡Gracias por utilizar el programa!")
