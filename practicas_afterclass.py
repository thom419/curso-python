
# Inicializar la lista de productos
productos = []

 #menu desplegable
condicion = True
while condicion:
    print("\n--- Menú de Productos ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. buscar productos")
    print("4. eliminar productos")  
    print("5. Salir")
    
    respuesta = int(input("aca ingresa que te gustaria hacer"))
    if respuesta == 1:
        nombre = input("Ingrese el nombre del producto: ")
    elif respuesta == 2:
        if productos:
            print("Lista de productos:")
            for i, producto in enumerate(productos):
                print(f"{i+1}. Nombre del producto: {producto.get('nombre')}. Precio: ${producto.get('precio')}")
        else:
            print("La lista de productos está vacía.")
        
    elif respuesta == 3:
        nombre = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in productos:
            if producto.get('nombre').lower() == nombre.lower():
                print(f"Producto encontrado: {producto.get('nombre')}, Precio: ${producto.get('precio')}")
                encontrado = True
                break
        if not encontrado:
            print(f"El producto '{nombre}' no se encuentra en la lista.")
        
    elif respuesta == 4:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
        for producto in productos:
            if producto.get('nombre').lower() == nombre.lower():
                productos.remove(producto)
                print(f"Producto '{nombre}' eliminado con éxito.")
                encontrado = True
                break
        if not encontrado:
            print(f"El producto '{nombre}' no se encuentra en la lista.")
    
    elif respuesta == 5:
        condicion = False
    print("Saliendo del programa...")
    
   