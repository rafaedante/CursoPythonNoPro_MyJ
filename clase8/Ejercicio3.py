# ~ Escribir un programa que pregunte al usuario
# ~ por dos cadenas de texto y llama a una funcion
# ~ para que le indique si esas cadenas son
# ~ iguales o no.
# ~ Devolver por pantalla el resultado de la comparacion


# ~ ----- inicio PROGRAMA PRINCIPAL----

# ~ PIDE LOS DATOS

# ~ LLAMA A LA FUNCION --> RETORNA SI SON IGUALES O NO

# ~ IMPRIME RESPUESTA

# ~ ----- fin PROGRAMA PRINCIPAL----

def comparacion(texto1, texto2):
	return texto1 == texto2
	
		
print("inicio programa")

cadena1= input("Ingrese el texto numero 1: ")
cadena2= input("Ingrese el texto numero 2: ")

resultadoComparacion = comparacion(cadena1, cadena2)

if resultadoComparacion:
	print("las cadenas son iguales")
else:
	print("las cadenas NO son iguales")

print("fin programa")


# ~ def comprobacion (a,b):
    # ~ if a == b:
        # ~ return True
    # ~ else:
        # ~ return False

# ~ p1= str(input("Inserte una palabra: "))
# ~ p2 = str(input("Inserte otra palabra: "))
# ~ i= comprobacion(p1, p2)
# ~ if i == True:
    # ~ print("Las palabras coinciden")
# ~ else:
    # ~ print("Las palabras no coinciden")
