'''Escribir una función en Python para calcular el factorial de un número entero
positivo. Basarse en la siguiente definición: El factorial de un número entero
positivo n, se define como el producto de todos los números enteros positivos
menores o iguales a n. El factorial de cero es 1. Por ejemplo, el factorial
de 4 será 4x3x2x1 = 24.
No utilizar ningún módulo matemático, solo lo visto en clase.'''
#declaramos una funcion que va a recorrer una variable
def factor(numero):
    #declaramos una funcion inicializada en 1
    factorial = 1
    #recorremos un for desde una variable vacia hasta un rango ya definido
    for a in range(1, numero+1):
        #hacemos que se acumule y se sume
        factorial=factorial*a
    #retornamos en la variable inicializada
    return factorial
#pedimos que se ingrese por teclado un numero entero
nume = int(input("Ingrese el numero para calcular su factorial: "))
#mostramos por pantalla el resultado
print("El factorial de ", nume, " es ", factor(nume))
