# Condiciones multiples

# operador AND (conjuncion)
# operador OR  (disyuncion)


a = 7 + 5

if a >= 1 and a <=10 and a != 15:
	print("a esta entre 1 y10")
else:
	print("a no esta entre 1 y 10")
	
print("-------------------------")
edad = 30

if edad >= 16 and edad < 70:
	print("votacion obligatoria")
elif edad >= 70:
	print("votacion opcional.")
else:
	print("No puede votar")


# disyuncion
print("-------------------------")
if a > 10 or a < 0:
	print("a es mayor que diez o negativo")
else:
	print("a esta entre 1 y10")
	
	
# operador NOT

print("-------------------------")

nota = 3
aprobado = nota >= 4

# not True == False
# not False == True


if not aprobado:
	print("Estas desaprobado")
if aprobado == False:
	print("Estas desaprobado")
	
	
