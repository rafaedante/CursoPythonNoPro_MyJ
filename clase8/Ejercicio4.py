# ~ import nombre_libreria

# ~ import random


# ~ while True:
	# ~ print("Menu")
	# ~ print("1 - Tirar dados")
	# ~ print("2 - Salir")
	
	# ~ opcion = int(input("Ingrese una opcion: "))
	
	# ~ if opcion == 1:
		# ~ numeroDado = random.randint(1, 6)
		# ~ print("el valor del dado es:", numeroDado)
	# ~ elif opcion == 2:
		# ~ break
	# ~ else:
		# ~ print("opcion no valida")


import time

i = 0

while i < 10:
	print(i)
	time.sleep(1)
	i = i + 1
