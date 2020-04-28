'''Crear una lista con 10 números enteros y mostrarlos por pantalla. Luego
reemplazar todos los números pares por la palabra PAR y volver a mostrar la
lista por pantalla.'''
#impostamos la libreria que nos va a devolver numeros al azar
import random
#declaramos una variable tipo lista vacia
numeros = []
#generamos un for con el rango el cual va a recorrer lo que este dentro de ese rango
for i in range(10):
    #declaramos una variable donde le decimos que desde el numero inicial al
    #al final nos de una lista
    numeros.append(random.randint(1,100))
#mostramos la lista
print('La lista es: ',numeros)
#generamos un for con rango 10 para que muestre los numeros
for par in range(10):
    #recorremos un if buscando los numeros divisibles por 2
    if numeros[par]%2==0:
        #mostramos dichos numeros con la palabra par
        numeros[par]='par'
#mostramos por pantalla los numeros y los cambiados por la palabra par
print('La lista encontro y cambio los siguientes numero a la palabra par:',numeros)
