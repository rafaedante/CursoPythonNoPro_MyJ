# Funciones

# ~ print()
# ~ input()
# ~ int()
# ~ lista.append()

# ~ Definiciones de una funcion:

# ~ def nombre_funcion():
	# ~ bloque de codigo

# ~ def nombre_funcion(parametro1, parametro2...):
	# ~ bloque de codigo
	
def imprimir_mensaje(lenguaje, editor, anio = 2022):
	print("hola mundo")
	print("Desde el lenguaje " + lenguaje)
	print("y uso el editor " + editor)
	print("en el año " + str(anio))
	
	
# Programa principal

print("------inicio programa---------")

imprimir_mensaje("python", "geany", 2021)

a = 15
b = 10
c = a + b
print(c)

imprimir_mensaje("java","eclipse")

print("------fin programa---------")
