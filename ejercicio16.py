'''Modificar el ejercicio anterior, para que el usuario pueda en cada opción del
programa, ingresar dos números enteros y que en cada opción a esos números se
les aplique una suma, una resta, una división o una multiplicación. Agregar una
nueva opción para que el programa funcione permanentemente hasta que el usuario
la seleccione y el programa finalice su ejecución.'''
#importamos la libreria msvcrt que nos permite oprimir una tecla despues de una
#pausa
import msvcrt
#declaramos una funcion
def suma():
    #mostramos la ecuacion a realizar
    print('Suma')
    #declaramos variables donde le pedimos al usuario que ingrese algo
    num1 = float(input('Ingrese el primer numero'))
    num2 = float(input('Ingrese el segundo numero'))
    #retornamos en la ecuacion mostrando el resultado
    return num1+num2
def resta():
    print('Suma')
    num1 = float(input('Ingrese el primer numero'))
    num2 = float(input('Ingrese el segundo numero'))
    return num1-num2
def mult():
    print('Suma')
    num1 = float(input('Ingrese el primer numero'))
    num2 = float(input('Ingrese el segundo numero'))
    return num1*num2
def division():
    print('Division')
    num1 = float(input('Ingrese el primer numero'))
    num2 = float(input('Ingrese el segundo numero'))
    return num1/num2
def menu():
    #mostramos por pantalla un menu
    print('1-suma')
    print('2-resta')
    print('3-multiplicacion')
    print('4-division')
    print('5-presione s para salir')
#recorremos un while donde le decimos que elija una opcion
while True:
    menu()
    #declaramos una variable donde le pedimos que elija una opcion 
    opcion = input('Ingrese a los calculos deseados')
    #recorremos un if elif donde dependiendo la opcion elejida va a salir
    #por esa opcion
    if opcion == '1':
        print('El resultado de la suma es', suma())
    elif opcion == '2':
        print('El resultado de la resta es', resta())
    elif opcion == '3':
        print('La multiplicacion es', mult())
    elif opcion == '4':
        print('La cociente de la division es', division())
    #en esta opcion el usuario va a presionar una tecla para continuar
    elif opcion == 's':
        #pausa del sistema
        break
    else:
        print('Incorrecto')
