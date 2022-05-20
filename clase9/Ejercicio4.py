import tkinter as tk

alumnos = {}

def ver_lista():
	print("Lista de alumnos:")
	for nombre in alumnos:		
		print(nombre + " - " + str(alumnos[nombre]) + " cursos")
		
def agregar_alumno():
	nombre = caja_nombre.get()
	cursos = int(caja_curso.get())
	if nombre == "":
		print("Error!!!, ingreso un nombre no valido")
	else:
		alumnos[nombre] = cursos
		print("¡El alumno fue añadido a la lista!")
		
def ver_cursos():
	nombre = caja_nombre.get()
	print("Cursos del alumno:",  alumnos[nombre])

#Crear una ventana
ventana = tk.Tk()

#Configurar el titulo
ventana.title("Proyecto Integrador")

#Configurar el tamaño
ventana.config(width = 400, height = 300)

#Ver lista de alumnos
botonLista = tk.Button(text= "Ver Lista de alumnos", command = ver_lista)
botonLista.place(x = 10, y = 10)

#Nombre Alumno
etiqueta_nombre = tk.Label(text = "Nombre alumno:")
etiqueta_nombre.place(x = 10, y = 60)

caja_nombre = tk.Entry()
caja_nombre.place(x = 110, y = 60, width = 150, height = 20)

#Cursos
etiqueta_curso = tk.Label(text = "Cursos:")
etiqueta_curso.place(x = 10, y = 100)

caja_curso = tk.Entry()
caja_curso.place(x = 110, y = 100, width = 50, height = 20)

#Agregar a la lista
botonAgregar = tk.Button(text= "Agregar a la lista", command = agregar_alumno)
botonAgregar.place(x = 10, y = 150)

#Ver cantidad de cursos
botonCurso = tk.Button(text= "Ver cantidad de cursos", command = ver_cursos)
botonCurso.place(x = 120, y = 150)

#Mostrar ventana
ventana.mainloop()
