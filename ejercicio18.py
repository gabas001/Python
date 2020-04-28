'''Escribir una función para determinar si un número entero, ingresado por
teclado es un número primo. Un número primo es aquel que solo tiene como
divisores enteros (resto igual a cero) al número 1 y a sí mismo, por ejemplo,
el número 5.'''
#declaramos una funcion con una variable
def primo(numero):
    #iniciamos una variable en 1
    factorial = 1
    #iniciamos una variable vacia pero string
    resul = ''
    #recorremos un for dentro del rango 1 y el numero elegido
    for a in range(1, numero):
        #multiplicamos el factorial por el numero
        factorial*=a
    #buscamos dentro del if si la condicion se da 
    if (factorial+1)%numero == 0:
        resul = 'es primo'
    #o si no se da
    else:
        resul = 'no es primo'
    #retornamos en un resultado
    return resul
#declaramos una variable con un input para pedir un numero
number = int(input('Ingrese un numero entero: '))
#mostramos el numero
print("El numero",number
      , primo(number))
