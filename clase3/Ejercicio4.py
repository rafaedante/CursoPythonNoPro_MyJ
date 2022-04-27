# input(): nos permite ingresar datos desde la consola y procesarlo

# int
# str
# float
# bool

nombre = input("escriba su nombre: ")
edad = int(input("ingrese su edad: "))  # int("20") -> 20
print("Hola como estas", nombre)


if edad >= 18:
	print("sos mayor de edad")

print("fin del programa")
