'''Escribir un programa que le solicite al usuario ingresar 10 palabras,
luego le pida ingresar una más y le diga si esa última palabra ingresada se
encuentra entre las 10 palabras ingresadas anteriormente.'''
#creamos una lista vacia
lista = []
#la recorremos con un por desde la posicion 0 a la 10
for i in range(0,10):
        #preguntamos al usuario las palabras que desea ingresar
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        #generamos un contador
        lista += [palabra]
#mostramos por pantalla dichas palabras
print("La lista creada es:", lista)
#le pedimos una mas
print("Dígame la palabra", str(i + 2) + ": ")
palabra = input()
#la agregamos a la lista
lista += [palabra]
#generamos una variable para buscar una palabra
buscar = input("Dígame la palabra a buscar: ")
#iniciamos un contador en 0
contador = 0
#recorremos un for de la lista de palabras
for i in lista:
        #consultamos si esta
        if i == buscar:
            contador += 1;
#si no esta mostramos mediante un print una leyenda indicando que no esta
if contador == 0:
        print("La palabra '" + buscar + "' no aparece en la lista.")
#si aparece mostramos que esta
elif contador == 1:
        print("La palabra '" + buscar + "' aparece una vez en la lista.")
#en este caso mostramos las veces que esta
else:
        print("La palabra '" + buscar + "' aparece", contador, "veces en la lista.")
    
