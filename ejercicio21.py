'''Escribir un programa que le pida al usuario que ingrese un número por teclado,
lo eleve al cubo y muestre el resultado por pantalla. El programa deberá seguir
funcionando hasta que el usuario ingrese el número cero.'''
#iniciamos la funcion con una variable
def cubico(num):
    #retornamos la variable con un resultado
    return num**3
#recorremos un while verdadero
while True:
    #iniciamos una variable con un input donde se pide al usuario que ingrese
    #algo por teclado
    num = int(input('Ingrese un numero (0 para salir) >>'))
    #verificamos lo ingresado con un if
    if num == 0:
        #pausa del sistema
        break
    #mostramos el resultado
    print('El cubo de', num, 'es:', cubico(num))
