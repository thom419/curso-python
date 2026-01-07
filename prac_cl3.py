print("Ejercicio clase 3")
#Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.
#Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor a 18 años.
#Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto "ERROR!".
print("---------------------")

nombre = input("Ingrese su nombre: ")

apellido = input("Ingrese su apellido: ")

edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Error usted es menor de edad")
else:
    print("Edad correcta")
if edad >99:
    print("Error, edad incorrecta")


correoelectronico = input("Ingrese su correo electrónico: ")
print(nombre, apellido, edad, correoelectronico)

# datos organizados en forma de una tarjeta de presentación en la pantalla.
print("/n-------Tarjeta de presentación -------")
print(f"Nombre: {nombre} {apellido}")
print(f"Edad: {edad} años")
print(f"Correo: {correoelectronico}")
print("-------------------------------------")
