# ~ Escribir un programa que pida al usuario una palabra
# ~ y el mismo muestre por pantalla el numero de veces que contiene cada vocal.

# ~ Banana

# ~ contiene 3 a
# ~ Contine  0 i
# ~ Contiene 0 o
# ~ Contiene 0 u
# ~ Contiene 0 e

# ~ Hipopotamo

# ~ Contine  1 i
# ~ Contiene 3 o
# ~ Contiene 1 a
# ~ Contiene 0 u
# ~ Contiene 0 e


palabra = input("Ingrese una palabra: ")

vocales = ["a", "e", "i", "o", "u"]


for vocal in vocales:
	ocurrencias = 0
	for letra in palabra:
		if vocal == letra:
			ocurrencias = ocurrencias + 1
	print("La vocal:", vocal, "aparece", ocurrencias, "veces")
	print("La vocal: " + vocal + " aparece " + str(ocurrencias) + " veces")
	print("----------------------------------------------------")
			
	
