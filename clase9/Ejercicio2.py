# ~ Escribir un programa que pida al usuario 2 valores numericos.
# ~ Validar que el primer valor sea menor al segundo valor.
# ~ Si la validacion crear una funcion que imprima los numeros
# ~ en ese rango de valores que envian por parametros.(que incluya los limites)


# ~ Programa Principal
# ~ 1- pido datos
# ~ 2- valido
# ~ 3. llamo funcion


def imprimirN(a,b):
    for i in range(a,b+1):
        print(i)



print("-----Inicio---------")

valor1 = int(input("ingresar un valor numerico: "))
valor2 = int(input("ingresar un segundo valor: "))

if valor1<valor2:
    imprimirN(valor1,valor2)


print("-----Fin---------")
