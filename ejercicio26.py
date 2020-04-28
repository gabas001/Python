'''Escribir un programa que genere 20 números al azar entre 1 y 5, los guarde
en una lista, muestre la lista y luego muestre los dos números que más se
repiten. En caso de haber dos o mas números con la misma cantidad de
apariciones, mostrarlos a todos. Por ejemplo, el número mas repetido es el 5,
mostramos el 5, pero en segundo lugar aparecen los números 2 y 4 con la misma
cantidad de repeticiones, mostrarlos a ambos, además de mostrar el 5.'''
#biblioteca para mostrar un numero al azar
import random
#creamos una variable de tipo lista vacia
lista = [ ]
#recorremos un for con rango 
for i in range (20):
    #pedimos al for que nos muestre entre dos numeros la cantidad pedida
    lista.append(random.randint(1, 5))
#mostramos los numeros en una lista
print (lista)
