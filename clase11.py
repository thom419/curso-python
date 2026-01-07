
#utilizar condicionales para gestionar las opciones del menu y las validaciones necesarias.

#Presentar un menu que permita elegir enre las funcionalidades disponibles:
  #agregar productos, visualizar, buscar y eliminar.

#El programa debe continuar funcionando hasta que se elija la opcion salir.
def menu():
    print("\nMenú de opciones:")
    print("1. Agregar producto")
    print("2. Visualizar productos")
    print("3. Buscar productos (pendiente)")
    print("4. Eliminar producto")
    print("5. Salir")

def agregar_productos():
    print("\nAgregar un producto")
    nuevo_producto = []

    nombre = input("Ingresá el nombre del producto: ")
    precio = input("Ingresá el precio del producto: ")
    cantidad = input("Ingresá la cantidad del producto: ")

    nuevo_producto.append(nombre)
    nuevo_producto.append(precio)
    nuevo_producto.append(cantidad)

    datos_productos.append(nuevo_producto)
    print("Producto agregado correctamente.")
    print(f"Estado actual de la lista: {datos_productos}")

def visualizar_productos():
    if not datos_productos:
        print("\nNo hay productos en la lista.")
        return

    print("\nProductos disponibles:")
    for i, producto in enumerate(datos_productos):
        nombre, precio, cantidad = producto
        print(f"{i + 1}. {nombre} - ${precio} - Cantidad: {cantidad}")

def buscar_productos():
    print("\nFuncionalidad de búsqueda aún no implementada.")

def eliminar_productos():
    if not datos_productos:
        print("\nNo hay productos para eliminar.")
        return

    print("\nEliminar producto")
    visualizar_productos()

    try:
        respuesta = int(input("Ingresá el número del producto a eliminar: "))
        respuesta = respuesta - 1  # para que coincida con el índice

        if 0 <= respuesta < len(datos_productos):
            eliminado = datos_productos.pop(respuesta)
            print(f"Producto eliminado: {eliminado[0]}")
        else:
            print("Número inválido. No existe esa posición.")
    except ValueError:
        print("Entrada inválida. Debés ingresar un número.")

# --- PROGRAMA PRINCIPAL ---

datos_productos = []  # lista general donde se guardan los productos
bucle = True

while bucle:
    menu()
    try:
        respuesta_menu = int(input("Seleccioná una opción: "))
        if respuesta_menu == 1:
            agregar_productos()
        elif respuesta_menu == 2:
            visualizar_productos()
        elif respuesta_menu == 3:
            buscar_productos()
        elif respuesta_menu == 4:
            eliminar_productos()
        elif respuesta_menu == 5:
            bucle = False
            print("Gracias por usar el programa. ¡Hasta la próxima!")
        else:
            print("Opción inválida. Intentá de nuevo.")
    except ValueError:
        print("Error: ingresá un número entre 1 y 5.")


archivo_productos = open("productos.txt", "w")
archivo_productos.write("Nombre,Precio,Cantidad\n")
for producto in datos_productos:
    archivo_productos.write(f"{producto[0]},{producto[1]},{producto[2]}\n")
archivo_productos.close()
# Leer el archivo y mostrar su contenido
archivo_productos = open("productos.txt", "r")
print("\nContenido del archivo productos.txt:")
for linea in archivo_productos:
    print(linea.strip())
archivo_productos.close()
# Guardar los nombres ingresados en un archivo y luego leerlos
archivo_nombre_prueba = open("nombres.txt", "a")
nombre = input("Ingrese su nombre: ")
archivo_nombre_prueba.write(f"{nombre}\n")  

