# Ejercicio clase de repaso.
#if 
print("----------------------------------------------------------------------------------------")
print("Hola buenas, bienvenido a la calculadora")

iniciacion = True
while iniciacion == True:
    print("ingresa el operador que deseas usar (+(suma), -(resta), *(multiplicacion), /(division))")       
    operador = input()
    Numero_1 = int(input("Ingrese el primer numero: "))
    Numero_2 = int(input("Ingrese el segundo numero: "))

    if operador == "*":
        resultado = Numero_1 * Numero_2
        print(f"El resultado de la multiplicacion entre {Numero_1} y {Numero_2} es igual a {resultado}")
    elif operador == "+":
        resultado = Numero_1 + Numero_2
        print(f"El resultado de la suma entre {Numero_1} y {Numero_2} es igual a {resultado}")
    elif operador == "-": 
        resultado = Numero_1 - Numero_2
        print(f"El resultado de la resta entre {Numero_1} y {Numero_2} es igual a {resultado}")
    elif operador == "/":   
        resultado = float(Numero_1 / Numero_2)
        print(f"El resultado de la division entre {Numero_1} y {Numero_2} es igual a {resultado}")
    else:
        print("el dato ingresado no es valido")
    print("¿Desea realizar otra operacion? (Si/No)")
    dato = input()
    if dato == "No" or dato == "NO" or dato == "no" or dato == "n":
        iniciacion = False













print("-----------------------------------------------------------------------------------------")
print("Gracias por usar la calculadora")
print("-----------------------------------------------------------------------------------------")