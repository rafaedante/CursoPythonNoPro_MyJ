# ~ Exception en Python

# ~ try:
	# ~ bloque de codigo exitoso
# ~ except Nombre_de_la_excepcion:
	# ~ bloque de codigo alternativo

import tkinter as tk

def suma():
	try:
		numero1= caja_Nro1.get()
		numero2= caja_Nro2.get()
		resultado = float(numero1) + float(numero2)
		print("La suma es", resultado)
	except ValueError:
		print("Debe ingresar solamente datos numericos!!!!!")
	except IndexError:
		print("Esta accediendo a una posicion inexistente")
		
def producto():
	try:
		numero1= caja_Nro1.get()
		numero2= caja_Nro2.get()
		resultado = float(numero1) * float(numero2)
		print("La multiplicacion es", resultado)
	except ValueError:
		print("Debe ingresar solamente datos numericos!!!!!")
	except IndexError:
		print("Esta accediendo a una posicion inexistente")


#Crear una ventana
ventana = tk.Tk()

#Configurar el titulo
ventana.title("Calculadora Python")

#Configurar el tamaño
ventana.config(width = 320, height = 200)

#Nro1
etiqueta_Nro1 = tk.Label(text = "Ingrese Numero 1")
etiqueta_Nro1.place(x = 20, y = 20, width = 100, height = 40)

caja_Nro1 = tk.Entry()
caja_Nro1.place(x = 20, y = 50, width = 100, height = 40)


#Nro2
etiqueta_Nro2 = tk.Label(text = "Ingrese Numero 2")
etiqueta_Nro2.place(x = 130, y = 20, width = 100, height = 40)

caja_Nro2 = tk.Entry()
caja_Nro2.place(x = 130, y = 50, width = 100, height = 40)


# Botones Operaciones

botonSumar = tk.Button(text= "SUMAR", command = suma)
botonSumar.place(x = 20, y = 100, width = 100, height = 40)

botonMultiplicar = tk.Button(text= "MULTIPLICAR", command = producto)
botonMultiplicar.place(x = 130, y = 100, width = 100, height = 40)


#Mostrar ventana
ventana.mainloop()
