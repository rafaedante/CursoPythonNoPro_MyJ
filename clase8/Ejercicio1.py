def imprimir_mensaje(lenguaje, editor, anio = 2022):
	print("hola mundo")
	print("Desde el lenguaje " + lenguaje)
	print("y uso el editor " + editor)
	print("en el año " + str(anio))
	
def imprimir_mensaje2():
	editor = "VSC"
	anio = 2022
	print("hola mundo")
	print("Desde el lenguaje python")
	print("y uso el editor " + editor)
	print("en el año " + str(anio))
	
def calculo_Matematico(numero1, numero2, numero3):
	n1 = numero1 ** 2
	n2 = numero2 ** 3
	n3 = numero3 ** 2
	
	n4 = n1 + n2
	n5 = n4 * n3
	
	return n5


# Programa principal

print("------inicio programa---------")

imprimir_mensaje("python", "geany", 2021)

print("--------------")

imprimir_mensaje2()

print("--------------")

valor1 = 5
valor2 = 3
valor3 = 4

resultado = calculo_Matematico(valor1, valor2, valor3)
print("resultado rta funcion:", resultado)

otro_resultado = resultado * 2
print("otro resultado:", otro_resultado)

print("------fin programa---------")
