'''Escribir un programa que le pida dos números al usuario y muestre por
pantalla todos los números pares que hay entre ambos números, incluyendo,
en caso de ser pares, los números que ingresó el usuario.'''

#se pide al usuario que ingrese numeros mediante un imput que solo ingresa enteros
n1= int(input('Imprima el primer numero'))
n2= int(input('Imprima el segundo numero'))
#se recorre un for entre los numeros ingresados 
for i in range(n1,n2):
    if i%2!=1:
        #muestra la cantidad de pares que ahi entre los numeros ingresados
        print(i)
