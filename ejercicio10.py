'''Escribir un programa que permita al usuario ingresar por teclado tantos
números enteros como desee. Cuando no quiera ingresar más números, deberá
ingresar el cero. A continuación, determinar cuál de los números ingresados es
el mayor y cuál es el menor. Mostrar ambos por pantalla.'''

print('Ingresa tantos numeros enteros como quieras')
print('para finalizar oprime 0')
#se declara una variable y se le pide mediante un imput de tipo entero que
#ingrese un numero
n=int(input('numero entero: '))
#se declaran dos variables inicializadas en 0
mayor = n
menor = n
#el while va a recorrer las variables hasta que el usuario oprima 0
while n!=0:
    #los if van a determinar cual numero es mayor y cual es menor
    if n>mayor:
        mayor=n
    if n<menor:
        menor=n
    n=int(input('numero entero: '))
#mediante el print se van a mostrar dichos numeros
print('El mayor numero ingresado es: ', mayor)
print('El menor numero ingresado es: ', menor)
