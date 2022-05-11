# tipos basicos

# int, str, float, bool

# tipos colecciones

# lista , matriz, tupla, diccionario


# --------------tupla---------------

mi_tupla = (1, True, "hola", 3.45)
print(mi_tupla[2])
print(type(mi_tupla))
#mi_tupla[1] = 23  ---> no es posible asignacion en tupla , da error.


conexion_bd = "127.0.0.1", "root", "qwerty", "nomina"
print(conexion_bd)
print(type(conexion_bd))


conexion_completa = conexion_bd, "33016", "10"
print(conexion_completa)
print(type(conexion_completa))

print("usuario:", conexion_completa[0][1])
