
from datetime import datetime

nombre = input ("ingrese su nombre :")

def diahorario():
    fecha_hora_actual = datetime.now()
    
    print(f"hola {nombre} hoy es {fecha_hora_actual}, bienvenido")

diahorario()

#se guardaran los datos ingresados en un archivo .txt

documento = open("nombres_fechas.txt", "a")
documento.write()
documento.close ()
