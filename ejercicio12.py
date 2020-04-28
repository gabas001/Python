'''Escribir un programa que le pregunte al usuario cuantas palabras desea
ingresar, luego le permita ingresarlas todas y finalmente mostrarlas por
pantalla.'''
#creamos una variable con un input de tipo entro donde le pedimos al usuario que
#ingrese datos
palabras= int(input('Cuantas palabras va a introducir? '))
#iniciamos el if diciendole que no puede introducir menos de una palabra
if palabras < 1:
    print('Imposible!')
#vamos por la parte donde ingreso mas de una 
else:
    #creamos una lista vacia
    lista = []
    #creamos un for que recorra dichas palabras 
    for i in range(palabras):
        print('escriba la palabra ', str(i+1) + ':', end='')
        letras = input()
        #calculamos cuantas alabras ingreso
        lista += [letras]
    #nostramos por un print las palabras
    print('La lista de palabras ingresada es: ',lista)
