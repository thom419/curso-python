#while
#hace posible repetir el codigo de manera infinita
# o de manera finita "con un numero de iteraciones definidas " 

#inicio = 0
#while inicio <= 10:
 #print(f"El valor de la variable inicio en la vuelta {inicio +1} vale = {inicio}")
 #inicio = inicio + 1
numerofavorito=0

print("______________________________________")
for numero in range(-2,11) :
    print(f"el valor de numero en la vuelta {numero+1} vale = {numero}")
    if numero == 7:
        numerofavorito = numero
print(f"el numero favorito de facu es {numerofavorito}")
print("______________________________________")
