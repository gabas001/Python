'''Escribir un programa que llene una lista con 50 números al azar y muestre
por pantalla el número (o números) que más se repite. '''
#importamos la libreria random que }nos permite trabajar con numeros aleatorios
import random
#generamos un for que va a recorrer de un numero a otro dandonos un numero
for i in range(0,50):
    #mostramos dichos numeros
    print(random.randrange(1, 50, 1), end=' ')
