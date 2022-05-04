
# Resumen Listas

# Creacion

# ~ lista = []


# ~ # Agregar un elemento al final
# ~ lista.append("elemento")

# ~ # Agregar un elemento en una posicion particular
# ~ indice = 2
# ~ lista.insert(indice, "elemento")

# ~ # Borrar un elemento
# ~ del lista[indice]

# ~ #Reemplazar un elemento por otro
# ~ lista[indice] = "elemento"

# ~ # Ver cantidad de elemntos de un lista
# ~ len(lista)


# Ejercicio

# ~ Escribir un programa que pida por consola el nombre de 4 alumnos, lo agregue a una lista
# ~ y por ultimo que imprima la lista

# FORMA 1

# ~ alumnos = [input("Ingrese alumno1 "),input("Ingrese alumno2 "), input ("Ingrese alumno3 "), input ("Ingrese alumno4 ")]

# ~ print(alumnos)



# FORMA 2

# ~ lista=[]
# ~ alumno1 = input("Agregar nombre del 1er alumno: ")
# ~ alumno2 = input("Agregar nombre del 2do alumno: ")
# ~ alumno3 = input("Agregar nombre del 3er alumno: ")
# ~ alumno4 = input("Agregar nombre del 4to alumno: ")

# ~ lista.append(alumno1)
# ~ lista.append(alumno2)
# ~ lista.append(alumno3)
# ~ lista.append(alumno4)

# ~ print(lista)


# FORMA 3

alumnos = []
alumnos.append(input("Insertar nombre de alumno: "))
alumnos.append(input("Insertar nombre de otro alumno: "))
alumnos.append(input("Insertar nombre de otro alumno: "))
alumnos.append(input("Insertar nombre de otro alumno: "))
print(alumnos)
