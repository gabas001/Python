'''Escribir una función que encuentre los números primos comprendidos entre dos
números enteros ingresados por teclado.'''
#creamos una variable tipo lista vacia
primos = []
#declaramos una funcion con una variable
def primo(numero):
    #iniciamos la variable en 1
    factorial = 1
    #recorremos un for desde el rango 1 al numero elegido
    for a in range(1, numero):
        factorial*=a
    #iniciamos un if con el factorial en 1 le sumamos uno mas y dividimos por el
    #numero elegido
    if (factorial+1)%numero == 0:
        primos.append(numero)
#pedimos por teclado que se ingesen los numeros
min = int(input('Ingrese el numero donde comienza: '))
max = int(input('Ingrese el numero en el que termina: '))
#calculamos con un if cual es el mayor
if min<max:
    #recorremos con un for el if
    for a in range(min, max):
        primo(a)
else:
    print('El segundo numero debe ser mayor que el primero.')
#mostramos por pantalla los numeros
print('Los numeros primos entre',min,'y',max,'son',primos)
