def ingreso_datos_personales ():
    # Solicitar datos personales al usuario
    print("--------Bienvenido al carrito de compras-------------")
    print("Por favor, ingrese sus datos personales para continuar.")
    print("-----------------------------------------------------")
    print("Nota: Asegúrese de ingresar los datos correctamente.")
    print("-----------------------------------------------------")
    print("Los campos no deben estar vacíos y la edad debe ser correcta.")
    print("-----------------------------------------------------")
      
    nombre = input("Ingrese su nombre: ").capitalize().strip()
   
    apellido = input("Ingrese su apellido: ").capitalize().strip()
   
    edad = input("Ingrese su edad: ").strip()
    
    while not edad.isdigit() or int(edad) < 0 or int(edad) < 18:
        print("Edad inválida. Debe ser un número positivo. y mayor a 18 años.")
        edad = input("Ingrese su edad: ").strip()
    
    while correoelectronico := input("Ingrese su correo electrónico: ").strip():
        if '@' not in correoelectronico and '.' not in correoelectronico and 'com' not in correoelectronico or "gmail" not in correoelectronico: 
            print("Correo electrónico inválido. Debe contener '@' y '.'")
        else:
            break
    correoelectronico = input("Ingrese su correo electrónico: ").strip()
    
    #datos organizados en forma de una tarjeta de presentación en la pantalla.
    print("--------Bienvenido al carrito-------------")
    print(f"Bienvenido {nombre} {apellido} de {edad} años.")
    print(f"Correo electrónico: {correoelectronico}")
    print("---------------------")


ingreso_datos_personales()

archivo = open(ingreso_datos_personales.txt, "a")


