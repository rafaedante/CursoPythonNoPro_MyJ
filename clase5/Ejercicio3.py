# ~ escribir un programa que almacene una de cadena de caracteres que represente
# ~ una contraseña en una variable.
# ~ buscar un mecanismo que pregunte al usuario por la contraseña
# ~ hasta que introduzca la contraseña correcta
# ~ si el usuario se equivoca de contraseña indicarselo


contraseña = "educacionit"

contra=input("Ingre la contraseña: ")

while contra != contraseña:
	contra = input ("Contraseña incorrecta, intentarlo nuevamente: ")
	
print("Contraseña correcta")


contraseña = input("Escriba una contraseña: ")

validacion= input ("Escriba nuevamente la contraseña: ")
if validacion != contraseña:
    while validacion != contraseña:
        validacion = input("Error inserte la misma contraseña: ")
