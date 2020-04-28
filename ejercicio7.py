'''Escribir un programa que pida ingresar un número entero mayor que cero por
teclado. Verificar si el número ingresado es múltiplo de 2, 3, 4, 5, 6, 7,8 o 9.
Armar una lista con los números encontrados (por ejemplo, si el número
ingresado es múltiplo de 3,6 y 7, armamos una lista que contenga estos tres
números). Mostrar la lista por pantalla, ordenada de mayor a menor.
En caso de que el número ingresado no sea múltiplo de estos números,
mostrar por pantalla el mensaje “No se encontraron divisores exactos”.'''
#se declaran variables inicializadas en 0
mul3=0
mul6=0
mul7=0
#se declara una variable donde se le pide que ingrese un entero
valor=int(input("Ingrese un valor:"))
#mediente un if segun el valor ingresado va a buscar el resultado
if valor%3==0:
        mul3=mul3+1
if valor%6==0:
        mul6=mul6+1
if valor%7==0:
        mul7=mul7+1
#muestra el resultado de las operaciones
print("El valor ingresado es múltiplo de 3")
print(mul3)
print("El valor ingresado es múltiplo de 6")
print(mul6)
print("El valor ingresado es múltiplo de 7")
print(mul7)
