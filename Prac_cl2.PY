#Solicite al cliente su nombre, apellido, edad y correo electrónico.

#Almacene estos datos en variables.

#Los muestre organizados en forma de una tarjeta de presentación en la pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
correoelectronico = input("Ingrese su correo electrónico: ")
print(nombre, apellido, edad, correoelectronico)

#Los muestre organizados en forma de una tarjeta de presentación en la pantalla.
print("/n-------Tarjeta de presentación -------")
print(f"Nombre: {nombre} {apellido}")
print(f"Edad: {edad} años")
print(f"Correo: {correoelectronico}")
print("-------------------------------------")

