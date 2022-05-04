# ~ Escribir un programa que pedi al usuario 2 numeros
# ~ y le devuelva como resultado cual es el mayor
# ~ en el caso que sean iguales devolver el mensaje son iguales

# ~ a = int(input ("Ingrese el 1er valor numerico: "))
# ~ b = int(input ("Ingrese el 2do valor numerico: "))
# ~ if a>b :
	# ~ print ("El valor mas grande es el número",a)
# ~ elif a<b:
	# ~ print ("El valor mas grande es el número",b)
# ~ elif a==b:
	# ~ print ("Los valores numericos son iguales")


numero1 = int(input("Escriba un numero: "))
numero2 = int(input("Escriba otro numero: "))

print (numero1)
print (numero2)

if numero1 > numero2 :
	print ("El primer numero es el mayor")
elif numero1 < numero2:
	print ("El segundo numero es el mayor")
else:
	print ("Los numeros son iguales")
