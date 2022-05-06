# ~ break

# ~ continue


# ~ i = 1
# ~ while i <= 10:
	# ~ print(i)
	# ~ i = i + 1
	# ~ if i == 5:
		# ~ break
		
		
# ~ for i in range(1,11):
	# ~ print(i)	
	# ~ if i == 5:
		# ~ break
	
i = 0	
alumnos = ["Juan", "Sofia", "Matias", "Jose", "Ana"]

# ~ for al in alumnos:
	# ~ if al == "Matias":
		# ~ continue
	# ~ print(al)	
	

# ~ while i < len(alumnos):	
	# ~ if alumnos[i] == "Matias":
		# ~ i=i+1
		# ~ continue
	# ~ print(alumnos[i])
	# ~ i = i + 1
	
	
while i < len(alumnos):
	nombre = alumnos[i]
	i=i+1

	if nombre == "Matias":
		continue
	print(nombre)


