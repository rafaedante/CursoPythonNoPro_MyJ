# Diccionarios

# Como se define un diccionario

# dicionario = {clave1:valor1, clave2:valor2,........}

mi_diccionario = {'nombre': 'jose', 'edad': 30, 'cursos': ['Python', 'Java', 'C']}

print(mi_diccionario)
print(type(mi_diccionario))
print("----------------------")
print(mi_diccionario['nombre'])
print(mi_diccionario['edad'])
print(mi_diccionario['cursos'])
print("----------------------")

#cambiar valora una key existente
mi_diccionario['edad'] = 40

for key in mi_diccionario:
	print(key, ":", mi_diccionario[key])
	
print("----------------------")

materias = {}
materias["lunes"] = ["Java", "Php"]
materias["martes"] = ["C#", "JS"]
materias["miercoles"] = ["Java", "Node"]
materias["jueves"] = []
materias["viernes"] = ["JS", "Php"]

#materia["Java"] = ["Lunes", "Jueves"]

for i in materias:
	print(i, ":", materias[i])
	
print("----------------------")

diccionario2 = {0 : "cero", 1 : "uno", 2: "dos", 3: "tres"}  # esta definicion NO es una buena practica
print(type(diccionario2))

print("elemento key 1:", diccionario2[1])
