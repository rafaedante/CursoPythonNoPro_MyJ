#tkinter: libreia para crear aplicaciones de escritorio

import tkinter as tk


#Crear una ventana
ventana = tk.Tk()

#Configurar el titulo
ventana.title("Mi primer aplicacion")

#Configurar el tamaño
ventana.config(width = 500, height = 400)

#Crear boton
boton = tk.Button(text= "Hola mundo")
#Les damos una posicion y tamaño al boton
boton.place(x = 30, y = 50, width = 100, height = 40)

boton1 = tk.Button(text= "Hacer click")
boton1.place(x = 30, y = 100, width = 100, height = 40)


#Cuadro de texto
caja = tk.Entry()
caja.place(x = 30, y = 220, width = 150, height = 40)

#Etiquetas
etiqueta = tk.Label(text = "Ingrese su nombre")
etiqueta.place(x = 30, y = 195, width = 200, height = 25)

#Mostrar ventana
ventana.mainloop()

print("Hola mundo")

