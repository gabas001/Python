'''Hacer un menú de cuatro opciones, que le permita al usuario navegar por
cuatro módulos diferentes del programa. Mostrar en cada módulo un título
diferente para verificar que funciona correctamente'''
#importamos la libreria mscrt para poder usarla
#esta libreria nos permite presionar una tecla para continuar
import msvcrt
#declaramos una funcion
def suma():
    #le decimos la operacion a realizar
    print('Suma')
    #declaramos variables, donde le pedimos al usuario que ingrese algo
    num1 = float(input('Ingrese el primer numero'))
    num2 = float(input('Ingrese el segundo numero'))
    #retornamos en la ecuacion realizada para mostrar su resultado
    return num1+num2
#mostramos el resultado
print(suma())

def resta():
    print('resta')
    num1 = float(input('Ingrese el primer numero'))
    num2 = float(input('Ingrese el segundo numero'))
    return num1-num2
print(resta())

def mult():
    print('multiplicacion')
    num1 = float(input('Ingrese el primer numero'))
    num2 = float(input('Ingrese el segundo numero'))
    return num1*num2
print(mult())

def division():
    print('Division')
    num1 = float(input('Ingrese el primer numero'))
    num2 = float(input('Ingrese el segundo numero'))
    return num1/num2
print(division())
#declaramos una funcion
def frenar():
    #pedimos que presione una tacla
    print('Presione una tecla para seguir')
    #utilizamos la libreria para acceder a esa funcion
    msvcrt.getch()
print(frenar())
#generamos una funcion de menu
def menu():
    Mostramos dicho menu
    print('1-suma')
    print('2-resta')
    print('3-multiplicacion')
    print('4-division')
    print('5-salir')
    print(menu())
