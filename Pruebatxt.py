
nombre = input("Ingrese su nombre: ")
archivo_nombre_prueba = open("nombres.txt", "a")
archivo_nombre_prueba.write(f"{nombre}\n")
archivo_nombre_prueba.close()

archivo_nombre_prueba = open("nombres.txt", "r")
for linea in archivo_nombre_prueba:
    print(linea.strip())
archivo_nombre_prueba.close()
