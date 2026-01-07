#¿Cuál es el propósito de un acumulador en un bucle?
# El propósito de un acumulador en un bucle es almacenar el resultado de una operación repetitiva a lo largo de las iteraciones del bucle.
# Por ejemplo, si queremos sumar una serie de números, podemos usar un acumulador para ir sumando cada número a medida que iteramos a través de ellos. Al final del bucle, el acumulador contendrá el resultado total de la operación.
# Ejemplo de uso de un acumulador en un bucle
# Sumar los números del 1 al 5
#acumulador = 0
#for i in range(1, 6):
 #   acumulador += i  # Sumar el valor de i al acumulador
#print("Suma acumulada:", acumulador)  # Resultado: 15
print("-----------------------------------------------------------------------------------------")

contador = 0

while contador < 3:

    print("Intento:", contador)

    contador += 1
