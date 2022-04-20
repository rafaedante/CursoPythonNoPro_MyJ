# ~ 1. Elevar b al cuadrado.
# ~ 2. Multiplicar 4 por a y por c.
# ~ 3. Restar el resultado de (2) al resultado de (1).
# ~ 4. Calcular la raíz cuadrada del resultado de (3).
# ~ 5. Sumar el resultado de (4) a - b.
# ~ 6. Restar el resultado de (4) a - b.
# ~ 7. Dividir el resultado de (5) por 2a.
# ~ 8. Dividir el resultado de (6) por 2a.

# potencia = a ** 3
# raiz cuadrada = a ** (1/2)
# concatenacion = print(cadena1, cadena2,....,cadenan)


a = 1
b = 1
c = -6


paso1 = b ** 2
#print(paso1)

paso2= 4 * a * c
#print(paso2)

paso3 = paso1 - paso2
#print(paso3)

paso4 = paso3 ** (1/2)
#print(paso4)

paso5= -b + paso4
#print(paso5)

paso6= -b - paso4
#print(paso6)

paso7 = paso5 / (2 * a)
#print("Primer resultado", paso7)

paso8 = paso6 / (2 * a)
#print("Segundo resultado", paso8)


print("Los resultados son", paso7, "y", paso8)
