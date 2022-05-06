
# ~ escribir un programa que pida una cantidad de alumnos al usuario

# ~ A continuacion debe pedir los nombres de los alumnos segun la cantidad ingresada

# ~ y por ultimo debe imprimir a cada alumno con un saludo

# ~ por ej."bienvenido alumno N"


cantidad = int(input("ingrese cantidad de nombres de alumnos: "))
alumnos= []
i = 0

# ~ for al in range(0,cantidad):
    # ~ nombre = input("ingrese el nombre del "+ str(al+1) + "° alumno: ")
    # ~ alumnos.append (nombre)
    
# ~ for N in alumnos:
    # ~ print("Bienvenido " , N)
    
# Implementacion con while

while i < cantidad:
	alumnos.append(input("ingrese el nombre del "+ str(i+1) + "° alumno: "))
	i = i + 1
	
	
i = 0
while i < cantidad:
	print("Bienvenido " , alumnos[i])
	i = i + 1
									 
	
