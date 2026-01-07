#posible proyecto de maquina de apuestas

#PERSISTENCIA DE DATOS 
# Archivos .txt (texto)
# Archivos .csv (valores separados por comas)
# Archivos .log (registros de eventos)   

# se pueden leer o escribir y abrir archivos de texto, csv y log
  # open() abre un archivo y devuelve un objeto de archivo
  # read() lee el contenido del archivo
  # write() escribe contenido en el archivo
  # close() cierra el archivo

#modos de apertura de archivos
# 'r' - lectura (read)
# 'w' - escritura (write), si el archivo no existe, se crea; si existe, se sobrescribe
# 'a' - anexar (append), si el archivo no existe, se crea; si existe, se agrega al final
# "r+" - lectura y escritura, el archivo debe existir




from datetime import datetime

nombre = input("Ingrese su nombre: ")

def DiaHorario():
  fecha_hora_actual = datetime.now()
  print("Fecha y hora actual:", fecha_hora_actual)
  print("Solo la fecha:", fecha_hora_actual.strftime("%Y-%m-%d"))
  print("Solo la hora:", fecha_hora_actual.strftime("%H:%M:%S"))
  print("Fecha legible:", fecha_hora_actual.strftime("%d de %B de %Y"))






import random
def lanzar_dado():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"valor dado 1 :{dado1}\n  valor dado 2 :{dado2}")
    suma = dado1 + dado2
    fecha_hora_actual = datetime.now()
    print(f"la suma de los dados dio:{suma}, en el dia {fecha_hora_actual}")
    return dado1, dado2, suma

dado1, dado2, suma = lanzar_dado()

archivo = open("DADOS.txt", "a")
archivo.write(f"{nombre}\n")
archivo.write(f"Dado 1: {dado1}\n")
archivo.write(f"Dado 2: {dado2}\n")
archivo.write(f"Suma: {suma}\n")
archivo.write(f"Fecha y hora: {datetime.now()}\n")
archivo.close ()







