
# Ejemplo 1: Función para sumar dos números
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"La suma de 5 y 3 es: {resultado}")

# Ejemplo 2: Función para verificar si un número es par
def es_par(numero):
    return numero % 2 == 0

numero = 4
if es_par(numero):
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Ejemplo 3: Función para calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"El factorial de {num} es: {factorial(num)}")

# Ejemplo 4: Función para convertir grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

grados_celsius = 25
print(f"{grados_celsius}°C son {celsius_a_fahrenheit(grados_celsius)}°F")

# Ejemplo 5: Función para encontrar el máximo de una lista
def encontrar_maximo(lista):
    return max(lista)

numeros = [3, 7, 2, 8, 4]
print(f"El número máximo en la lista es: {encontrar_maximo(numeros)}")