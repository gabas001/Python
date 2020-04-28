'''Pedir al usuario que ingrese una frase y luego le muestre la frase
ingresada y la cantidad de veces que aparece cada vocal.'''
#iniciamos una funcion con variable
def contarvocales(frase):
    #iniciamos una variable con contador en 0
    vocal = 0
    #creamos un for el cual recorrera la funcion
    for i in frase:
        #hacemos un if donde ira ubicacion por ubicacion recorriendo la variable
        #buscando si es igual a lo establecido
        if i == 'a' or i == 'e' or i == 'i' or i =='o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i =='O' or i == 'U':
            #el contador aumentara segun la cantidad que indique el if
            vocal=vocal+1
    #retornara en la variable finalizada
    return vocal
#iniciamos una variable de tipo input donde pediremos que se ingrese datos
frase = input('ingresa frace: ')
#mostramos los datos ingresados y el resultado de la funcion
print (contarvocales(frase))
