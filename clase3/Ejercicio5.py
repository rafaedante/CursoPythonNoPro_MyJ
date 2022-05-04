# listas

# int, bool, float, str
# list, tupla, dict


alumno1 = "Juan"
alumno2 = "Matias"
alumno3 = "Jose"

# ~ print(alumno1)
# ~ print(alumno2)
# ~ print(alumno3)


# Crear una lista

alumnos = ["Juan", "Matias", "Jose", "Martina"]

# indice = posicion
x = 2
print(alumnos[1 + x])
print("hola", alumnos[x])


# programa sin lista

alumno1 = "Juan"
alumno2 = "Matias"
alumno3 = "Jose"
alumno4 = "Martina"

indice = int(input("Ingrese un indice de alumno: "))


if indice == 1:
	print("Hola", alumno1)
elif indice == 2:
	print("Hola", alumno2)
elif indice == 3:
	print("Hola", alumno3)
elif indice == 4:
	print("Hola", alumno4)
	
	
# programa con lista

alumnos = ["Juan", "Matias", "Jose", "Martina"]
indice = int(input("Ingrese un indice de alumno: "))
print("Hola", alumnos[indice])
