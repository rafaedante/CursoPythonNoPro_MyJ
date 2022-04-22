
#SENTENCIAS CONDICIONALES

# ~ if condicion:
	# ~ bloque de codigo
	# ~ if condicion2:
		# ~ bloque de codigo 2
	# ~ else:
		# ~ bloque de codigo 2 alternativo
		# ~ if condicion3:
			# ~ bloque de codigo 3
		# ~ else:
			# ~ bloque de codigo 3 alternativo
# ~ else:
	# ~ bloque de codigo
	
	
	
print("------inicio del programa-----")
	
a = 10 + 5

# ~ if a == 12:
	# ~ print("la variable a es igual a 12")
	# ~ print("esta es otra linea en la sent condicional")
	# ~ b = 5
	# ~ c = b + a
	# ~ print("el valor de c es:",c)
# ~ else:
    # ~ print("la variable a es distinto a 12")
	# ~ print("esta es otra linea en la sent condicional x el distinto")
	# ~ b = 5
	# ~ c = b - a
	# ~ print("el valor de c es:",c)
	

# ~ if a != 12:
	# ~ print("la variable a es distinto a 12")
	# ~ print("esta es otra linea en la sent condicional x el distinto")
	# ~ b = 5
	# ~ c = b - a
	# ~ print("el valor de c es:",c)
	
	
if a == 12:
	print("la variable a es igual a 12")
else:
	if a == 13:
		print("la variable a es igual a 13")
	else:
		if a == 14:
			print("la variable a es igual a 14")
		else:
			print("la variable a no es igual ni a 12, ni a 13 ni a 14")


		
print("-----fin del programa-----")

