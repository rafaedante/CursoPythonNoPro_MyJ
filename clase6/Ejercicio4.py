# ~ Ingrese el número de la operación que desea ejecutar:
# ~ 1 - Ver la lista de alumnos.
# ~ 2 - Añadir un alumno a la lista.
# ~ 3 - Salir.

alumnos = {}

# ~ Como deberia quedar la informacion en la lista

# ~ alumnos = [["Juan", 4],["Ana", 6],["Jose", 5]]

#   alumnos = {"Juan": 4, "Ana": 6, "Jose": 5}

# Pablo - 3 cursos


#opcion = 0
#while opcion =! 3:
while True:
	print("Ingrese el número de la operación que desea ejecutar:")
	print("1 - Ver la lista de alumnos.")
	print("2 - Añadir un alumno a la lista.")
	print("3 - Ver la cantidad de cursos de un alumno.")
	print("4 - Salir.")
	
	opcion = int(input("Ingrese un numero de opcion: "))
	
	if opcion == 1:
		print("Lista de alumnos:")
		for nombre in alumnos:			
			cursos = alumnos[nombre]
			print(nombre + " - " + str(cursos) + " cursos")
	elif opcion == 2:
		nombre = input("Ingrese el nombre del alumno: ")
		cursos = int(input("Ingrese la cantidad de cursos: "))
		if nombre == "":
			print("Error!!!, ingreso un nombre no valido")
		else:
			alumnos[nombre] = cursos
			print("¡El alumno fue añadido a la lista!")
	elif opcion == 3:
		nombre = input("Ingrese el nombre del alumno a consultar: ")
		print("Cursos del alumno:",  alumnos[nombre])
	elif opcion == 4:		
		break
	else:
		print("La opción ingresada no es correcta, vuelva a intentarlo")
		
print("¡Gracias por utilizar el programa!")
